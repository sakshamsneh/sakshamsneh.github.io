from pymongo import MongoClient
import pandas as pd
#client = MongoClient()
#db = client.ibm1
client= MongoClient("mongodb+srv://sakshamsneh:SAKsneh098#@ibm1-1tqxu.mongodb.net/test?retryWrites=true")
db = client.test
dataflow = db.dataflow
df = pd.read_csv("C:/Users/SAKSHIM/Documents/IBMProj/UNSW-NB15_4_1.csv")
records_ = df.to_dict(orient = 'records')
result = db.dataflow.insert_many(records_ )
print(db.dataflow.find().count())
