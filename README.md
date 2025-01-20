# Architecte en Intelligence Artificielle
## ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/f17d64a9-3922-4cee-87dc-9b881085659c) Moteur de recommandation Netflix ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/f17d64a9-3922-4cee-87dc-9b881085659c)
![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/2f002cd8-a41b-4e93-a357-b8eba4d86e69)

Ce dépôt contient toutes les ressources liées à la présentation du projet sur le moteur de recommandation Netflix.

## Ressources disponibles :

- Le diaporama de présentation est accessible dans le fichier nommé **Présentation_Certification_Architecte_en_Intelligence_Artificielle.pptx**.  
- Des ressources supplémentaires, y compris le modèle et les données d’entraînement, sont disponibles ici : [Google Drive](https://drive.google.com/drive/folders/14qz8C2JKb7AuaLz6VbQjgEoHbhNFNw5S?usp=drive_link).  
- Le sujet du projet est accessible ici : [Jedha Final Projects](https://app.jedha.co/course/final-projects-l/netflix-automation-engine-l).  

Une description des dossiers et des objectifs de chaque répertoire est fournie ci-dessous.  
Pour toute question ou information complémentaire, contactez le propriétaire du dépôt : **Billel ABBAS** (billel_abbas@yahoo.fr).

---

## Prétraitement des données et Entraînement du modèle :  
Ce dossier, nommé **Preprocessing_Netflix**, contient :  
- **data_preprocessing.ipynb** : Un script qui intègre les données provenant de Kaggle et construit l’ensemble de données d’entraînement pour le modèle de recommandation.  
- Les données brutes sont disponibles ici : [Kaggle Netflix Dataset](https://www.kaggle.com/code/laowingkin/netflix-movie-recommendation).  

Le dossier **model** contient une version sérialisée du modèle entraîné :  
- **model.pkl** : Utilisé pour générer les recommandations de films.  

Les fichiers de sortie suivants sont également disponibles :  
- **data_cleaned.csv**, **data_reco.csv** et **model.pkl** (accessibles sur Google Drive).

---

## Dossiers Airflow, Kafka et FASTAPI :
### Airflow
- **airflow.cfg** : Fichier de configuration pour Apache Airflow, utilisé pour créer, planifier et surveiller des workflows.  
- **airflow.db** : Base de données SQLite utilisée par Airflow. Pour la production, il est recommandé d'utiliser PostgreSQL ou MySQL.  
- **dags** : Contient les scripts des pipelines Airflow.  

### FASTAPI
Dans le dossier **FASTAPI**, vous trouverez :  
- **app.py** : Application FastAPI fournissant une API pour générer des recommandations de films.  
  - Endpoint **/** : Renvoie un simple message "Hello world!".  
  - Endpoint **/suggested_movies** : Renvoie les 10 meilleurs films recommandés pour un utilisateur donné.  
- **data/data_reco.csv** : Contient les films avec leurs scores estimés.  
- **model/model.pkl** : Modèle de prédiction.

---

### Project_Netflix_Kafka
Ce dossier contient des scripts liés à Kafka :  

1. **ccloud_lib.py** : Fournit des fonctions pour interagir avec Confluent Cloud.  
2. **producer.py** : Envoie des données de l'API à un topic Kafka sous forme de JSON.  
3. **consumer.py** : Reçoit des données d’un topic Kafka et utilise FastAPI pour obtenir des recommandations, stockées ensuite dans PostgreSQL.

---

## Configuration de l'environnement :  

1. **Installer Miniconda** : Téléchargez l’installateur depuis le site officiel.  
2. **Créer un environnement Conda** :  
    ```bash
    conda create -n kafka_airflow_fasapi python=3.10
    conda activate kafka_airflow_fasapi
    ```
3. **Installer les bibliothèques nécessaires** :  
    ```bash
    conda install -c conda-forge argparse pandas
    pip install confluent-kafka joblib requests psycopg2 sqlalchemy
    ```

---

## Lancement :  

1. **Apache Airflow** :  
   - Initialisez la base de données :  
     ```bash
     airflow db init
     ```
   - Lancez le serveur web d’Airflow :  
     ```bash
     airflow webserver -p 8080
     ```
   - Lancez le scheduler :  
     ```bash
     airflow scheduler
     ```

2. **Kafka Producer et Consumer** :  
   - Producteur Kafka :  
     ```bash
     python3 producer.py
     ```
   - Consommateur Kafka :  
     ```bash
     python3 consumer.py
     ```

---

## Diagramme global de Kafka Confluent Streaming :
![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/61c6c3d9-3dc4-4a77-977b-b8810176341d)

Le flux Kafka inclut :  
- Génération de données en temps réel depuis l’API Jedha.  
- Publication des données dans des topics Kafka avec un producteur.  
- Consommation des données via FastAPI pour des recommandations.  
- Stockage dans Amazon S3 et PostgreSQL.

---

## Remarque :
En raison des limitations de taille sur GitHub, les fichiers volumineux **data_cleaned.csv** et **model.pkl** ont été remplacés par des versions réduites :  
- **data_cleaned_sample.csv** et **model_sample.pkl**.  
Pour accéder aux fichiers complets, consultez les répertoires Google Drive.

