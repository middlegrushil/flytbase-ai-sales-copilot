import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_company(company_name):
    """
    Searches the web for company information using Tavily.
    """

    query = f"""
    {company_name} company overview,
    industry,
    operations,
    recent news,
    drone inspections,
    industrial automation
    """

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    return response