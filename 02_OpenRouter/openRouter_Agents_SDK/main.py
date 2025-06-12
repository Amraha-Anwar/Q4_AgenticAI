from dotenv import load_dotenv
import os
import json
import requests


load_dotenv() 

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL")
BASE_URL = os.getenv("BASE_URL")
URL = os.getenv("URL")

response = requests.post(
    url = f"{URL}/chat/completion",
    headers = {
        "Authorization" : f"Bearer {OPENROUTER_API_KEY}"
    },
    data = json.dumps({
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": "What is the National Language of Pakistan"
            }
        ]
    })
)

print(response.json()['choices'][0]['message']['content'])
