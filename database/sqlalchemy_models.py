from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String(255), nullable=False, default="Default Author")
    prompt = Column(Text, nullable=False, default="A cat in a tree")
    revised_prompt = Column(Text, nullable=False, default="")
    result_image_url = Column(String(500), nullable=False, default="")
    created_at = Column(String(30), default=datetime.now().__str__(), nullable=False)
