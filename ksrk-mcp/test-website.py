import httpx
from bs4 import BeautifulSoup
import asyncio  # Import asyncio


async def fetch_url(url: str):
    text = """"""
    async with httpx.AsyncClient() as client:
        try:
            text = ""
            response = await client.get(url, timeout=30.0)

            # Check if the response is HTML or text
            content_type = response.headers.get("Content-Type", "")
            if "text/html" in content_type or "text/plain" in content_type:
                soup = BeautifulSoup(response.text, "html.parser")
                for string in soup.stripped_strings:
                    text += string + "\n"
                return text
            else:
                return f"Unsupported content type: {content_type}"

        except httpx.TimeoutException:
            return "Timeout Error"


async def main():

    url = "https://ksrk.in"
    text = await fetch_url(url)  # Use await here to call the async function
    print(text)


if __name__ == "__main__":
    asyncio.run(main())  # Run the main async function using asyncio.run()
