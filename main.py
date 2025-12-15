import asyncio
from dotenv import load_dotenv
load_dotenv()

import os
async def main():
    print("Hello from mcp-adapters!")
    print("Environment variables loaded successfully.")
    print(f"LANGSMITH_API_KEY: {os.getenv('LANGSMITH_API_KEY')}")


if __name__ == "__main__":
   asyncio.run(main()) 
