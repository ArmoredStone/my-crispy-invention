from flask import Blueprint, jsonify, render_template_string, request, abort
from database.crud import TransactionCRUD
from flask_code.templates import TRANSACTIONS_TEMPLATE, CREATE_TRANSACTION_TEMPLATE
from database.database import get_db_session
from database.sqlalchemy_models import Transaction
from api_calls.transaction_handler import TransactionHandler
import json

routes = Blueprint('routes', __name__)

@routes.route('/list')
def list_route():
    """Render all transactions in a paged table format"""
    # Validate and set page parameters with reasonable limits
    try:
        page = request.args.get('page', 1, type=int)
        if page < 1:
            page = 1
    except ValueError:
        page = 1

    # Define allowed page sizes and validate
    allowed_page_sizes = [10, 25, 50, 100]
    try:
        page_size = request.args.get('page_size', 10, type=int)
        if page_size not in allowed_page_sizes:
            page_size = 10
    except ValueError:
        page_size = 10

    # Get total count for pagination
    with get_db_session() as session:
        total_transactions = session.query(Transaction).count()
    
    transactions = TransactionCRUD.get_all_transactions_values_by_page(page=page, page_size=page_size)
    total_pages = (total_transactions + page_size - 1) // page_size

    # If page is greater than total pages, redirect to last page
    if page > total_pages and total_pages > 0:
        abort(404)
    
    return render_template_string(
        TRANSACTIONS_TEMPLATE,
        transactions=transactions,
        current_page=page,
        total_pages=total_pages,
        page_size=page_size,
        allowed_page_sizes=allowed_page_sizes
    )

@routes.route('/create')
def create_route():
    """Render the create transaction page"""
    return render_template_string(CREATE_TRANSACTION_TEMPLATE)

@routes.route('/api/create_transaction', methods=['POST'])
def create_transaction():
    """API endpoint to create a new transaction"""
    data = request.json
    
    prompt = data['prompt'].strip()
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    author = data['author'].strip()
    if not author:
        return jsonify({"error": "Author is required"}), 400
    
    transaction_handler = TransactionHandler(author=author, prompt=prompt)
    success = transaction_handler.execute()
    if success:
        transaction = TransactionCRUD.get_transaction_values(transaction_handler.transaction_id)
        print(transaction)
        print(f"Transaction completed successfully!")
    else:
        print("Transaction failed to complete")
    return jsonify(transaction)
