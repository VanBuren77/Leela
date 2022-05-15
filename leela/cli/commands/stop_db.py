

from leela.config import config
import os

def stop_db():
    print()
    print("------- Stopping Postgres Server -------")
    print()
    os.system(f"pg_ctl stop -D \"{config.POSTGRES_DIR}\"")