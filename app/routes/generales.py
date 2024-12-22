
from ..app import app
from flask import render_template
import requests

#road when you arrive on the websibe 
@app.route("/")
@app.route("/home")
def home ():
    return "Hello world but enter retrive_wikidata + id"

# Get road with parameters : 
@app.route("/retrive_wikidata/<id>")
def retrive_wikidata(id):
    """Function that uses Wikidata API to retrieve entity data in JSON format.

    Args:
        id (str): The ID of the wikidata entity to retrieve
        ex. Q42 = Douglas Adams

    Returns:
        Flask.reponse : A rendered HTML template (display_wikidata.html) with the following context variables:
        - id (str): the Wikidata entity ID.
        - status_codes (int): The htpp status code of the API reponse:
            - 200 if the request is succesful
            - 404 if the servers does not reponse.
        - content (str): The content type of the API reponse 
        - json (dict. or None) : The JSON data retrieved from wikidata, or None if the request failed. 
    """
    base_url ="https://www.wikidata.org/wiki/Special:EntityData"
    json = None
    try: 
        reponse = requests.get(f"{base_url}/{id}.json")
        status_codes = reponse.status_code
        content = reponse.headers.get("Content-type")

        if status_codes == 200  and content.startswith("application/json")==True:
            json = reponse.json()
    except Exception as e :
        print (f"Erreur lors de la reception des données {e}")

    return render_template(
        'display_wikidata.html',
        id=id,
        status_codes=status_codes,
        content=content,
        json=json
    )
