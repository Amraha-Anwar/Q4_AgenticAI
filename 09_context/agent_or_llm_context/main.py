from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, function_tool, RunContextWrapper, enable_verbose_stdout_logging
from dataclasses import dataclass
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()
enable_verbose_stdout_logging()

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
    name: str
    uid: int

@function_tool
async def greet_user(context: RunContextWrapper[UserInfo], greeting: str) -> str:
    '''Greets the user with their name.
    Args:
    greeting: A special greeting message for user.'''
    name = context.context.name
    return f"Hello {name}, {greeting}"


async def main():
    user_info = UserInfo(name=" Amraha A", uid=2301)

    agent = Agent[UserInfo](
        name="Assistant",
        tools = [greet_user],
        model= model,
        instructions = "Always greet the user using greet_user and welcome them to the event"
    )

    result = await Runner.run(
        agent,
        input="Hello",
        context = user_info,
    )

    print(result.final_output)

asyncio.run(main())


# Creating trace Agent workflow with id trace_9a23ae99ea114d76aaaf7adbc6026538
# Setting current trace: trace_9a23ae99ea114d76aaaf7adbc6026538
# Creating span <agents.tracing.span_data.AgentSpanData object at 0x000002A8E7EA2AD0> with id None
# Running agent Assistant (turn 1)
# Creating span <agents.tracing.span_data.GenerationSpanData object at 0x000002A8E7E8D010> with id None
# [
#   {
#     "content": "Always greet the user using greet_user and welcome them to the event",
#     "role": "system"
#   },
#   {
#     "role": "user",
#     "content": "Hello"
#   }
# ]
# Tools:
# [
#   {
#     "type": "function",
#     "function": {
#       "name": "greet_user",
#       "description": "Greets the user with their name.\nArgs:\ngreeting: A special greeting message for user.",
#       "parameters": {
#         "properties": {
#           "greeting": {
#             "title": "Greeting",
#             "type": "string"
#           }
#         },
#         "required": [
#           "greeting"
#         ],
#         "title": "greet_user_args",
#         "type": "object",
#         "additionalProperties": false
#       }
#     }
#   }
# ]
# Stream: False
# Tool choice: NOT_GIVEN
# Response format: NOT_GIVEN

# LLM resp:
# {
#   "content": null,
#   "refusal": null,
#   "role": "assistant",
#   "annotations": null,
#   "audio": null,
#   "function_call": null,
#   "tool_calls": [
#     {
#       "id": "",
#       "function": {
#         "arguments": "{\"greeting\":\"Welcome to the event!\"}",
#         "name": "greet_user"
#       },
#       "type": "function"
#     }
#   ]
# }

# Creating span <agents.tracing.span_data.FunctionSpanData object at 0x000002A8E82EB930> with id None
# Invoking tool greet_user with input {"greeting":"Welcome to the event!"}
# Tool call args: ['Welcome to the event!'], kwargs: {}
# Tool greet_user returned Hello  Amraha A, Welcome to the event!
# Running agent Assistant (turn 2)
# Creating span <agents.tracing.span_data.GenerationSpanData object at 0x000002A8E82F6390> with id None
# [
#   {
#     "content": "Always greet the user using greet_user and welcome them to the event",
#     "role": "system"
#   },
#   {
#     "role": "user",
#     "content": "Hello"
#   },
#   {
#     "role": "assistant",
#     "tool_calls": [
#       {
#         "id": "",
#         "type": "function",
#         "function": {
#           "name": "greet_user",
#           "arguments": "{\"greeting\":\"Welcome to the event!\"}"
#         }
#       }
#     ]
#   },
#   {
#     "role": "tool",
#     "tool_call_id": "",
#     "content": "Hello  Amraha A, Welcome to the event!"
#   }
# ]
# Tools:
# [
#   {
#     "type": "function",
#     "function": {
#       "name": "greet_user",
#       "description": "Greets the user with their name.\nArgs:\ngreeting: A special greeting message for user.",
#       "parameters": {
#         "properties": {
#           "greeting": {
#             "title": "Greeting",
#             "type": "string"
#           }
#         },
#         "required": [
#           "greeting"
#         ],
#         "title": "greet_user_args",
#         "type": "object",
#         "additionalProperties": false
#       }
#     }
#   }
# ]
# Stream: False
# Tool choice: NOT_GIVEN
# Response format: NOT_GIVEN

# LLM resp:
# {
#   "content": "Hello Amraha A, Welcome to the event!\n",
#   "refusal": null,
#   "role": "assistant",
#   "annotations": null,
#   "audio": null,
#   "function_call": null,
#   "tool_calls": null
# }

# Resetting current trace
# Hello Amraha A, Welcome to the event!

# Shutting down trace provider
# Shutting down trace processor <agents.tracing.processors.BatchTraceProcessor object at 0x000002A8E66AC3B0>
# OPENAI_API_KEY is not set, skipping trace export