import pandas as pd
import numpy as np
from os import stat
import socket
# import win32serviceutil
# import servicemanager
# import win32event
# import win32service

class Utils:
    
    @staticmethod
    def foo():
        pass


    @staticmethod
    # def SQL_INSERT_STATEMENT_FROM_DATAFRAME(SOURCE, TARGET):
    def sql_insert_statement_from_df(SOURCE: pd.DataFrame, TARGET: str):
        sql_texts = []
        for index, row in SOURCE.iterrows():       
            sql_texts.append('INSERT INTO '+TARGET+' ('+ str(', '.join(SOURCE.columns))+ ') VALUES '+ str(tuple(row.values)))        
        return sql_texts