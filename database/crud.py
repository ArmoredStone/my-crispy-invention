from typing import List
from database.sqlalchemy_models import Transaction
from database.database import get_db_session
from config.static import get_transaction_dict

class TransactionCRUD:
    @staticmethod
    def create_transaction(author: str, prompt: str) -> str:
        """Create a new transaction."""
        with get_db_session() as session:
            transaction = Transaction(author=author, prompt=prompt)
            session.add(transaction)
            session.flush()
            return transaction.id
    
    @staticmethod
    def get_transaction_values(transaction_id: int) -> dict:
        """Get a transaction by ID."""
        with get_db_session() as session:
            transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()
            return get_transaction_dict(transaction)

    @staticmethod
    def get_all_transactions_values() -> List[Transaction]:
        """Get all transactions, ordered by ID in descending order (newest first)."""
        with get_db_session() as session:
            return [get_transaction_dict(transaction) for transaction in 
                   session.query(Transaction)
                   .order_by(Transaction.id.desc())
                   .all()]
    
    @staticmethod
    def get_all_transactions_values_by_page(page: int, page_size: int) -> List[Transaction]:
        """Get all transactions by page, ordered by ID in descending order (newest first)."""
        with get_db_session() as session:
            return [get_transaction_dict(transaction) for transaction in 
                   session.query(Transaction)
                   .order_by(Transaction.id.desc())
                   .offset((page - 1) * page_size)
                   .limit(page_size)]

    @staticmethod
    def get_transactions_values_by_author(author: str) -> List[Transaction]:
        """Get all transactions by a specific author, ordered by ID in descending order (newest first)."""
        with get_db_session() as session:
            return [get_transaction_dict(transaction) for transaction in 
                   session.query(Transaction)
                   .filter(Transaction.author == author)
                   .order_by(Transaction.id.desc())
                   .all()]
        
    @staticmethod
    def update_transaction(transaction_id: int, **kwargs) -> bool:
        """Update a transaction."""
        with get_db_session() as session:
            transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()
            if transaction:
                for key, value in kwargs.items():
                    if hasattr(transaction, key):
                        setattr(transaction, key, value)
                session.commit()
                return True
            return False

    @staticmethod
    def delete_transaction(transaction_id: int) -> bool:
        """Delete a transaction."""
        with get_db_session() as session:
            transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()
            if transaction:
                session.delete(transaction)
                session.commit()
                return True
            return False
    