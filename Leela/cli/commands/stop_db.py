


import os

def stop_db():
    if os.name == 'windows':
        os.system('cmd /c pg_ctl')