import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
mycollection = mydb["customer"]

def search(name):
    data = mycollection.find_one({"name": name})
    if data:
        return data
    else:
        return None
def display_messages(t, message):
    if t == "s":
        info = "operation was successful, " + message

    else:
        info = "operation not successful, " + message
    return info