from pymongo import MongoClient, errors

# global variables for MongoDB host (default port is 27017)
DOMAIN = '0.0.0.0'
PORT = 27017

try:
    client = MongoClient(
        host=[str(DOMAIN) + ":" + str(PORT)],
        serverSelectionTimeoutMS=3000
        #username = "root",
        #password = "toor"
    )

    database_names = client.list_database_names()
    database = client.get_database(name='stone')
    collections = database.collection_names(include_system_collections=False)

except errors.ServerSelectionTimeoutError as err:
    client = None
    database_names = []
    print("pymongo ERROR:", err)

print("Databases:", database_names)
print("Collections stone:", collections)

sel_collection = database.get_collection(name='initialCalls')
elements = sel_collection.find()
print("Number of lines:", elements.count())

