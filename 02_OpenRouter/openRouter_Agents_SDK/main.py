from dotenv import load_dotenv, find_dotenv
import os
import json
import requests


load_dotenv(find_dotenv()) 

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL")
BASE_URL = os.getenv("BASE_URL")
URL = os.getenv("URL")

response = requests.post(
    url = f"{URL}/chat/completions",
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


# OUTPUT 👇🏻
# The **national language of Pakistan** is **Urdu**.  

# However, **Pakistan recognizes multiple official languages**, including:  
# - **Urdu** (National language and lingua franca)  
# - **English** (Official and widely used in government, education, and business)  

# Additionally, several **regional languages** are spoken across Pakistan, such as:  
# - Punjabi  
# - Sindhi  
# - Pashto  
# - Balochi  
# - Saraiki
# - And others

# While Urdu serves as the national symbol of unity, different provinces often use their native languages in daily communication.