from agents import Agent, Runner, function_tool
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import find_dotenv, get_key
import requests

GEMINI_API_KEY = get_key(find_dotenv(), "GOOGLE_API_KEY")

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
    name="hello",
    instructions="You are a helpful assistant.",
    model=LitellmModel(model="gemini/gemini-2.0-flash",api_key=GEMINI_API_KEY),
    tools=[getWeather],
)

def run(message:str)->str:
    print("Run message",message)
    result=Runner.run_sync(
        agent,
        f"{message}?",  
    )
    return result.final_output
