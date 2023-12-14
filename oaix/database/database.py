from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB = "sqlite:///./db.db"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


engine = create_engine(DB, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
