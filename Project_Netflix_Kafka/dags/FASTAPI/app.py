# Importation des bibliothèques nécessaires
import uvicorn  # Pour démarrer le serveur FastAPI
from fastapi import FastAPI  # Pour créer l'application FastAPI
from fastapi import HTTPException  # Pour gérer les exceptions HTTP
import joblib  # Pour charger des modèles sauvegardés au format pickle
import pandas as pd  # Pour manipuler les données sous forme de DataFrame
from io import BytesIO  # Pour la gestion des flux de données en mémoire

# Description de l'API (sera affichée dans la documentation interactive)
description = """
Cette API Netflix vous permet de faire des recommandations de films pour un utilisateur donné.

## Fonctionnalités disponibles

* `/suggested_movies` : Obtenez les meilleures suggestions de films pour un utilisateur donné.
"""

# Métadonnées pour la documentation de l'API
tags_metadata = [
    {
        "name": "Prédictions",
        "description": "Utilisez cet endpoint pour obtenir des prédictions"
    }
]

# Création de l'application FastAPI avec des informations supplémentaires
app = FastAPI(
    title="👨‍💼 API_Netflix_Reco",  # Titre affiché dans la documentation
    description=description,  # Description de l'API
    version="0.1",  # Version actuelle de l'API
    openapi_tags=tags_metadata  # Métadonnées pour les tags
)

# Chargement du modèle de prédiction sauvegardé
model = joblib.load('../dags/FASTAPI/model/model.pkl')  # Charger le modèle à partir du chemin indiqué

# Définition de l'endpoint racine (`/`)
@app.get("/")
async def index():
    """
    Endpoint par défaut qui affiche un message de bienvenue.
    """
    message = "Bonjour tout le monde ! Ce point d'accès (`/`) est le plus simple et par défaut. Pour en savoir plus, consultez la documentation de l'API à `/docs`."
    return message  # Retourne un message de bienvenue

# Endpoint pour obtenir les suggestions de films
@app.get("/suggested_movies")
async def look_prediction(Cust_Id):
    """
    Retourne les 10 meilleurs films recommandés pour un utilisateur donné.
    """
    # Chargement des données de recommandation depuis un fichier CSV
    df = pd.read_csv("../dags/FASTAPI/data/data_reco.csv", index_col=0)
    
    # Calcul de l'estimation des scores pour chaque film en utilisant le modèle
    df['Estimate_Score'] = df['Movie_Id'].apply(lambda x: model.predict(int(Cust_Id), x).est)
    
    # Tri des films par score estimé (du plus élevé au plus faible)
    df = df.sort_values('Estimate_Score', ascending=False)
    
    # Sélection des 10 meilleurs films
    best_movie = df.head(10)
    
    # Retourne les résultats sous forme de dictionnaire
    return best_movie.to_dict()

# Exécution de l'application FastAPI
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)  # Définition du serveur web pour exécuter l'application `app`
    # `host="0.0.0.0"` permet à l'application d'être accessible depuis n'importe quelle adresse IP.
    # `port=4000` indique le port sur lequel le serveur écoute les requêtes.
