from groq import Groq

from config import settings


class GroqLLM:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

        self.model = "llama-3.3-70b-versatile"

    def generate(
        self,
        prompt
    ):

        response = self.client.chat.completions.create(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,

            max_tokens=1500
        )

        return (
            response
            .choices[0]
            .message
            .content
        )