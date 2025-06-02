from flask import Blueprint, jsonify, render_template_string
from database.crud import TransactionCRUD
from flask_code.templates import TRANSACTIONS_TEMPLATE

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    """Render all transactions in a paged table format"""
    transactions = TransactionCRUD.get_all_transactions_values()[::-1]
    # transactions = TransactionCRUD.get_all_transactions_values_by_page(page=1, page_size=10)[::-1]
    return render_template_string(TRANSACTIONS_TEMPLATE, transactions=transactions)

@routes.route('/api/transactions')
def get_transactions():
    """API endpoint to get all transactions as JSON"""
    transactions = TransactionCRUD.get_all_transactions_values()
    return jsonify(transactions)

@routes.route('/api/transactions/<int:transaction_id>')
def get_transaction(transaction_id):
    """API endpoint to get a specific transaction by ID"""
    transaction = TransactionCRUD.get_transaction_values(transaction_id)
    if transaction:
        return jsonify(transaction)
    return jsonify({"error": "Transaction not found"}), 404

@routes.route('/api/transactions/author/<author>')
def get_transactions_by_author(author):
    """API endpoint to get transactions by author"""
    transactions = TransactionCRUD.get_transactions_values_by_author(author)
    return jsonify(transactions)