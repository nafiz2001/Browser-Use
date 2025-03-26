from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
load_dotenv()

import asyncio


# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp')

async def main():
    agent = Agent(
        task="go to my facebook account and post  hi everyone",
        llm=llm,
        browser=browser,
    )
    result = await agent.run()
    print(result.extracted_content())
    await browser.close()


asyncio.run(main())