from dotenv import load_dotenv
import os
from openai import OpenAI

class LLMClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("MODEL_NAME")
        self.client = OpenAI(api_key=self.api_key)

    def generate(self,prompt):
        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )
        return response.output_text