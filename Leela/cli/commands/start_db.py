import os
import sys
from leela.config import config

# Service needs to be running ->
# postgresql-x64-14, if in stopped state, start it
def start_db():
    print()
    print("------- starting postgres -------")
    # /app_folder_location_of_postgresql_database_server/bin/pg_ctl 
    # -D /data_folder_location_of_postgresql_database_server operation_parameter
    # C:/Program Files/PostgreSQL/14/data
    os.system(f"pg_ctl start -D \"{config.POSTGRES_DIR}\"")