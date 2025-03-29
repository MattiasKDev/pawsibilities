from pydantic import SecretStr, BaseModel
from typing import Optional
import os, json
from browser_use import Agent, Controller, ActionResult, BrowserConfig, Browser
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio
# from playwright import pw

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
    config = BrowserConfig(
        headless=False,
        disable_security=False,
    )
)

initial_actions = [{'open_tab': {'url': 'https://www.google.com'}}]

async def main():
    # Initialize the agent with the browser configuration
    agent = Agent(
        task="""Find the closest bowling places to the following coordinates: 43.52° North and longitude 79.71° West
        and extract the following things: name, address, hours, pricing, and website""",
        llm=llm,
        controller=controller,
        # browser=browser,
        initial_actions=initial_actions,
    )
	
    history = await agent.run()

    result = history.final_result()

    for v in json.loads(result)["places"]:
            print('\n--------------------------------')
            print(f'Title:            {v["name"]}')
            print(f'URL:              {v["website"]}')
            print(f'Address:          {v["address"]}')
            print(f'Hours:            {v["hours"]}')
            print(f'Pricing:          {v["pricing"]}')

asyncio.run(main())