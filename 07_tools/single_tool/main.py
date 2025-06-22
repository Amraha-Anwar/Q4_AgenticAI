from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel ,function_tool, set_tracing_disabled
from dotenv import load_dotenv
import os
import requests

load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key =gemini_api_key,
    base_url ="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = 'gemini-2.0-flash',
    openai_client = provider,
)

@function_tool
def  get_weather(city: str) -> str:
    """
    get the weather of the given city
    """
    result = requests.get(f"http://api.weatherapi.com/v1/current.json?key=8e3aca2b91dc4342a1162608252604&q={city}")

    if result.status_code == 200:
        data = result.json()
        return f"The weather in {city} is {data['current']['temp_c']}°C with {data['current']['condition']['text']}."
    else:
        return f"Something went wrong :("

agent: Agent = Agent(
    name="Assistant",
    instructions=
    """
    If user asks for the weather of any city, use tool [get_weather] and tell him about the current weather, otherwise don't guess or add anything from your side.
    """,
    model=model,
    tools=[get_weather],
)

result = Runner.run_sync(
    agent,
    "what is the weather in Karachi?"
)
print(result.final_output)


# OUTPUT 👇🏻
# The weather in Karachi is 31.2°C with Mist.