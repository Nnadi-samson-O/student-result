import pymongo
from pprint import pprint

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
db = myclient['mydatabase']
mycol = db["customers"]

patient_record ={
    "NAME": "mod",
    "AGE": 29,
    "GENDER": "male",
    "BLOOD PRSSURE":[{"SYS":156},{"dia": 78}],
    "Heart rate": 87
}

mycol.insert_one(patient_record)

for item in mycol.find():
    pprint(item)