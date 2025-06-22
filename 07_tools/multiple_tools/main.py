from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool, set_tracing_disabled
import os
import random
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(disabled = True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = 'gemini-2.0-flash',
    openai_client = provider,
)

@function_tool
def how_many_jokes():
    """
    choose random number and generate that number of jokes
    """
    return random.randint(1,5)

@function_tool
def greet():
    """greet back the user"""
    return f"Hello! How have you been?"

agent = Agent(
    name= "Helpful Assistant",
    instructions = """
    if the user ask for the jokes use [how_many_jokes] tool, choose random number and tell the number with jokes.
    fif the user greets you, use tool [greet] and greet him back.
    """,
    model=model,
    tools = [how_many_jokes, greet]
)
result = Runner.run_sync(
    agent,
    "Lighten my mood",
)

print(result.final_output)


# OUTPUT👇🏻
# I will tell you 5 jokes to lighten your mood:


# Why don't scientists trust atoms?
# Because they make up everything!

# Why did the scarecrow win an award?
# Because he was outstanding in his field!

# What do you call a fish with no eye?
# Fsh!

# Why did the bicycle fall over?
# Because it was two tired!

# What do you call a bear with no teeth?
# A gummy bear!
