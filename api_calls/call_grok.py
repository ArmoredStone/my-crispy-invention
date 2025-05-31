from openai import OpenAI

def create_client(XAI_API_KEY):
    return OpenAI(base_url="https://api.x.ai/v1", api_key=XAI_API_KEY)

def generate_image(client: OpenAI, prompt: str):
    return client.images.generate(model="grok-2-image-1212", prompt=prompt)
