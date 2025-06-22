from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, Runner, set_tracing_disabled
from dotenv import load_dotenv
# from pydantic import BaseModel
import asyncio
import os

load_dotenv()
set_tracing_disabled(True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
url = os.getenv("BASE_URL")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = url,
)

model = OpenAIChatCompletionsModel(
    model = 'gemini-2.0-flash',
    openai_client = external_client,
)

spanish_agent = Agent(
    name= "Spanish Agent",
    instructions = "You translate the user's message to Spanish",
    handoff_description = "An English to Spanish Translator",
    model=model
)

turkish_agent = Agent(
    name= "Turkish Agent",
    instructions = "You translated user's message to Turkish.",
    handoff_description = "An English to Turkish Translator.",
    model=model
)

urdu_agent = Agent(
    name= "Urdu Agent",
    instructions = "You translated user's message to Urdu.",
    handoff_description = "An English to Urdu Translator.",
    model=model
)

italian_agent = Agent(
    name= "Italian Agent",
    instructions = "You translated user's message to Italian.",
    handoff_description = "An English to Italian Translator.",
    model=model
)

orchestrator_agent = Agent(
    name= "Orchestrator Agent",
    instructions =(
        "You are a translator Agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant toold in order."
        "You never translate on your own, you always use the provided tools."
    ),
    tools = [
        spanish_agent.as_tool(
            tool_name = "Translate_to_spanish",
            tool_description = "Translate the user's message to Spanish.",
        ),
        turkish_agent.as_tool(
            tool_name = "Translate_to_turkish",
            tool_description = "Translate the user's message to Turkish.",
        ),
        urdu_agent.as_tool(
            tool_name = "Translate_to_urdu",
            tool_description = "Translate the user's message to Urdu.",
        ),
        italian_agent.as_tool(
            tool_name = "Translate_to_italian",
            tool_description = "Translate the user's message to Italian.",
        ),
    ],
    model=model
)

async def main():
    msg = input("Hello! What would you like translated, and to which languages? ")
    orchestrator_result = await Runner.run(orchestrator_agent, msg)
    print(f'\n\nFinal Response:\n{orchestrator_result.final_output}')


if __name__ == "__main__":
    asyncio.run(main())


# OUTPUT 👇🏻
# 1.  Hello! What would you like translated, and to which languages? translate 'hello! I am Amraha' into turkish

# Final Response:
# Merhaba! Ben Amraha.

# 2.  Hello! What would you like translated, and to which languages? translate 'hello! I am Amraha' into italian

# Final Response:
# Ciao! Sono Amraha.

# 3.  Hello! What would you like translated, and to which languages? translate 'hello! I am Amraha' into spanish

# Final Response:
# ¡Hola! Soy Amraha.

# 4.  Hello! What would you like translated, and to which languages? translate 'hello! I am Amraha' into urdu   


# Final Response:
# ہیلو! میں امرحہ ہوں۔

# 🩷 NOTE:  This Agent is the only one who wrote my name correctly in urdu even humans couldn't🩷