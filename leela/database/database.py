import pandas as pd
import numpy as np
from pathlib import Path
import psycopg
import os
import sys
from leela.config import config






# The steps below are a standard approach. The steps will vary according to specific requirements, and may require a more customised approach

# Step 1 - Identify current data directory path 

# SHOW data_directory;

# Step 2- Stop Postgresql services

# systemctl status  <service_name>

# systemctl stop <service_name>

# Step 3 - create a blank directory on the target path 

# e.g    mkdir /mydirectory/data

# --change ownership to the postgres user , for example

# chown  postgres:postgres /mypostgres/data

# Step 4 - Use initdb to create  creates a new PostgreSQL database cluster

# ./initdb -D /mydirectory/data

# The -D option specifies the directory where the database cluster should be stored

# initdb creates a new database cluster . The initdb command has a number of other switches to customise the setup. Check the documentation for extra details 

 

class Database:

    @staticmethod
    def test_method():
        # Note: the module name is psycopg, not psycopg3
        import psycopg

        # Connect to an existing database
        with psycopg.connect("dbname=test user=postgres") as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:

                # Execute a command: this creates a new table
                cur.execute("""
                    CREATE TABLE test (
                        id serial PRIMARY KEY,
                        num integer,
                        data text)
                    """)

                # Pass data to fill a query placeholders and let Psycopg perform
                # the correct conversion (no SQL injections!)
                cur.execute(
                    "INSERT INTO test (num, data) VALUES (%s, %s)",
                    (100, "abc'def"))

                # Query the database and obtain data as Python objects.
                cur.execute("SELECT * FROM test")
                cur.fetchone()
                # will return (1, 100, "abc'def")

                # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
                # of several records, or even iterate on the cursor
                for record in cur:
                    print(record)

                # Make the changes to the database persistent
                conn.commit()


    @staticmethod
    def start_server():
        print("---------- Starting Server ----------")
        os.system(f"pg_ctl start -D \"{config.POSTGRES_DIR}\"")


    @staticmethod
    def get_server_status():
        status = os.system(f"pg_ctl -D \"{config.POSTGRES_DIR}\" status")
        return status
        
    @staticmethod
    def build_database():
        print()
        print("Building Database...")
        print()

        command = f"""
            createdb {config.POSTGRES_DB_NAME} &
            type data/hpi_index_codes.txt | psql {config.POSTGRES_DB_NAME} -c "COPY hpi_indexes FROM stdin DELIMITER '|' NULL '';" &
            type data/interpolated_hpi_values.txt | psql {config.POSTGRES_DB_NAME} -c "COPY hpi_values FROM stdin DELIMITER '|' NULL '';" &
            type data/pmms.csv | psql {config.POSTGRES_DB_NAME} -c "COPY mortgage_rates FROM stdin NULL '' CSV HEADER;" &
            type data/msa_county_mapping.csv | psql {config.POSTGRES_DB_NAME} -c "COPY raw_msa_county_mappings FROM stdin NULL '' CSV HEADER;"
        """
        
        print(command)
        os.system(command)
        # os.system(f"cmd /k {command}")

        sql_statements = open(r"leela\database\sql\build_db.sql").read().split(';')
        
        with psycopg.connect(f"dbname={config.POSTGRES_DB_NAME} user={config.POSTGRES_USER}") as conn:
            with conn.cursor() as cur:
                print()
                print("-------- Executing SQL --------")
                print()
                
                for sql in sql_statements:
                    print(sql)
                    cur.execute(sql)

            conn.commit()


    @staticmethod
    def delete_database():
        sql_statements = open(r"leela\database\sql\delete_db.sql").read().split(';')
        
        with psycopg.connect(f"dbname={config.POSTGRES_DB_NAME} user={config.POSTGRES_LOGIN}") as conn:
            with conn.cursor() as cur:
                print()
                print("-------- Executing SQL --------")
                print()
                for sql in sql_statements:
                    print(sql.strip("\n"))
                    cur.execute(sql)
            conn.commit()

        print("Dropping Database.")
        os.system(f"dropdb {config.POSTGRES_DB_NAME}")

    @staticmethod
    def load_fannie_data():
        pass

    @staticmethod
    def load_freddie_data():
        pass

    @staticmethod
    def update_fannie_data():
        pass

    @staticmethod
    def update_freddie_data():
        pass