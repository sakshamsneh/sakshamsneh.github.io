from pymongo import MongoClient
import pandas as pd
#Offline db:
#client = MongoClient()
#db = client.ibm1
filename=""
client= MongoClient("mongodb+srv://sakshamsneh:SAKsneh098#@ibm1-1tqxu.mongodb.net/test?retryWrites=true")
db = client.test
dataflow = db.dataflow
df = pd.read_csv(filename)
records_ = df.to_dict(orient = 'records')
result = db.dataflow.insert_many(records_ )
print(db.dataflow.find().count())
