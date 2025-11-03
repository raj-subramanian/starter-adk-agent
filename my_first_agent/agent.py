from Google.adk.agents import agent

root_agent = Agent(
    name= "My First Agent",
    model ="gemini-2.0-flash",
    description ="An example Agent",
    instruction = """ You are an agent that helps with Google cloud related questions """,
)