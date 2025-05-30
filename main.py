import os

from dotenv import load_dotenv
from openai import OpenAI

XAI_API_KEY = os.environ.get("XAI_API_KEY")
client = OpenAI(base_url="https://api.x.ai/v1", api_key=XAI_API_KEY)

response = client.images.generate(
  model="grok-2-image-1212",
  prompt="A cat in a tree"
)

print(response.data)
