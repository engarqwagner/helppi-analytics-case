from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    f"mysql+mysqlconnector://{os.getenv('MYSQL_USER')}:"
    f"{os.getenv('MYSQL_PASSWORD')}@"
    f"{os.getenv('MYSQL_HOST')}/"
    f"{os.getenv('MYSQL_DB')}"
)

with engine.connect() as conn:
    result = conn.execute(text("SHOW TABLES;"))
    print(result.fetchall())
