import asyncio
import json
import os
import time  # Import the time module
from typing import Optional

from browser_use import ActionResult, Agent, Browser, BrowserConfig, Controller
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, SecretStr

from getAddress import get_address


async def run_scraper(keyword, long, lat):
    location = get_address(lat, long)

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError('GEMINI_API_KEY is not set')

    # Initialize the model
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))

    # Define the base model for place details
    class Place(BaseModel):
        name: str
        address: Optional[str] = None
        hours: Optional[str] = None
        pricing: Optional[str] = None
        website: Optional[str] = None

    class Places(BaseModel):
        places: list[Place]

    controller = Controller(output_model=Places)

    # Browser configuration (Make headless True for production)
    browser = Browser(
        config=BrowserConfig(
            headless=True,
        )
    )

    # Construct a valid Google Maps search URL
    google_maps_base_url = "https://www.google.com/maps/search/"
    search_query = f"{keyword} near {location}".replace(" ", "+")
    search_url = f"{google_maps_base_url}{search_query}"

    initial_actions = [
        {'open_tab': {'url': search_url}},  # Open Google Maps with a valid search URL
        {'scroll_down': {'amount': 1000}},  # Scroll down to load more results
    ]

        # Record the start time
    start_time = time.time()
        
    agent = Agent(
        task = """Grab the following information for first 4 places: name, address, hours, pricing(DIsplay pricing using '$' symbol, you may guess if not avaiable), website(grab website from the website button)""",
        llm=llm, browser=browser, initial_actions=initial_actions, controller=controller,
    )
    await agent.run()
    
    # Run the agent
    history = await agent.run(max_steps=5)
    result = json.loads(history.final_result())


    # Print results
    for v in result["places"]:
        print('\n--------------------------------')
        print(f'Title:            {v["name"]}')
        print(f'URL:              {v["website"]}')
        print(f'Address:          {v["address"]}')
        print(f'Hours:            {v["hours"]}')
        print(f'Pricing:          {v["pricing"]}')
    
    # Record the end time and calculate the duration
    end_time = time.time()
    duration = end_time - start_time
    print(f"\nTime taken to grab all information: {duration:.2f} seconds")
    return result["places"]