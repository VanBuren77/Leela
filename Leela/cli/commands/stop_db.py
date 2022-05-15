

from leela.config import config
import os

def stop_db():
    os.system(f"pg_ctl stop -D \"{config.POSTGRES_DIR}\"")