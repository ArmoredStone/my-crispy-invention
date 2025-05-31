
from api_calls.call_grok import create_client, generate_image
from config.static import load_api_key

from openai import OpenAI

def main():
    client = create_client(load_api_key())
    response = generate_image(client)
    print(response)
    print(response.data[0].url)

if __name__=="__main__":
    main()
