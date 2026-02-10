from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.os import AgentOS
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=OpenRouter(id="nvidia/nemotron-3-nano-30b-a3b:free"),
    instructions="You are a helpful assistant. All your responses must be brief and concise.",
)

agent.print_response("What healthy dinner can I have today?", stream=True)

# Create the AgentOS
agent_os = AgentOS(agents=[agent])
# Get the FastAPI app for the AgentOS
app = agent_os.get_app()