## Description  
The application enables users to seamlessly load CSV files containing data into a MongoDB database. It offers a comprehensive set of functionalities for managing part numbers within the database.

Loading CSV Data: Users can effortlessly import data from CSV files into MongoDB.

Searching by Part Number: The system facilitates quick searches by part number. If the part is present in the database, its details are returned. Otherwise, users receive a notification indicating that the part is not found.

Search, Delete, Modify, and Add Parts: Users have the flexibility to perform various operations on parts and their associated data:

Search: Users can search for specific parts and retrieve their details.
Delete: Unwanted parts can be easily removed from the database.
Modify: Users can update the information associated with existing parts.
Add New Parts: Users can effortlessly add new parts along with their relevant data into the database.
This intuitive interface empowers users to efficiently manage their part number data, ensuring easy access, manipulation, and maintenance.

## How to use
### CLI Use
```shell
(parts_inventory) C:\Users\tech1\Code\Python\Inventory_Parts>python main.py --help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  del-doc-field     Delete a field inside a document in the database.
  delete-part       Delete a part from the database using the parts Part...
  find-part         Find part by using its part number, if part is not in...
  insert-csv-sheet  Insert data from a CSV file into a database
  insert-part       Insert new parts into the database
  rename-field      "Rename a field inside a Collection document
  update-part       Update parts in the database.
```
```shell
  (parts_inventory) C:\Users\tech1\Code\Python\Inventory_Parts>python main.py del-doc-field --help
Usage: main.py del-doc-field [OPTIONS] PART_NUMBER DELETE_FIELD

  Delete a field inside a document in the database.

  Args:

      part_number (str, required): Part number of the part you wish to delete
      a field in.

      delete_field (str, required): Field you wish to delete.

Arguments:
  PART_NUMBER   [required]
  DELETE_FIELD  [required]

Options:
  --help  Show this message and exit.
  ```
  ```shell
  (parts_inventory) C:\Users\tech1\Code\Python\Inventory_Parts>python main.py find-part --help
Usage: main.py find-part [OPTIONS] PART_NUMBER

  Find part by using its part number, if part is not in the database the user
  is notified.

  Args:     query (str): Part number string used in the search

Arguments:
  PART_NUMBER  [required]

Options:
  --help  Show this message and exit.
```
```shell
(parts_inventory) C:\Users\tech1\Code\Python\Inventory_Parts>python main.py find-part 8675309
[{'Bin': '1A',
  'Description': 'None',
  'Part Number': '8675309',
  'Qty': '7',
  'Specifications': 'None',
  'Supplier': 'None',
  '_id': ObjectId('62ade32d35ee6599b45d8f37')}]
```
### Gui Use
Comming Soon  
