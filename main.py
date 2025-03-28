# main.py
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configuration (using .env or JSON)
config_list = [
    {
        "model": "gpt-4",
        "api_key": os.getenv("OPENAI_API_KEY"),  # From .env
    }
]
# Alternative: Load from JSON
# config_list = config_list_from_json("OAI_CONFIG_LIST.json")

# Create Assistant Agent
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
    system_message="You are a helpful AI assistant.",
)

# Create User Proxy Agent
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="ALWAYS",  # Change to "NEVER" for full automation
    code_execution_config={"work_dir": "coding"},
)

# Initiate chat
user_proxy.initiate_chat(
    assistant,
    message="Write a Python script to calculate prime numbers.",
)
