import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import numbers
cred = credentials.Certificate("computersciencediddly-firebase-adminsdk-apdja-ed7c3b9cd8.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://computersciencediddly-default-rtdb.europe-west1.firebasedatabase.app'})
ref = db.reference('/')


df = pd.read_csv('Meteorites Cleaned.csv')

data_dict = df.to_dict()

print(data_dict)

for name,data in data_dict.items():
    ref.update({name:data})
    
print("\nDataframe has been updated. Refresh Firebase if it's open in Firefox.")