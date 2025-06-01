from api_calls.transaction_handler import TransactionHandler
from database.crud import TransactionCRUD
from flask_code.flask_app import flask_main

def main():
    # Create and execute transaction with default prompt
    handler = TransactionHandler()
    success = handler.execute()
    if success:
        transaction = TransactionCRUD.get_transaction_values(handler.transaction_id)
        print(transaction)
        print(f"Transaction completed successfully!")
    else:
        print("Transaction failed to complete")

if __name__ == "__main__":
    # main()
    flask_main()
