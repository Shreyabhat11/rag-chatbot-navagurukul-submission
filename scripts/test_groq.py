# test_groq.py

from groq import Groq
from config import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Hello"
        }
    ]
)

print(
    response.choices[0].message.content
)