from crewai import Crew, Agent, Task, Process
from langchain_community.tools import DuckDuckGoSearchRun
from crewai_tools import tools
import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from crewai import Agent, Task, Crew
from langchain.tools import tool
from langchain_community.chat_models import ChatOllama
from tools import search


llm=ChatOllama(model='llama3')
# Define agents with specific roles and tools
researcher = Agent(
    role='Senior Research Analyst',
    goal='Discover innovative AI technologies',
    backstory="""You're a senior research analyst at a large company.
        You're responsible for analyzing data and providing insights
        to the business.
        You're currently working on a project to analyze the
        trends and innovations in the space of artificial intelligence.""",
    tools=[search],
    llm=llm,
    memory=True,
    allow_delegation=True
)

writer = Agent(
    role='Content Writer',
    goal='Write engaging articles on AI discoveries',
    backstory="""You're a senior writer at a large company.
        You're responsible for creating content to the business.
        You're currently working on a project to write about trends
        and innovations in the space of AI for your next meeting.""",
        llm=llm,
    verbose=True,
    memory=True,
    allow_delegation=False
)