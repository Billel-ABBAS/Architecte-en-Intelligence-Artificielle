# Importation des bibliothèques nécessaires
import argparse  # Pour analyser les arguments de la ligne de commande
import sys  # Pour gérer les opérations système
from confluent_kafka import avro, KafkaError  # Pour interagir avec Apache Kafka et gérer les erreurs Kafka
from confluent_kafka.admin import AdminClient, NewTopic  # Pour administrer des topics Kafka
from uuid import uuid4  # Pour générer des identifiants uniques

# Définition du schéma Avro pour les clés Kafka
name_schema = """
    {
        "namespace": "io.confluent.examples.clients.cloud",
        "name": "Name",
        "type": "record",
        "fields": [
            {"name": "name", "type": "string"}
        ]
    }
"""

# Classe représentant un enregistrement de clé Kafka
class Name(object):
    """
        La classe Name stocke les enregistrements Avro désérialisés pour la clé Kafka.
    """

    # Utilisation de __slots__ pour déclarer explicitement les membres de données
    __slots__ = ["name", "id"]

    def __init__(self, name=None):
        self.name = name  # Le champ 'name' de l'enregistrement
        self.id = uuid4()  # Génère un identifiant unique pour le suivi des requêtes

    @staticmethod
    def dict_to_name(obj, ctx):
        # Convertit un dictionnaire en instance de la classe Name
        return Name(obj['name'])

    @staticmethod
    def name_to_dict(name, ctx):
        # Convertit une instance Name en dictionnaire
        return Name.to_dict(name)

    def to_dict(self):
        """
            Représente la classe sous forme de dictionnaire pour la sérialisation Avro.
        """
        return dict(name=self.name)

# Définition du schéma Avro pour les valeurs Kafka
count_schema = """
    {
        "namespace": "io.confluent.examples.clients.cloud",
        "name": "Count",
        "type": "record",
        "fields": [
            {"name": "count", "type": "int"}
        ]
    }
"""

# Classe représentant un enregistrement de valeur Kafka
class Count(object):
    """
        La classe Count stocke les enregistrements Avro désérialisés pour la valeur Kafka.
    """

    # Utilisation de __slots__ pour déclarer explicitement les membres de données
    __slots__ = ["count", "id"]

    def __init__(self, count=None):
        self.count = count  # Le champ 'count' de l'enregistrement
        self.id = uuid4()  # Génère un identifiant unique pour le suivi des requêtes

    @staticmethod
    def dict_to_count(obj, ctx):
        # Convertit un dictionnaire en instance de la classe Count
        return Count(obj['count'])

    @staticmethod
    def count_to_dict(count, ctx):
        # Convertit une instance Count en dictionnaire
        return Count.to_dict(count)

    def to_dict(self):
        """
            Représente la classe sous forme de dictionnaire pour la sérialisation Avro.
        """
        return dict(count=self.count)

# Fonction pour analyser les arguments en ligne de commande
def parse_args():
    """Analyse les arguments de la ligne de commande"""
    parser = argparse.ArgumentParser(
             description="Exemple de client Python Confluent pour produire des messages vers Confluent Cloud")
    parser._action_groups.pop()
    required = parser.add_argument_group('arguments requis')
    required.add_argument('-f',
                          dest="config_file",
                          help="chemin vers le fichier de configuration Confluent Cloud",
                          required=True)
    required.add_argument('-t',
                          dest="topic",
                          help="nom du topic",
                          required=True)
    args = parser.parse_args()
    return args

# Fonction pour lire le fichier de configuration Confluent Cloud
def read_ccloud_config(config_file):
    """Lire la configuration Confluent Cloud pour les clients librdkafka"""
    conf = {}
    with open(config_file) as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                conf[parameter] = value.strip()
    return conf

# Fonction pour supprimer les paramètres liés au registre de schémas du dictionnaire de configuration
def pop_schema_registry_params_from_config(conf):
    """Supprime les configurations liées au registre de schémas du dictionnaire"""
    conf.pop('schema.registry.url', None)
    conf.pop('basic.auth.user.info', None)
    conf.pop('basic.auth.credentials.source', None)
    return conf

# Fonction pour créer un topic Kafka
def create_topic(conf, topic):
    """
        Crée un topic si nécessaire.
        Exemple de fonctionnalités supplémentaires de l'API Admin :
        https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/adminapi.py
    """
    admin_client_conf = pop_schema_registry_params_from_config(conf.copy())
    a = AdminClient(admin_client_conf)

    fs = a.create_topics([NewTopic(
         topic,
         num_partitions=1,  # Nombre de partitions pour le topic
         replication_factor=3  # Facteur de réplication pour le topic
    )])
    for topic, f in fs.items():
        try:
            f.result()  # Le résultat est None si tout va bien
            print("Topic {} créé".format(topic))
        except Exception as e:
            # Continuer si l'erreur est TOPIC_ALREADY_EXISTS, sinon échouer rapidement
            if e.args[0].code() != KafkaError.TOPIC_ALREADY_EXISTS:
                print("Échec de la création du topic {}: {}".format(topic, e))
                sys.exit(1)