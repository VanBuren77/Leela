import pandas as pd
import numpy as np
from pathlib import Path
import psycopg
import os
import sys
from leela.config import config

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
    def build_database():
        
        os.system(f"""
                cmd /k 
                "
                    createdb agency-loan-level passwd={config.POSTGRES_PW} & 
                    type data/hpi_index_codes.txt | psql agency-loan-level -c "COPY hpi_indexes FROM stdin DELIMITER '|' NULL '';" &
                    type data/interpolated_hpi_values.txt | psql agency-loan-level -c "COPY hpi_values FROM stdin DELIMITER '|' NULL '';" &
                    type data/pmms.csv | psql agency-loan-level -c "COPY mortgage_rates FROM stdin NULL '' CSV HEADER;" &
                    type data/msa_county_mapping.csv | psql agency-loan-level -c "COPY raw_msa_county_mappings FROM stdin NULL '' CSV HEADER;" &
                "
        """)

        sql_statements = open(r"leela\database\sql\build_db.sql").read().split(';')
        
        with psycopg.connect(f"dbname={config.POSTGRES_DB_NAME} user={config.POSTGRES_USER}") as conn:
            with conn.cursor() as cur:
                
                for sql in sql_statements:
                    print("-------- Executing SQL --------")
                    print(sql)
                    cur.execute(sql)

            conn.commit()


    @staticmethod
    def delete_database():
        sql_statements = open(r"leela\database\sql\delete_db.sql").read().split(';')
        
        with psycopg.connect("dbname=test user=postgres") as conn:
            with conn.cursor() as cur:

                for sql in sql_statements:
                    print("-------- Executing SQL --------")
                    print(sql)
                    cur.execute(sql)
            conn.commit()

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