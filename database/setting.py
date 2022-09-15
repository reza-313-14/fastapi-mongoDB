from pymongo import MongoClient


# your mongoDB URI
mongodb_uri = 'localhost'
# port
port = 27017


clinet = MongoClient(mongodb_uri, port)
db = clinet['blog']