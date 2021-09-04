# Python program shows the
# connection management
# for MongoDB

# resource - https://www.geeksforgeeks.org/context-manager-in-python/

from pymongo import MongoClient

class MongoDBConnectionManager():
    def __init__(self, conn_string):
        self.conn_string = conn_string
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.conn_string)
        return self.connection

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()

# connecting with a localhost
# with MongoDBConnectionManager('mongodb://localhost:27017/') as mongo:
#     collection = mongo.connection.SampleDb.test
#     data = collection.find({'_id': 1})
#     print(data.get('name'))
