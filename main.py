"""Docstring will go here"""

import json

import pandas as pd
import pymongo
from pprint import pprint

from client import PARTS_COLL


def insert_csv_sheet(csv_sheet) -> None:
    """Docstring will go here"""

    data = pd.read_csv(csv_sheet)
    data_insert = json.loads(data.to_json(orient="records"))
    PARTS_COLL.insert_many(data_insert)


def find_parts(query: dict) -> None:
    """Docstring will go here"""

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
) -> None:
    """Docstring will go here"""

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


def update_part(update_query: str, update_param: str, update_value: str) -> None:
    """Docstring will go here"""

    y = PARTS_COLL.find_one_and_update(
        {"Part Number": update_query},
        {"$set": {update_param: update_value}},
        return_document=pymongo.collection.ReturnDocument.AFTER,
    )
    print(f"{update_query} has been updated")
    pprint(y)


def delete_part(delete_quary: str) -> None:
    """Docstring will go here"""

    y = PARTS_COLL.find_one_and_delete({"Part Number": delete_quary})
    print(f"{delete_quary} has been deleted")
    pprint(y)


def main():
    # insert_csv_sheet("Parts_Inventory_List.csv")
    # find_parts({"Part Number": "171-009-203L001"})
    # update_part("171-009-203L001", "Description", "9 Pin D-Sub Femail type")
    # insert_part("8675309", "1A", "3", "For a good time", "Jenny", "Stacy's Mom")
    delete_part("8675309")


if __name__ == "__main__":
    main()
