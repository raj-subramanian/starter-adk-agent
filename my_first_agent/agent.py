from google.adk.agents import Agent

root_agent = Agent(
    name= "My_First_Agent",
    model ="gemini-2.0-flash",
    description ="An example Agent",
    instruction = """ You are an agent that helps with Google cloud related questions """,
)