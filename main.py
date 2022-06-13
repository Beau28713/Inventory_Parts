import pandas as pd
import pymongo
import json
from pprint import pprint

from client import CLIENT

MY_CLIENT = pymongo.MongoClient(CLIENT)
MYDB = MY_CLIENT["parts_database"]
PARTS_COLL = MYDB["parts"]

def insert_csv_sheet(csv_sheet):
    data = pd.read_csv(csv_sheet)
    data_insert = json.loads(data.to_json(orient="records"))
    PARTS_COLL.insert_many(data_insert)


def test_collection():

    collection_list = MYDB.list_collection_names()

    if "parts" in collection_list:
        print("Test passed", PARTS_COLL.estimated_document_count())

    else:
        print("Test failed")

def find_parts(query):

    data = list(PARTS_COLL.find(query))
    if len(data) > 0:
        for part in data:
            pprint(part)

    else:
        print("Part not in system")

def insert_part():
    PARTS_COLL.insert_one()# Finish this next!

def update_part(update_query, update_param, update_value):
    PARTS_COLL.update_one({"Part Number": update_query}, {"$set": {update_param: update_value}})
    print(f"{update_query} has been updated")

def main():
    # insert_csv_sheet("Parts_Inventory_List.csv")
    # test_collection()
    find_parts({"Part Number": "171-009-203L001"})
    # update_part("171-009-203L001", "Description", "9 Pin D-Sub F")
    # insert_part()

if __name__ == '__main__':
    main()