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
        postgres_service_name = "postgresql-x64-14"

        status = os.system(f"systemctl is-active --quiet {postgres_service_name}")
        # will return 0 for active else inactive.
        print(f"Service Status: {status}")

        if status != 0:
            # command = f"pg_ctl.ex start -N {postgres_service_name} -D \"C:\Program Files\PostgreSQL\9.5\data\" -w"
            command = f"net start {postgres_service_name}"
            p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
            p.communicate("")
            # subprocess.call(['runas', '/user:Administrator', 'net start {postgres_service_name}'])
            # os.system(f"net start {postgres_service_name}")
        
        # "C:/Program Files/PostgreSQL/14/data"
        # os.system(f"pg_ctl start -D \"{config.POSTGRES_DIR}\"")
    else:
        print("Foo(): linux")
        pass