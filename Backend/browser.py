from pydantic import SecretStr
import os
from browser_use import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI  # Import the missing class
load_dotenv()

import asyncio


api_key = os.getenv("GEMINI_API_KEY")

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))


async def main():
    agent = Agent(
        task="Find the price of nike airforce 1",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())