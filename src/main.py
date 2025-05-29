import os
import sys

from langchain_community.utilities import SearxSearchWrapper
from langchain.agents import initialize_agent, AgentType
from langchain_openai import AzureChatOpenAI
from langchain_community.tools import Tool
from dotenv import load_dotenv

load_dotenv()

def main():
    try:
        searx = SearxSearchWrapper(
            searx_host=os.getenv("SEARXNG_HOST"),
        )

        llm = AzureChatOpenAI(
            temperature=0,
            api_version=os.getenv("OPENAI_API_VERSION"),
            azure_deployment=os.getenv("OPENAI_CHAT_DEPLOYMENT_NAME"),
            api_key=os.getenv("OPENAI_API_KEY"),
            azure_endpoint=os.getenv("OPENAI_ENDPOINT"),
        )

        result = searx.run("What is artificial intelligence?")
        print("Basic search result:", result)

        search_tool = Tool(
            name="searx_search",
            func=lambda query: searx.run(query),
            description="Useful for searching the web for information. Input should be a search query."
        )

        agent = initialize_agent(
            [search_tool],
            llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )
        
        result = agent.invoke("What are the latest developments in quantum computing in 2025?")
        print("Agent result:", result)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
