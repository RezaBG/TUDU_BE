from sqlalchemy import text
from src.services.database import SessionLocal


def test_connection():
    session = SessionLocal()
    try:
        result = session.execute(text("SELECT 1"))
        print(result.fetchone())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()

test_connection()
