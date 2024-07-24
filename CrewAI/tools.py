from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

@tool('DuckDuckGoSearch')
def search(search_query: str):
    """Search the web for information on a given topic"""
    return DuckDuckGoSearchRun().run(search_query)
