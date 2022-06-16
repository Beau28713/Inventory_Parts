"""Docstring will go here"""

import json

import pandas as pd
import pymongo
import typer
from pprint import pprint

from client import PARTS_COLL

app = typer.Typer()


@app.command()
def insert_csv_sheet(csv_sheet) -> None:
    """_summary_

    Args:
        csv_sheet (_type_): _description_
    """

    data = pd.read_csv(csv_sheet)
    data_insert = json.loads(data.to_json(orient="records"))
    PARTS_COLL.insert_many(data_insert)


@app.command()
def find_parts(query: str) -> None:
    """_summary_

    Args:
        query (str): _description_
    """

    data = list(PARTS_COLL.find({"Part Number": query}))
    if len(data) > 0:
        for part in data:
            pprint(part)

    else:
        print("Part not in system")


@app.command()
def insert_part(
    part_number: str = "None given",
    bin: str = "None given",
    qty: str = "None given",
    supplier: str = "None given",
    description: str = "None given",
    specification: str = "None given",
) -> None:
    """Insert new parts into the database

    Args:\n
        part_number (str, optional): Part Number of part. Defaults to "None given".\n
        bin (str, optional): Bin number you wish to put part in. Defaults to "None given".\n
        qty (str, optional): Count of individual parts. Defaults to "None given".\n
        supplier (str, optional): Place you purchased part. Defaults to "None given".\n
        description (str, optional): Give a discription of part. Defaults to "None given".\n
        specification (str, optional): Any addition information. Defaults to "None given".\n
    """

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


@app.command()
def update_part(update_query: str, update_param: str, update_value: str) -> None:
    """Update parts in the database.

    Args:\n
        update_query (str): Part number you want to update\n
        update_param (str): Section you want to update\n
        update_value (str): Value you want to enter for the part section
    """

    y = PARTS_COLL.find_one_and_update(
        {"Part Number": update_query},
        {"$set": {update_param: update_value}},
        return_document=pymongo.collection.ReturnDocument.AFTER,
    )
    print(f"{update_query} has been updated")
    pprint(y)


@app.command()
def delete_part(delete_quary: str) -> None:
    """Delete a part from the database using the parts Part Number.

    Args:
        delete_quary (str): Part number of the part you want to delete.
    """

    y = PARTS_COLL.find_one_and_delete({"Part Number": delete_quary})
    print(f"{delete_quary} has been deleted")
    pprint(y)


# def main():
# insert_csv_sheet("Parts_Inventory_List.csv")
# find_parts({"Part Number": "171-009-203L001"})
# update_part("171-009-203L001", "Description", "9 Pin D-Sub Femail type")
# insert_part("8675309", "1A", "3", "For a good time", "Jenny", "Stacy's Mom")
# delete_part("8675309")


if __name__ == "__main__":
    app()
