import collections
from uniqlo.settings import *
import pymongo


def set_mongo_server():
    conn = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    print(conn)
    return conn[MONGODB_DBNAME]
