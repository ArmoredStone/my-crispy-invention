import os
from database.sqlalchemy_models import Transaction

def load_api_key():
    XAI_API_KEY = os.environ.get("XAI_API_KEY")
    return XAI_API_KEY

def get_transaction_dict(transaction: Transaction) -> dict:
        return {
            'id': transaction.id,
            'author': transaction.author,
            'prompt': transaction.prompt,
            'revised_prompt': transaction.revised_prompt,
            'result_image_url': transaction.result_image_url,
            'created_at': transaction.created_at
            }