from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from dotenv import load_dotenv
import os
import chainlit as cl
from agents.run import RunConfig
from typing import cast

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI API KEY is not found. Check your .env file")

@cl.on_chat_start
async def start():
    external_client = AsyncOpenAI(
        api_key = gemini_api_key,
        base_url ="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(
        model = "gemini-2.0-flash",
        openai_client = external_client
    )

    config = RunConfig(
        model = model,
        model_provider = external_client,
        tracing_disabled=True
    )

    # setting up an empty chat history

    cl.user_session.set("chat_history", [])
    cl.user_session.set("config", config)

    agent = Agent(
        name = "Assistant Agent",
        instructions = "you are a playfull Assistant Agent who is good at humor.",
        model = model
    )
    cl.user_session.set("agent", agent)

    await cl.Message(
        content = "Welcome to the Amraha's developed Agent who is god at humor.").send()
    
@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content = "thinking...")
    await msg.send()

    agent : Agent = cast(Agent, cl.user_session.get("agent"))
    config : RunConfig = cast(RunConfig, cl.user_session.get("config"))

    history = cl.user_session.get("chat_history") or []

    history.append({"role": "user", "content": message.content})

    try:
        print("\n[CALLING AGENT WITH CONTEXT]", history, "\n")
        result = Runner.run_sync(starting_agent = agent, input = history, run_config = config)
        response_content = result.final_output

        msg.content = response_content
        await msg.update()

        cl.user_session.set("chat_history", result.to_input_list())

        print(f"User: {message.content}")
        print(f"Assistant: {response_content}")

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")
