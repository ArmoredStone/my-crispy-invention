# crud.py
from typing import List, Optional
from sqlalchemy.orm import Session

class TransactionCRUD:
    @staticmethod
    def create_transaction(author: str, prompt: str) -> Transaction:
        """Create a new transaction."""
        with get_db_session() as session:
            transaction = Transaction(author=author, prompt=prompt)
            session.add(transaction)
            session.flush()  # To get the ID
            session.refresh(transaction)
            return transaction
    
    @staticmethod
    def get_transaction(transaction_id: int) -> Optional[Transaction]:
        """Get a transaction by ID."""
        with get_db_session() as session:
            return session.query(Transaction).filter(Transaction.id == transaction_id).first()
    
    @staticmethod
    def get_transactions_by_author(author: str) -> List[Transaction]:
        """Get all transactions by a specific author."""
        with get_db_session() as session:
            return session.query(Transaction).filter(Transaction.author == author).all()
    
    @staticmethod
    def get_all_transactions() -> List[Transaction]:
        """Get all transactions."""
        with get_db_session() as session:
            return session.query(Transaction).all()
    
    @staticmethod
    def update_transaction(transaction_id: int, **kwargs) -> Optional[Transaction]:
        """Update a transaction."""
        with get_db_session() as session:
            transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()
            if transaction:
                for key, value in kwargs.items():
                    if hasattr(transaction, key):
                        setattr(transaction, key, value)
                session.refresh(transaction)
                return transaction
            return None
    
    @staticmethod
    def delete_transaction(transaction_id: int) -> bool:
        """Delete a transaction."""
        with get_db_session() as session:
            transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()
            if transaction:
                session.delete(transaction)
                return True
            return False
    
    @staticmethod
    def get_incomplete_transactions() -> List[Transaction]:
        """Get transactions that are not complete."""
        with get_db_session() as session:
            return session.query(Transaction).filter(
                (Transaction.revised_prompt == '') | 
                (Transaction.result_image_url == '')
            ).all()
