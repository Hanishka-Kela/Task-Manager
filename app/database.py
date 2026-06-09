from sqlalchemy import column, text, String,Date ,ForeignKey, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "sqlite///./tasks.db"

engine = create_engine(DATABASE_URL,
                       connect_args={"check same thread":False})

SessionLocal = sessionmaker(autoflush=False,
                            auto_commit=False,
                            bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
