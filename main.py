import os

from api_calls.call_grok import create_client, generate_image

from dotenv import load_dotenv
from openai import OpenAI

def load_api_key():
    load_dotenv()
    XAI_API_KEY = os.environ.get("XAI_API_KEY")
    return XAI_API_KEY

def main():
    client = create_client(load_api_key())
    response = generate_image(client)
    print(response)
    print(response.data[0].url)

if __name__=="__main__":
    main()
