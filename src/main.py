# import the MongoClient class
from pymongo import MongoClient, errors

# global variables for MongoDB host (default port is 27017)
#DOMAIN = '0.0.0.0'
DOMAIN = 'mongodb'
PORT = 27017

# use a try-except indentation to catch MongoClient() errors
try:
    # try to instantiate a client instance
    client = MongoClient(
        host=[str(DOMAIN) + ":" + str(PORT)],
        serverSelectionTimeoutMS=3000
        #username = "root",
        #password = "toor"
    )

    # print the version of MongoDB server if connection successful
    print("server version:", client.server_info()["version"])

    # get the database_names from the MongoClient()
    database_names = client.list_database_names()
    database = client.get_database(name='stone')
    collections = database.collection_names(include_system_collections=False)

except errors.ServerSelectionTimeoutError as err:
    # set the client and DB name list to 'None' and `[]` if exception
    client = None
    database_names = []

    # catch pymongo.errors.ServerSelectionTimeoutError
    print("pymongo ERROR:", err)

print("\ndatabases:", database_names)
print("\ncollections mydb:", collections)

sel_collection = database.get_collection(name='initialCalls')
elements = sel_collection.find()
print("number of lines:", elements.count())















