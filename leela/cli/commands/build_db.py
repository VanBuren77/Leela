


from leela.database.database import Database

def build_db():
    # delete then build -> ?
    status = Database.get_server_status()
    
    if status == 3:
        print()
        print(f"Database Not Running: {status}")
        print()
        Database.start_server()
    
    Database.build_database()