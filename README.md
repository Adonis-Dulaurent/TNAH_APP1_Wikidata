# APP-1 : requests et les routes à paramètres

Exercice réalisé par Adonis Dulaurent, pour Maxime Challon 

## Objectif : 

- vérifier les acquis sur la structure d'une application Flask simple
- écrire une route GET à paramètre(s)
- découvrir et utiliser la librairie requests
- lire de la documentation (librairie externe, et API externe)

## Exercice : 

- Créer une route Flask nommée retrieve_wikidata acceptant un paramètre id (un identifiant Wikidata).
- Utiliser la bibliothèque requests pour interroger l’API de Wikidata et récupérer des informations sur cet identifiant. Pour cela :
    - Spécifier des paramètres de requête pour demander une réponse au format JSON.
    - Décoder le contenu JSON renvoyé par l’API.

- Retourner une page HTML utilisant Jinja pour afficher :
    -Les métadonnées de la réponse (code HTTP, type de contenu, etc.).
    -Les données JSON de l’entité si elles sont disponibles, ou un message d’erreur si aucune donnée n’est trouvée ou que le retour contient une erreur.