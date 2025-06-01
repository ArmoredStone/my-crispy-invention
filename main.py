from api_calls.transaction_handler import TransactionHandler
from database.crud import TransactionCRUD
from flask_code.wsgi import flask_main

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
    app = flask_main()
    app.run(debug=True, host='0.0.0.0', port=5000)
