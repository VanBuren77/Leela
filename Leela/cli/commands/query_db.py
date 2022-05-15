import os
import sys
from leela.config import config

def query_db():
    print("------- querying db -------")
    os.system(f"psql -d {config.POSTGRES_DB_NAME}")
    # psql -d agency-loan-level