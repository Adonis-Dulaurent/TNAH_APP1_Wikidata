# APP-1 : requests and parmeters road: 

Homework by Adonis Dulaurent, for Maxime Challon 

## goals : 

- verify knowledge of the structure of a simple Flask application.
- write a GET route with parameter(s).
- discover and learn how to use Python Requests Library.
- read documentation for exertern Python Library and extern API.

## Exercise : 

- Create a Flask road named 'retrive_wikidata' accepting an id parameter (a wikidata identifier)
- Use the requests library to query the Wikidata API and retrieve information about this identifier. To do this:
    - Specify query parameters to request a response in JSON format.
    - Decode the JSON content returned by the API.

- Return an HTML page using Jinja to display :
    -Response metadata (HTTP code, content type, etc.).
    -The entity's JSON data if available, or an error message if no data is found or the return contains an error.

## Instruction : 

- 1. Open your terminal. 

- 2. Install the latest version of python Python :
    - `sudo apt-get install python3`.
    - `sudo apt install python3-pip`.
      
- 3. Use a specific virtual environment for this project:
	-  `pip install virtualenv`.
	- `cd dossier_racine/`.
	- `virtualenv env -p python3`.
	-  `source env/bin/activate`.


- 4. Install external python libraries :
     
    - `pip install -r requirements.txt`.

- 5. Launch the application:*
     
    - `python3 run.py`.

- 6. Enjoy

- 7. Disable virtual environment :
     - `deactivate`.


