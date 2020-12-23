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
    collections = database.list_collection_names(
        include_system_collections=False)

    print("Databases:", database_names)
    print("Collections stone:", collections)

    sel_collection = database.get_collection(name='initialCalls')
    elements = sel_collection.find()
    print("Number of lines:", elements.count())
    sel_collection = database.get_collection(name='initialStock')
    elements = sel_collection.find()
    print("Number of lines:", elements.count())

except errors.ServerSelectionTimeoutError as err:
    client = None
    database_names = []
    print("pymongo ERROR:", err)

