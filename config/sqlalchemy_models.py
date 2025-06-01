from sqlalchemy import Column, Integer, String, Text, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from datetime import datetime
from typing import Optional

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String(255), nullable=False, default="Default Author")
    prompt = Column(Text, nullable=False, prompt="A cat in a tree")
    revised_prompt = Column(Text, nullable=False)
    result_image_url = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    
