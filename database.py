from pymongo import MongoClient

try:
    client = MongoClient('mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23')
    print("Connected to database")
except Exception as e:
    print(e.args)    

db = client['interns_b2_23']
lib = db['priyanka_db'] 


