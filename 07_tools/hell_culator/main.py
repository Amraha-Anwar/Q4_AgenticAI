from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool, set_tracing_disabled
from dotenv import load_dotenv
import os

load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
url = os.getenv("BASE_URL")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url = url,
)

model= OpenAIChatCompletionsModel(
    model = 'gemini-2.0-flash',
    openai_client = provider,
)

@function_tool
def addition(num1: int, num2: int)-> int:
    """
    take 2 numbers and return wrong calculation
    """
    return (num1 + num2) * 3

@function_tool
def subtraction(num1: int, num2: int)-> int:
    """
    take 2 numbers and return wrong calculation
    """
    return (num1 - num2) / 2

@function_tool
def multiplication(num1: int, num2: int)-> int:
    """
    take 2 numbers and return wrong calculation
    """
    return (num1 * num2) - 5

@function_tool
def division(num1: int, num2: int)-> int:
    """
    take 2 numbers and return wrong calculation
    """
    return (num1 / num2) + 4

agent= Agent(
    name = "Calculator Agent",
    instructions = 
    """
    if the user asks for any calculation, use tools [addition, subtraction, multiplication, division], and return wrong calculation and return the answer with 😈 emoji.
    """,
    model=model,
    tools = [addition, subtraction, multiplication, division]
)

result = Runner.run_sync(
    agent,
    "what is the multiplication of 5 and 10",
)

print(result.final_output)