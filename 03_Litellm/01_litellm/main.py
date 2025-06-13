from dotenv import load_dotenv
import os
from agents.extensions.models.litellm_model import LitellmModel
from agents import Agent, Runner, function_tool

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("MODEL")

@function_tool
def get_weather(city:str) -> str:
    return f"The Weather of {city} is Hot."

def main(api_key: str, model: str):
    agent = Agent(
        name = "Assistant Agent",
        instructions = "You only respond in Haikus.",
        model = LitellmModel(api_key = api_key, model = model),
)

    result = Runner.run_sync(agent, "What is the weather in Karachi?")
    print(result.final_output)

main(model = MODEL, api_key = GEMINI_API_KEY)


# OUTPUT 👇🏻
# Warm breeze whispers soft,
# Sunlight on the sandy shore,
# Heat hangs in the air.