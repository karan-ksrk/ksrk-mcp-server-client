from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import httpx
import json
import os
from bs4 import BeautifulSoup


load_dotenv()

mcp = FastMCP("ksrk-mcp")

USER_AGENT = "ksrk-mcp/1.0"
SCRAPING_DOG_URL = "https://api.scrapingdog.com/google"

ksrk_url = {
    "ksrk": "ksrk.in",
    "karan-ksrk": "ksrk.in",
    "karan ksrk": "ksrk.in",
    "karan": "ksrk.in"
}


async def search_web(query: str) -> dict | None:
    url = "https://api.scrapingdog.com/google"

    params = {
        "api_key": os.getenv("SCRAPING_DOG_API_KEY"),
        "query": query,
        "results": 2,
        "country": "us",
        "page": 0,
        "advance_search": "false"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                url,  params=params, timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException:
            return {"organic": []}


async def fetch_url(url: str):
    async with httpx.AsyncClient() as client:
        try:
            text = ""
            response = await client.get(url, timeout=30.0)
            soup = BeautifulSoup(response.text, "html.parser")
            for string in soup.stripped_strings:
                if "%PDF-1.5" in string:
                    break
                text += string + "\n"
            return text
        except httpx.TimeoutException:
            return "Timeout Error"


@mcp.tool()
async def about_ksrk(query: str, website: str):
    """
    Search for the details about the ksrk in the given website.
    details include project, social media links, and about, experience, education, phone or contact details.

    Args:
        query (str): The query to search for (e.g. "projects by ksrk or karan, ksrk social media links (github, linkedin, instagram, twitter), education, experience
        or about").
        website (str): The website to search in (e.g. "ksrk, karan, karan-ksrk, karan ksrk").

    Returns:
        return response should be very small and concise.
        List of dictionaries containing the text from the search results.
    """
    if website not in ksrk_url:
        raise ValueError(f"Website {website} not supported by this tool")

    query = f"site:{ksrk_url[website]} {query}"
    results = await search_web(query)

    if len(results["organic_results"]) == 0:
        return "No results found"

    text = ""
    for result in results["organic_results"]:
        text += await fetch_url(result["link"])
    return text


if __name__ == "__main__":
    mcp.run(transport='stdio')
