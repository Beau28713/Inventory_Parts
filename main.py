"""Allow users to load csv file containing data into a MongoDB database.
Allows users to search by part number, If part is in the database it is 
retuned else If part is not there user is then notified.
User can search, delete, modify, and addd new parts and their data
"""

import json
from pprint import pprint

import pandas as pd
import pymongo
import typer

from client import PARTS_COLL

app = typer.Typer()


@app.command()
def insert_csv_sheet(csv_sheet) -> None:
    """Insert data from a CSV file into a database

    Args:
        csv_sheet (CSV file, required): The CSV file used for data insertion
    """
    try:
        data = pd.read_csv(csv_sheet)
        data_insert = json.loads(data.to_json(orient="records"))
        PARTS_COLL.insert_many(data_insert)

    except FileNotFoundError as error:
        typer.echo(f"File not in directory\n {error}")


@app.command()
def find_part(part_number: str) -> None:
    """Find part by using its part number, if part is not in
    the database the user is notified.

    Args:
        query (str): Part number string used in the search
    """

    data = list(PARTS_COLL.find({"Part Number": part_number}))
    if data:
        pprint(data)

    else:
        typer.echo(f"{part_number} not in system")


@app.command()
def insert_part(
    part_number: str,
    bin: str,
    qty: str,
    supplier: str = "None",
    description: str = "None",
    specification: str = "None",
) -> None:
    """Insert new parts into the database

    Args:\n
        part_number (str, required): Part Number of part. Defaults to "None given".\n
        bin (str, required): Bin number you wish to put part in. Defaults to "None given".\n
        qty (str, required): Count of individual parts. Defaults to "None given".\n
        supplier (str, optional): Place you purchased part. Defaults to "None given".\n
        description (str, optional): Give a discription of part. Defaults to "None given".\n
        specification (str, optional): Any addition information. Defaults to "None given".\n
    """

    part = PARTS_COLL.find_one({"Part Number": part_number})
    if part:
        typer.echo(f"Part {part['Part Number']} is already in the sytem")

    else:
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
        typer.echo(f"Part number {part_number} has been added to database.")


@app.command()
def update_part(
    part_number: str,
    update_section: str,
    update_value: str,
) -> None:
    """Update parts in the database.

    Args:\n
        part_number (str): Part number you want to update\n
        update_section (str): Section you want to update. Enter one
    of the following (Part Number, Qty, Specifications, Supplier, Bin #, Description)\n
        update_value (str): Value you want to enter for the part section
    """

    part = PARTS_COLL.find_one_and_update(
        {"Part Number": part_number},
        {"$set": {update_section: update_value}},
        return_document=pymongo.collection.ReturnDocument.AFTER,
    )
    if part:
        typer.echo(f"{part_number} has been updated")
        pprint(part)
    else:
        typer.echo("Part not in system")


@app.command()
def delete_part(part_number_to_delete: str) -> None:
    """Delete a part from the database using the parts Part Number.

    Args:\n
        part_number_to_delete (str): Part number of the part you want to delete.
    """

    y = PARTS_COLL.find_one_and_delete({"Part Number": part_number_to_delete})
    if y:
        typer.echo(f"{part_number_to_delete} has been deleted")

    else:
        typer.echo("Part number not in system")


@app.command()
def del_doc_field(part_number: str, delete_field: str) -> None:
    """Delete a field inside a document in the database.

    Args:\n
        part_number (str, required): Part number of the part you wish to delete a field in.\n
        delete_field (str, required): Field you wish to delete.
    """
    part = PARTS_COLL.find_one_and_update(
        {"Part Number": part_number},
        {"$unset": {delete_field: ""}},
        return_document=pymongo.collection.ReturnDocument.AFTER,
    )
    if part:
        typer.echo("The new fields are:")
        pprint(part)

    else:
        print("Part not in database.")


@app.command()
def rename_field(update_field: str, new_field: str) -> None:
    """ "Rename a field inside a Collection document

    Args:\n
        update_field (str, required): Old field name.If fieled name has a space 
    you must surround the Field in '' Ex: Bin # -> 'Bin #'\n
        new_field (str, required): new field name
    """
    field_changed = PARTS_COLL.update_many({}, {"$rename": {update_field: new_field}})
    if field_changed.modified_count > 0:
        typer.echo(f"{update_field} has been changed")

    else:
        typer.echo(f"{update_field} not in documents.")


if __name__ == "__main__":
    app()
