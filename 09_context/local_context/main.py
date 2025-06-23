from dataclasses import dataclass
from agents import Agent, Runner, RunContextWrapper, function_tool,  AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
import os
import asyncio
from dotenv import load_dotenv


load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set.")


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

@dataclass
class UserInfo:
    name : str
    uid : int
    location: str = "Pakistan"

@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:
    '''Returns the age of the user.'''
    return f"The Age of {wrapper.context.name} is 25."

@function_tool
async def fetch_user_location(wrapper: RunContextWrapper[UserInfo]) -> str:
    '''Returns the location of the user.'''
    return f"{wrapper.context.name} is from {wrapper.context.location}."

async def main():
    user_info = UserInfo(name= "Amraha A", uid=2301)


    agent = Agent(
        name = "Assistant",
        tools = [fetch_user_age, fetch_user_location],
        model = model
    )
    result = await Runner.run(
        agent,
        input = "And What is the name of the user?",
        context = user_info,
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())


# OUTPUT👇🏻

# The age of the user is 25 and he is from Pakistan

# I do not have access to the user's name. I can only access the user's age and location.
# BECAUSE OF THIS 👇🏻
# The context object is not sent to the LLM. It is purely a local object that you can read from,
# write to and call methods on it.