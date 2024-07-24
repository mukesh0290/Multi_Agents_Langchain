from crewai import Crew,Process
from agents import researcher, writer
from tasks import research_task, write_article_task

# Assemble the crew with a sequential process
my_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_article_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)


inputs = {'topic': 'AI in healthcare'}
result = my_crew.kickoff(inputs=inputs)
print(result)