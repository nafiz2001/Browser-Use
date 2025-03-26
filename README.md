# LangChain Agent with Browser Use for Social Media Automation

This project demonstrates how to use LangChain, specifically with Google Generative AI (Gemini 2.0 Flash Experimental), in conjunction with a web browser automation tool (based on `browser_use`) to perform tasks on websites like Facebook.  The goal is to create an agent that can navigate to a specified website (in this case, Facebook), log in (requires you to handle credentials appropriately outside of this code), and perform actions like posting a message.

**Key Components:**

*   **LangChain:** Used for creating an intelligent agent that can understand instructions and plan actions.  We're leveraging `ChatGoogleGenerativeAI` as the language model.
*   **`browser_use`:** A library for controlling a Chrome browser programmatically. This allows the agent to interact with web pages, fill out forms, click buttons, and extract information.
*   **Google Gemini 2.0 Flash Experimental:** The selected language model to drive the agent's decision-making.
*   **Asyncio:**  The code is built using `asyncio` for concurrent execution, ensuring efficient browser interaction.
*   **dotenv:** loads the api key from the .env file

**How it Works:**

1.  **Configuration:** The script configures the `Browser` object to connect to an existing Chrome instance.  **Important:** You need to specify the correct path to your Chrome executable in the `chrome_instance_path` setting. This path is different depending on your operating system (Windows, macOS, Linux).
2.  **Agent Initialization:** An `Agent` is created with a specific task (e.g., "go to my facebook account and post hi everyone").  The agent is linked to the language model (`llm`) and the browser (`browser`).
3.  **Task Execution:** The `agent.run()` method executes the task.  The agent uses the language model to determine the necessary steps, and then uses the browser to interact with the website.
4.  **Result Extraction:** The `result.extracted_content()` method retrieves any relevant information from the execution, which can then be printed or further processed.
5.  **Browser Closure:**  The `browser.close()` method properly closes the browser instance when the task is complete.

**Prerequisites:**

*   **Python 3.7+**
*   **Installed Packages:**
    ```bash
    pip install langchain langchain-google-genai python-dotenv browser-use
    ```
*   **Google API Key:** You need a Google API key enabled for the Gemini API.  Store this key securely in a `.env` file in the same directory as the script.
    ```
    GOOGLE_API_KEY=YOUR_API_KEY
    ```
*   **Chrome Browser:** You must have Google Chrome installed. The script requires the correct path to the Chrome executable.
*   **browser_use**:  This library allows controlling Chrome.  Refer to its documentation for installation and usage.

**Important Considerations:**

*   **Authentication (Facebook Login):** The current script does *not* handle Facebook login.  You will need to implement a secure and reliable mechanism to authenticate with Facebook. This typically involves handling cookies, using a headless browser, or exploring Facebook's API.  **Do not hardcode credentials directly in the script.** Use environment variables or a secure configuration file.
*   **Error Handling:** Robust error handling is crucial.  The script should handle cases where the website is unavailable, elements are not found, or login fails.
*   **Rate Limiting:** Be mindful of Facebook's rate limits.  Excessive automated requests can lead to your account being restricted.
*   **Terms of Service:**  Always adhere to Facebook's Terms of Service. Automated scraping or posting may be prohibited.
*   **Security:**  Be extremely careful with your credentials and any data you extract from websites.  Use secure coding practices to prevent vulnerabilities.
*   **API Key Safety:** Ensure your Google API key remains private. Avoid committing it directly to your code repository. Use environment variables (as shown) and protect your `.env` file.

**How to Use:**

1.  **Install Dependencies:** Run `pip install langchain langchain-google-genai python-dotenv browser-use`.
2.  **Set up `.env`:** Create a `.env` file with your Google API key: `GOOGLE_API_KEY=YOUR_API_KEY`.
3.  **Configure Chrome Path:**  Modify the `chrome_instance_path` variable in the script to point to your Chrome executable.
4.  **Implement Authentication:** Add your Facebook login logic (safely!).
5.  **Run the Script:**  Execute the Python script.

**Example Usage (after implementing Facebook login):**

```python
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
