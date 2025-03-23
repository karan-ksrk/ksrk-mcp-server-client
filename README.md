## Requirements

- Python 3.13
- Dependencies listed in `pyproject.toml`

## Installation

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd documentation
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   Create a `.env` file in the root directory with the following content:

   ```env
   SCRAPING_DOG_API_KEY=your_scraping_dog_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

### Running the Client

1. Navigate to the root directory:

   ```sh
   cd ..
   ```

2. Run the client:

   ```sh
   python client.py
   ```

3. Enter your prompts in the interactive prompt loop. Type `quit` or `exit` to stop the client.

## Project Files

### `client.py`

This file contains the main client code that interacts with the MCP server and OpenAI's GPT-4 model. It includes the following key components:

- `MCPClient`: A class that manages the connection to the MCP server and provides methods to retrieve available tools and call them.
- `agent_loop`: An asynchronous function that processes user queries using the LLM and available tools.
- `main`: The main function that sets up the MCP server, initializes tools, and runs the interactive loop.

### `ksrk-mcp/ksrk-mcp-server.py`

This file contains the MCP server implementation. It includes the following key components:

- `search_web`: An asynchronous function that searches the web using the ScrapingDog API.
- `fetch_url`: An asynchronous function that fetches the content of a URL.
- `about_ksrk`: An MCP tool that searches for details about "ksrk" on a given website.

### `ksrk-mcp/test-website.py`

This file contains a script to test website scraping using `httpx` and `BeautifulSoup`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://openai.com) for providing the GPT-4 model.
- [ScrapingDog](https://scrapingdog.com) for the web scraping API.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for parsing HTML and XML documents.
- [httpx](https://www.python-httpx.org) for the HTTP client.
