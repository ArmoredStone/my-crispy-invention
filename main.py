
from api_calls.call_grok import create_client, generate_image
from config.static import load_api_key
from config.models import Transaction

from openai import OpenAI

def main():
    #Create transaction object
    transaction = Transaction()

    #Process the prompt to API call
    client = create_client(load_api_key())
    response = generate_image(client, transaction.prompt)

    #Update transaction object
    transaction.update_result_image_url(response.data[0].url)
    transaction.update_revised_prompt(response.data[0].revised_prompt)
    print(transaction.is_complete())
    print(transaction.__repr__())

if __name__=="__main__":
    main()
