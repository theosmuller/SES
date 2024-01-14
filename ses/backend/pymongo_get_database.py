
# import MongoClient
from pymongo import MongoClient

def get_database(): 

    # Creating a client
    client = MongoClient(port=27017)
    
    # Creating a database name GFG
    db = client['ses']
    
    print("Database is created !!")
  
    return db

if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
    