import os
from dotenv import load_dotenv 

def load_api_key():
    load_dotenv()
    XAI_API_KEY = os.environ.get("XAI_API_KEY")
    return XAI_API_KEY
