
from ..app import app
from flask import render_template
import requests


@app.route("/")
@app.route("/home")
def home ():
    return "Hello world but enter retrive_wikidata + id"

# Route get avec paramètres : 
@app.route("/retrive_wikidata/<id>")
def retrive_wikidata(id):
    """ 
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
