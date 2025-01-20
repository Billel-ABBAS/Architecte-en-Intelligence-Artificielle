# Importation des bibliothèques nécessaires
from confluent_kafka import Producer  # Pour produire des messages vers Kafka
import requests  # Pour effectuer des requêtes HTTP
import pandas as pd  # Pour manipuler les données sous forme de DataFrame
import ccloud_lib  # Bibliothèque personnalisée pour les configurations Confluent Cloud
import time  # Pour gérer les délais et les timings
import datetime  # Pour manipuler les dates et heures

# Initialisation des configurations à partir du fichier "python.config"
CONF = ccloud_lib.read_ccloud_config("../dags/kafka_netflix/python.config")  # Lecture des configurations Kafka
TOPIC = "netflix_recommendation"  # Nom du topic Kafka

# Création d'une instance de Producteur Kafka
producer_conf = ccloud_lib.pop_schema_registry_params_from_config(CONF)  # Suppression des paramètres liés au registre de schémas
producer = Producer(producer_conf)  # Initialisation du producteur Kafka

# Création du topic Kafka s'il n'existe pas déjà
ccloud_lib.create_topic(CONF, TOPIC)

# Compteur de messages livrés
delivered_records = 0

# Fonction pour récupérer les données de l'API
def movie_api_get():
    """
    Cette fonction envoie une requête GET à l'API.
    Elle traite la réponse de l'API pour produire un DataFrame Pandas.
    Retourne le DataFrame sous forme de dictionnaire.
    """
    url = 'https://jedha-netflix-real-time-api.herokuapp.com/users-currently-watching-movie'
    response = requests.get(url).json()  # Récupération des données au format JSON
    df = pd.read_json(response, orient='split').reset_index().rename(columns={'index': 'Movie_Id'})  # Conversion en DataFrame
    return df

# Fonction de rappel appelée `acked` (déclenchée par poll() ou flush())
# Elle est appelée lorsque le message a été livré avec succès ou a échoué définitivement
def acked(err, msg):
    global delivered_records
    if err is not None:
        print("Échec de la livraison du message : {}".format(err))  # Message non livré
    else:
        delivered_records += 1  # Incrémentation du compteur de messages livrés
        print("Message produit dans le topic {} partition [{}] @ offset {}"
              .format(msg.topic(), msg.partition(), msg.offset()))  # Confirmation de livraison

# Boucle principale pour produire des messages
try:
    while True:
        # Récupération des données depuis l'API
        data = movie_api_get()
        user_id = data["customerID"][0]  # Extraction de l'ID utilisateur
        current_time = data['current_time'][0]  # Extraction de l'heure actuelle
        print(f"Production d'un message - heure : {current_time}\tuserID : {user_id}")
        
        # Conversion des données en JSON pour l'envoyer à Kafka
        record_value = data.to_json()
        
        # Envoi des données au topic Kafka
        producer.produce(
            TOPIC,
            key=f"netflix_{user_id}",  # Clé unique basée sur l'ID utilisateur
            value=record_value,  # Valeur contenant les données
            on_delivery=acked  # Fonction de rappel pour gérer les rapports de livraison
        )
        
        # Appel à poll() pour traiter les rapports de livraison grâce à `acked`
        producer.poll(0)
        
        # Pause de 20 secondes avant d'envoyer le prochain message
        time.sleep(20)
        
# Gestion de l'interruption clavier (Ctrl+C)
except KeyboardInterrupt:
    pass
finally:
    # Vidage des messages en attente avant d'arrêter complètement le producteur
    producer.flush()