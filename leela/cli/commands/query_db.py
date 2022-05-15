import os
import sys
from leela.config import config

def query_db():
    print()
    print("------- Querying DB -------")
    print()
    # psql -d agency-loan-level
    # interactive shell:
    os.system(f"psql -d {config.POSTGRES_DB_NAME}")