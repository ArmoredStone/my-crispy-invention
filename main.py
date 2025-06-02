from api_calls.transaction_handler import TransactionHandler
from database.crud import TransactionCRUD
from flask_code.wsgi import flask_main
from config.request_wrapper import make_post_request
import threading
import time

def make_request(thread_id):
    data = {
        "author": f"thread_{thread_id}",
        "prompt": f"usachman"
    }
    try:
        response = make_post_request(url="http://localhost:8000/api/create_transaction", data=data)
        print(f"Thread {thread_id} - Response: {response.json()}")
    except Exception as e:
        print(f"Thread {thread_id} - Error: {str(e)}")

def main():
    # Create a list to store thread objects
    threads = []
    
    # Create and start 10 threads
    for i in range(10):
        thread = threading.Thread(target=make_request, args=(i,))
        threads.append(thread)
        thread.start()
        print(f"Started thread {i}")
        time.sleep(2)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    print("All threads have completed")

if __name__ == "__main__":
    main()
