import os

def load_api_key():
    XAI_API_KEY = os.environ.get("XAI_API_KEY")
    return XAI_API_KEY
