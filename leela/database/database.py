from pathlib import Path
from leela.config import config
import pandas as pd
import numpy as np
import os
import sys
import psycopg
from psycopg import Error
import pprint
from dateutil import parser

# import psycopg2 # from psycopg2 import Error

# The steps below are a standard approach. The steps will vary according to specific requirements, and may require a more customised approach
# Step 1 - Identify current data directory path 
# SHOW data_directory;
# Step 2- Stop Postgresql services
# systemctl status  <service_name>
# systemctl stop <service_name>
# Step 3 - create a blank directory on the target path 
# e.g mkdir /mydirectory/data
# --change ownership to the postgres user , for example
# chown  postgres:postgres /mypostgres/data
# Step 4 - Use initdb to create  creates a new PostgreSQL database cluster
# ./initdb -D /mydirectory/data
# The -D option specifies the directory where the database cluster should be stored
# initdb creates a new database cluster. 
# The initdb command has a number of other switches to customise the setup. Check the documentation for extra details 

# import psycopg2

# #establishing the connection
# conn = psycopg2.connect(
#    database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
# )
# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# #Executing an MYSQL function using the execute() method
# cursor.execute("select version()")

# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print("Connection established to: ",data)

# #Closing the connection
# conn.close()
# Connection established to: (
#    'PostgreSQL 11.5, compiled by Visual C++ build 1914, 64-bit',
# )

import psycopg2
class Database:

    @staticmethod
    def get_connection(DEBUG=False):
        print()
        print("-----------------------------")
        print("PostgreSQL server information")
        print("-----------------------------")
        
        connection = psycopg2.connect(user=config.POSTGRES_USER,
                                        password=config.POSTGRES_PW,
                                        host=config.POSTGRES_HOST,
                                        port=config.POSTGRES_PORT,
                                        database=config.POSTGRES_DB_NAME)
        
        if DEBUG:
            pprint.pprint(connection.get_dsn_parameters())
            print()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
        cursor.close()
        return connection

    @staticmethod
    def start_server():
        print("---------- Starting Server ----------")
        os.system(f"pg_ctl start -D \"{config.POSTGRES_DIR}\"")

    @staticmethod
    def get_server_status():
        status = os.system(f"pg_ctl -D \"{config.POSTGRES_DIR}\" status")
        return status

    @staticmethod
    def switch_database_connection():
        os.system(f"psql \c {config.POSTGRES_DB_NAME}")

    @staticmethod
    def build_database():
        print()
        print("Building Database...")
        print()

        # template command: COPY zip_codes FROM '/path/to/csv/ZIP_CODES.txt' WITH (FORMAT csv);
        # type data/hpi_index_codes.txt | psql agency-loan-level -c "COPY hpi_indexes FROM stdin DELIMITER '|' NULL '';"
        # C:\Projects\GitHub\Leela\data\hpi_index_codes.txt


        # COPY hpi_indexes FROM 'C:\Projects\GitHub\Leela\data\hpi_index_codes.txt' DELIMITER '|' NULL '';
        commands = [
            f"createdb {config.POSTGRES_DB_NAME}"
            # f"type data/hpi_index_codes.txt | psql {config.POSTGRES_DB_NAME} -c \"COPY hpi_indexes FROM stdin DELIMITER '|' NULL '';\"",
            # f"type data/interpolated_hpi_values.txt | psql {config.POSTGRES_DB_NAME} -c \"COPY hpi_values FROM stdin DELIMITER '|' NULL '';\""
            # f"type data/pmms.csv | psql {config.POSTGRES_DB_NAME} -c \"COPY mortgage_rates FROM stdin NULL '' CSV HEADER;\"",
            # f"type data/msa_county_mapping.csv | psql {config.POSTGRES_DB_NAME} -c \"COPY raw_msa_county_mappings FROM stdin NULL '' CSV HEADER;\""
        ]

        for command in commands:
            print(command)
            os.system(command)

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
        
        # No need to drop db, just wipe tables...
        # print("Dropping Database.")
        # os.system(f"dropdb {config.POSTGRES_DB_NAME}")

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

    @staticmethod
    def get_raw_data(start_date, end_date=None, filter=None, ascending=False, DEBUG=False, limit=None):
        # connection = psycopg.connect(config.POSTGRES_DB_NAME)
        # connection.row_factory = psycopg.Row

        if ascending:
            date_order_sql = "asc"
        else:
            date_order_sql = "desc"

        # "where monthly_reporting_period > = {start_date}"""
        # select count(*) from fannie_processed where monthly_reporting_period >= '2021-03-01';
        # 108,166,456
        # select count(*) fannie_processed where monthly_reporting_period >= '2021-03-01'  and original_interest_rate is between 2.5 and 4.5 desc;
        # select count(*) from fannie_processed where monthly_reporting_period >= '2021-03-01' and original_interest_rate >= 2.5 and original_interest_rate <= 4.5;"
        # 92,868,179
        sql = f"""select * from fannie_processed where monthly_reporting_period >= '{start_date}' """
        # 201-225k
        # 176-200k
        # 151-175k
        # 111-150k HLB
        # 86-110k MLB
        # 0-85k LLB

        if filter is not None:
            sql += " and " + filter

        sql += f" order by monthly_reporting_period {date_order_sql}"
        
        if limit is not None:
            sql += f" limit {limit}"
        
        if DEBUG:
            print(sql)

        res = pd.read_sql_query(sql, Database.get_connection())
        # res["timestamp"] = pd.to_datetime(res["timestamp"])
        # res = res.set_index(["symbol", "timestamp"])
        return res

    @staticmethod
    def get_model_input(start, end=None, my_filter=None, scaled=False, DEBUG=False, limit=None):
        df = Database.get_raw_data(start, end, my_filter, DEBUG=DEBUG, limit=limit)
        
        # ------------------------- # 
        # Add Additional Features ->
        # ------------------------- #



        return df

    @staticmethod
    def query_db(sql):
        res = pd.read_sql_query(sql, Database.get_connection())
        return res
