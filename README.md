## Description  
Allow users to load csv file containing data into a MongoDB database.  
Allows users to search by part number, If part is in the database it is retuned else If part is not there user is then notified.  
User can search, delete, modify, and add new parts and their data  

## How to use
### CLI Use
```
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
```
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
  ```
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
```
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

## Requirements
See also the requirements file  
Python 3.9+   
pandas==1.4.2  
pymongo==3.12.0  
typer==0.4.1  
 
