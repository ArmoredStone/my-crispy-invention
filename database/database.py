from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from database.sqlalchemy_models import Base

# Database URL - adjust according to your database
DATABASE_URL = "sqlite:///config/transactions.db"  # For SQLite
# DATABASE_URL = "postgresql://user:password@localhost/dbname"  # For PostgreSQL
# DATABASE_URL = "mysql+pymysql://user:password@localhost/dbname"  # For MySQL

engine = create_engine(DATABASE_URL, echo=False)  # echo=True for SQL logging
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Context manager for database sessions
@contextmanager
def get_db_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
