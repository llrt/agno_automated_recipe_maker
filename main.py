from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv

load_dotenv() # Read env vars from .env file
print("Env vars loaded..")

# Define LLM model
MODEL_ID = "gemini-2.5-flash"

# Using Google AI Studio
agent = Agent(
    model=Gemini(id=MODEL_ID),
    markdown=True,
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")