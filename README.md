# LEAD-Bloc1-Recommandation-Netflix-Jedha
## ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/f17d64a9-3922-4cee-87dc-9b881085659c) Moteur de recommandation Netflix ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/f17d64a9-3922-4cee-87dc-9b881085659c)
![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/2f002cd8-a41b-4e93-a357-b8eba4d86e69)

Ce dépôt (localisé sur GitHub) / document Word (localisé sur Google Drive) contient toutes les ressources liées à la présentation du projet sur le moteur de recommandation Netflix.

## Toutes les ressources :

- Le diaporama de la présentation est accessible dans le fichier nommé **Présentation_Certification_Bloc_1_Netflix_reco_en.pptx**.
- Des ressources supplémentaires, y compris le modèle et les données d’entraînement, sont disponibles à ce lien : [Google Drive](https://drive.google.com/drive/folders/14qz8C2JKb7AuaLz6VbQjgEoHbhNFNw5S?usp=drive_link).
- Le sujet du projet est accessible ici : [Jedha Final Projects](https://app.jedha.co/course/final-projects-l/netflix-automation-engine-l).  
  Une description du contenu et des objectifs de chaque dossier de ce dépôt est fournie ci-dessous.  

Si vous avez des questions ou avez besoin de plus d’informations sur ce projet, n’hésitez pas à contacter le propriétaire du dépôt sur GitHub : **billel0912** (billel_abbas@yahoo.fr).

---

## ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/54ed3921-f6f6-4603-92b7-89904323f64d) Dossier Prétraitement et Entraînement du Modèle : ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/3b255f3b-1bc7-4eb1-9c02-512b41a4839b)

Ce répertoire, nommé **Preprocessing_Netflix**, contient un script appelé **data_preprocessing.ipynb**.  
Ce script réalise l'intégration des données provenant de Kaggle et construit l'ensemble de données d'entraînement pour le modèle de recommandation.  

- Le dossier **data** contient les données brutes, issues de [Kaggle](https://www.kaggle.com/code/laowingkin/netflix-movie-recommendation).  
- Le dossier **model** contient une version sérialisée du modèle de recommandation entraîné :  
  - **model.pkl** : Ce fichier est utilisé pour générer des prédictions de films.  
- Les fichiers de sortie (fichiers nettoyés et modèle) **data_cleaned.csv**, **data_reco.csv** et **model.pkl** sont disponibles sur Google Drive.

---

## Dossier Airflow, Kafka et FASTAPI :
Dans le répertoire **Project_Netflix_Kafka**, on trouve les fichiers suivants :

### Apache Airflow :
1. **airflow.cfg** : Fichier de configuration pour Apache Airflow, une plateforme permettant de créer, planifier et surveiller des workflows.  
2. **airflow.db** : Base de données utilisée par Airflow pour gérer ses DAGs (Directed Acyclic Graphs) et tâches.  
3. **dags** : Ce dossier contient les pipelines définis dans Airflow.  
   - **Script “dag.py”** : Définit un DAG avec trois tâches principales :  
     - **run_start**, **run_all** et **run_end**.  
     La tâche **run_all** exécute trois scripts : **app.py** (FastAPI), **producer.py** et **consumer.py**.  

### FastAPI :
Dans le dossier **FASTAPI**, vous trouverez :  
- **app.py** : Fournit une API avec deux points d’accès :  
  - **/** : Retourne un simple message "Hello world!".  
  - **/suggested_movies** : Retourne les 10 meilleurs films recommandés pour un utilisateur donné.  
- **data/data_reco.csv** : Contient les films avec leurs scores estimés.  
- **model/model.pkl** : Le modèle de prédiction pour générer les recommandations.

---

## Scripts Kafka :
1. **ccloud_lib.py** : Fournit des fonctions pour interagir avec Confluent Cloud.  
2. **producer.py** : Envoie les données extraites d'une API vers un topic Kafka.  
3. **consumer.py** : Reçoit des données de Kafka et utilise FastAPI pour obtenir des recommandations, qui sont ensuite stockées dans une base PostgreSQL.

---

## Étapes pour lancer le projet :

1. **Créer un environnement Conda** :  
   ```bash
   conda create -n kafka_airflow_fasapi python=3.10
   conda activate kafka_airflow_fasapi
   ```
2. **Installer les bibliothèques nécessaires** :  
   ```bash
   conda install -c conda-forge argparse pandas
   pip install confluent-kafka joblib requests psycopg2 sqlalchemy
   ```
3. **Lancer Airflow** :
   - Initialisez la base :  
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

---

## Diagramme global du flux Kafka :  

![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/61c6c3d9-3dc4-4a77-977b-b8810176341d)

Le flux Kafka inclut :  
- Génération de données en temps réel depuis l’API Jedha.  
- Publication des données dans des topics Kafka.  
- Consommation via FastAPI pour générer des recommandations.  
- Stockage dans Amazon S3 et PostgreSQL.

---

## Remarque :
En raison des limitations de taille sur GitHub, les fichiers volumineux **data_cleaned.csv** et **model.pkl** ont été remplacés par des versions réduites :  
- **data_cleaned_sample.csv** et **model_sample.pkl**.  

Pour accéder aux fichiers complets, consultez les répertoires Google Drive.