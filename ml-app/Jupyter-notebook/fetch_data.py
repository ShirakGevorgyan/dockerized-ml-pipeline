import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

def fetch_data():
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")  
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")  
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")


    connection_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    try:

        engine = create_engine(connection_string)
        query = "SELECT * FROM gene_data;"
        df = pd.read_sql(query, con=engine)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

