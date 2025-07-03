from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, handoff, RunContextWrapper
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

def on_handoff(agent: Agent, ctx: RunContextWrapper[None]):
    agent_name = agent.name
    print(f"\n\t\tHanding off to {agent_name}...\n")

triage_agent = Agent(
    name = "Triage Agent",
    instructions = "Handoff to the appropriate agent based on the language of the request.",
    handoffs = [
        handoff(urdu_agent, on_handoff = lambda ctx: on_handoff(urdu_agent, ctx)),
        handoff(english_agent, on_handoff = lambda ctx: on_handoff(english_agent, ctx))
    ]
)

async def main(input: str):
    result = await Runner.run(
        triage_agent,
        input = input,
        run_config = config
    )

    print(result.final_output)

asyncio.run(main("!السلام عليكم"))
asyncio.run(main("Hello! How are you doing?"))



# OUTPUT 👇🏻

#            Handing off to Urdu Agent...

# وعلیکم السلام! کیا حال ہے؟ میں آپ کی کیا مدد کر سکتا ہوں؟


#            Handing off to English Agent...

# I'm doing well, thank you for asking! How can I help you today?