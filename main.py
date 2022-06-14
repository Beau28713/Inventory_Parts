import pandas as pd
import json
from pprint import pprint

from client import MYDB, PARTS_COLL


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


def find_parts(query: dict):

    data = list(PARTS_COLL.find(query))
    if len(data) > 0:
        for part in data:
            pprint(part)

    else:
        print("Part not in system")


def insert_part(
    part_number: str = "None given",
    bin: str = "None given",
    qty: str = "None given",
    supplier: str = "None given",
    description: str = "None given",
    specification: str = "None given",
):
    PARTS_COLL.insert_one(
        {
            "Bin #": bin,
            "Description": description,
            "Part Number": part_number,
            "Qty": qty,
            "Specifications": specification,
            "Supplier": supplier,
        }
    )


def update_part(update_query: str, update_param: str, update_value: str):
    PARTS_COLL.update_one(
        {"Part Number": update_query}, {"$set": {update_param: update_value}}
    )
    print(f"{update_query} has been updated")


def main():
    # insert_csv_sheet("Parts_Inventory_List.csv")
    # test_collection()
    # find_parts({"Part Number": "171-009-203L001"})
    # update_part("171-009-203L001", "Description", "9 Pin D-Sub F")
    insert_part("8675309", "1A", "3", "For a good time", "Jenny", "Stacy's Mom")


if __name__ == "__main__":
    main()
