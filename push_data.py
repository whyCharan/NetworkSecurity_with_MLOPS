import os 
import sys
import json

from dotenv import load_dotenv
load_dotenv()

mongo_db_url = os.getenv('MONGO_DB_URL')

import certifi #certifi used to verify the SSL certificate
ca = certifi.where()

import pandas as pd 
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkSecurityData:
    def __init__(self):
        try:
            pass 
        except Exception as e:
            raise NetworkSecurityException(e, sys) 
    
    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys) 

    def insert_data_mongodb(self,records,db_name,collection_name):
        try:
            self.db_name = db_name
            self.collection_name = collection_name
            self.records = records

            client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca) #tlsCAFile=ca is used to verify the SSL certificate
            db = client[self.db_name]

            collection = db[self.collection_name]
            collection.insert_many(records)

            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == '__main__':
    
    file_path = "./Network_Data/phisingData.csv"
    db_name = "sandakacharan"
    collection_name = "phisingData"
    Networkobj = NetworkSecurityData()
    records = Networkobj.csv_to_json_converter(file_path)
    no_of_records = Networkobj.insert_data_mongodb(records,db_name,collection_name)
    print(no_of_records)