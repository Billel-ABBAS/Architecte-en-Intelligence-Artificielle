# Importation des bibliothèques nécessaires
from confluent_kafka import Consumer  # Pour consommer les messages depuis Kafka
import json  # Pour manipuler les données JSON
import ccloud_lib  # Bibliothèque personnalisée pour les configurations Confluent Cloud
import time  # Pour gérer les délais et les timings
import pandas as pd  # Pour manipuler les données sous forme de DataFrame
import psycopg2  # Pour interagir avec une base de données PostgreSQL
from sqlalchemy import create_engine  # Pour gérer les connexions à la base de données
import requests  # Pour effectuer des requêtes HTTP

# Configuration de Kafka
CONF = ccloud_lib.read_ccloud_config("../dags/kafka_netflix/python.config")  # Lecture de la configuration Kafka
TOPIC = "netflix_recommendation"  # Nom du topic Kafka à consommer
consumer_conf = ccloud_lib.pop_schema_registry_params_from_config(CONF)  # Suppression des paramètres liés au registre de schémas
consumer_conf['group.id'] = 'netflix_prediction'  # Identifiant du groupe de consommateurs
consumer_conf['auto.offset.reset'] = 'latest'  # Définir le point de départ pour consommer les messages
consumer = Consumer(consumer_conf)  # Initialisation du consommateur Kafka
consumer.subscribe([TOPIC])  # Abonnement au topic spécifié

# Fonction pour obtenir des recommandations pour un utilisateur donné
def predict(user_id):
    """
    Effectue une requête HTTP à l'API FastAPI locale pour obtenir les recommandations
    basées sur l'ID utilisateur.
    """
    prediction = requests.get(f'http://localhost:4000/suggested_movies?Cust_Id={user_id}').json()
    return prediction

# Boucle principale pour consommer les messages Kafka
try:
    while True:
        msg = consumer.poll(1.0)  # Récupération des messages avec un délai d'attente de 1 seconde
        if msg is None:  # Aucun message reçu
            print("En attente de messages ou d'événements/erreurs dans poll()")
            continue
        elif msg.error():  # Gestion des erreurs
            print(f'erreur : {msg.error()}')
        else:
            print("Traitement du message...")
            record_key = msg.key()  # Clé du message Kafka
            record_value = msg.value().decode('utf-8')  # Valeur du message Kafka décodée
            print("Chargement du JSON...")
            record_value_df = pd.read_json(record_value)  # Conversion en DataFrame Pandas
            print(f"Valeur reçue = {record_value}")
            
            # Traitement des films que l'utilisateur est actuellement en train de regarder
            user_curr_watching = record_value_df.copy()
            
            # Extraction de l'ID utilisateur
            user_id = user_curr_watching['customerID'][0]
            
            # Obtenir les meilleurs films recommandés pour cet utilisateur
            best_movie = pd.DataFrame(predict(user_id))
            best_movie['Cust_id'] = user_id  # Ajouter l'ID utilisateur aux recommandations
            print(best_movie)
            
            # Spécification de la base de données PostgreSQL et des identifiants
            engine = create_engine(
                'postgresql+psycopg2://ntkaybccubsmpt:c006bee3e63118363c9dbe825f8f3f5e26a62f026aec335dbfea5ebb922325fd@ec2-63-34-69-123.eu-west-1.compute.amazonaws.com:5432/dbvuj6r9nah6ju',
                echo=False
            )

            # Utilisation de la fonction Pandas `to_sql()` pour insérer les données du DataFrame dans la base de données
            best_movie.to_sql('top_movies', engine, if_exists='append', index=False)  # Ajout des données à la table `top_movies`

# Gestion des interruptions clavier (Ctrl+C)
except KeyboardInterrupt:
    pass
finally:
    # Fermeture propre du consommateur Kafka
    consumer.close()