from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, handoff
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
url = os.getenv("BASE_URL")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = url,
)

model = OpenAIChatCompletionsModel(
    model = 'gemini-2.0-flash',
    openai_client = external_client,
)

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True,
)

urdu_agent = Agent(
    name= "Urdu Agent",
    instructions = "you only respond in Urdu",
)

english_agent = Agent(
    name= "English Agent",
    instructions= "you only respond in English",
)

triage_agent = Agent(
    name = "Triage Agent",
    instructions = "Handoff to the appropriate agent based on the language of the request.",
    handoffs = [urdu_agent, english_agent],
)

async def main(input: str):
    result = await Runner.run(triage_agent, input= input, run_config=config)

    print(result.final_output)

asyncio.run(main("hello! this is Amraha"))


# OUTPUT 👇🏻
# asyncio.run(main("السلام عليكم"))
# وعلیکم السلام! کیا حال ہے آپ کا؟ میں آپ کی کیا مدد کر سکتا ہوں؟

# asyncio.run(main("hello! this is Amraha"))
# Okay Amraha. How can I help you today?