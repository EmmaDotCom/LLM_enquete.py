import numpy
import requests
from bs4 import BeautifulSoup
from ollama import generate
from functions.load_extensions import load_extensions

async def main():
  load_extensions(braincells)
  start_ia()

await main()
