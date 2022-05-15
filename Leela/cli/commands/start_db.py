import os
import sys
from leela.config import config
import subprocess

# Service needs to be running ->
# postgresql-x64-14, if in stopped state, start it



def start_db():

    print()
    print("------- Starting Postgres Server -------")
    print()
    # /app_folder_location_of_postgresql_database_server/bin/pg_ctl 
    # -D /data_folder_location_of_postgresql_database_server operation_parameter
    # C:/Program Files/PostgreSQL/14/data

    # Check if service is running ->

    if os.name == "nt":
        # postgres_service_name = "postgresql-x64-14"
        os.system(f"pg_ctl start -D \"{config.POSTGRES_DIR}\"")
    else:
        print("Foo(): linux")
        pass