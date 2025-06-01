from api_calls.call_grok import create_client, generate_image
from config.static import load_api_key
from database.crud import TransactionCRUD

class TransactionHandler:
    def __init__(self, prompt: str = "A cat in a tree", author: str = "Default Author"):
        # Create transaction using TransactionCRUD
        self.prompt = prompt
        self.transaction_id = TransactionCRUD.create_transaction(author=author, prompt=prompt)
    
    def execute(self) -> bool:
        """Execute the transaction by making API call and saving to database"""
        try:
            # Create API client and make the call
            client = create_client(load_api_key())
            response = generate_image(client, self.prompt)
            
            # Update transaction with response using TransactionCRUD
            updated_transaction = TransactionCRUD.update_transaction(
                self.transaction_id,
                result_image_url=response.data[0].url,
                revised_prompt=response.data[0].revised_prompt
            )
            if updated_transaction:
                self.transaction = updated_transaction
                return True
            return False
            
        except Exception as e:
            print(f"Error executing transaction: {str(e)}")
            return False

    def __repr__(self):
        return "Associated with transaction:"+str(self.transaction_id)
    
    def __str__(self):
        return "Assiociated with transaction:"+str(self.transaction_id)
