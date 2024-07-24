from crewai import Task
from tools import search
from agents import researcher, writer

# Create tasks for the agents
research_task = Task(
    description='Identify breakthrough AI technologies',
    agent=researcher,
    expected_output='A bullet list summary of the top 5 most important AI news'
)
write_article_task = Task(
    description='Draft an article on the latest AI technologies',
    agent=writer,
    expected_output='3 paragraph blog post on the latest AI technologies'
)
