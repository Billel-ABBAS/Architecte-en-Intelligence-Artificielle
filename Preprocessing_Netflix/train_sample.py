# Importation des bibliothèques nécessaires
import pandas as pd  # Pour manipuler les données sous forme de DataFrame
import numpy as np  # Pour les calculs numériques
from surprise import Reader, Dataset, SVD  # Pour créer et entraîner le modèle de recommandation
from surprise.model_selection import GridSearchCV  # Pour la recherche des meilleurs hyperparamètres
import joblib  # Pour sauvegarder et charger le modèle

# Chargement des données
df = pd.read_csv('data/data_cleaned_sample.csv')  # Charger les données nettoyées à partir du fichier CSV

# Initialisation du Reader pour Surprise
reader = Reader()  # Permet de convertir les données en un format utilisable par Surprise

# Chargement des données dans un format compatible avec Surprise
data = Dataset.load_from_df(df[['Cust_Id', 'Movie_Id', 'Rating']], reader)

# Définition de la grille des hyperparamètres à tester pour le modèle SVD
param_grid = {
    "n_epochs": [5, 10],  # Nombre d'époques (itérations d'entraînement)
    "lr_all": [0.002, 0.005],  # Taux d'apprentissage global
    "reg_all": [0.4, 0.6],  # Régularisation pour éviter le surapprentissage
    "n_factors": [50, 100]  # Nombre de facteurs latents
}

# Recherche des meilleurs hyperparamètres à l'aide de GridSearchCV
gs = GridSearchCV(SVD, param_grid, measures=["rmse", "mae"], cv=5)  # Validation croisée sur 5 sous-ensembles
gs.fit(data)  # Entraînement sur l'ensemble des combinaisons d'hyperparamètres

# Affichage des meilleurs scores
print("Meilleur score RMSE :", gs.best_score["rmse"])  # Score d'erreur quadratique moyenne
print("Meilleur score MAE :", gs.best_score["mae"])  # Score d'erreur absolue moyenne

# Affichage des meilleurs paramètres pour RMSE
print("Meilleurs paramètres pour RMSE :", gs.best_params["rmse"])

# Affichage des meilleurs paramètres pour MAE
print("Meilleurs paramètres pour MAE :", gs.best_params["mae"])

# Entraînement du modèle avec les meilleurs paramètres pour RMSE
best_params_rmse = gs.best_params["rmse"]  # Récupération des meilleurs paramètres pour RMSE
model = SVD(**best_params_rmse)  # Initialisation du modèle avec ces paramètres
trainset = data.build_full_trainset()  # Conversion des données en un ensemble d'entraînement complet
model.fit(trainset)  # Entraînement du modèle

# Sauvegarde du modèle dans un fichier
model_file = "model/model_sample.pkl"  # Chemin du fichier de sauvegarde
joblib.dump(model, model_file, compress=True)  # Sauvegarde du modèle compressé
