```markdown
# LEAD-Bloc1-Netflix-Recommendation-Jedha
## ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/f17d64a9-3922-4cee-87dc-9b881085659c) Moteur de recommandation Netflix ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/f17d64a9-3922-4cee-87dc-9b881085659c)
![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/2f002cd8-a41b-4e93-a357-b8eba4d86e69)

Ce dépôt (localisé sur Github) / document Word (localisé sur Google Drive) contient toutes les ressources liées à la présentation du projet sur le moteur de recommandation Netflix.

## Ressources disponibles :

- Le diaporama de la présentation est accessible dans le fichier nommé **Présentation_Certification_Bloc_1_Netflix_reco_en.pptx**.
- Ressources supplémentaires, y compris le modèle et les données d’entraînement, disponibles à ce lien : [Google Drive](https://drive.google.com/drive/folders/14qz8C2JKb7AuaLz6VbQjgEoHbhNFNw5S?usp=drive_link).
- Le sujet du projet est accessible ici : [Jedha Final Projects](https://app.jedha.co/course/final-projects-l/netflix-automation-engine-l). Une description des dossiers et objectifs de ce dépôt est présentée ci-dessous.

Pour toute question ou information complémentaire, contactez le propriétaire du dépôt sur GitHub : billel0912 (billel_abbas@yahoo.fr).

## ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/54ed3921-f6f6-4603-92b7-89904323f64d) Prétraitement et Entraînement du Modèle : ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/3b255f3b-1bc7-4eb1-9c02-512b41a4839b)

Ce dossier, nommé **Preprocessing_Netflix**, contient un script appelé **data_preprocessing.ipynb** qui intègre les données issues de Kaggle et construit l’ensemble de données d’entraînement pour le modèle de recommandation. 

- Les données brutes se trouvent dans le dossier **data**, issues de [Kaggle](https://www.kaggle.com/code/laowingkin/netflix-movie-recommendation).
- Ce dossier contient également des informations sur l’entraînement du modèle. Le dossier **model** contient une version sérialisée du modèle de recommandation entraîné, stockée sous la forme d’un fichier pickle nommé **model.pkl**. Ce modèle génère les prédictions de films.
- Les fichiers de sortie **data_cleaned.csv**, **data_reco.csv** et **model.pkl**, qui incluent les données nettoyées et le modèle entraîné, sont disponibles sur Google Drive.

## Dossiers Airflow ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/9679373f-f151-4117-9696-7a712769d2e4), Kafka ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/8a330337-5048-4ce4-9e7b-7e24e0362887) et FASTAPI ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/92dbeb3f-bb06-442a-81f9-e661b7754ada) :

Dans le dossier **Project_Final_Kafka**, nous trouvons :

### Airflow
1. **airflow.cfg** : fichier de configuration pour Apache Airflow, une plateforme pour créer, planifier et surveiller des workflows.
2. **airflow.db** : base de données SQLite3 utilisée par Airflow pour gérer les DAGs et tâches.
3. **dags** : dossier contenant les pipelines Airflow (DAGs).

   Dans ce dossier **dags**, se trouve :
   - **dag.py** : script Python définissant un DAG dans Airflow. Ce DAG exécute trois tâches principales : **run_start**, **run_all**, et **run_end**. La tâche **run_all** lance les scripts **app.py**, **producer.py**, et **consumer.py**.

### FASTAPI
- Le dossier contient :
  - **app.py** : application FastAPI proposant une API pour les recommandations de films.
  - **data** : contient le fichier **data_reco.csv**.
  - **model** : contient le modèle de prédiction **model.pkl**.

### Kafka
1. **ccloud_lib.py** : script Python fournissant des fonctions pour interagir avec Confluent Cloud.
2. **python.config** : fichier de configuration pour l’application Python interagissant avec Confluent Cloud.
3. **producer.py** : producteur Kafka qui envoie des données à un topic Kafka.
4. **consumer.py** : consommateur Kafka qui reçoit des données depuis un topic Kafka.

**Remarque** : Avant d’exécuter ces scripts, suivez les étapes d’installation décrites dans le dépôt.

## Lancement : Airflow DAGs, FASTAPI et Kafka Streaming

### Étapes :
1. **Vérifiez la version de Python** (Python 3.10 recommandé).
2. **Installez Apache Airflow**.
3. Configurez Airflow et démarrez le serveur web Airflow à l’adresse [http://localhost:8080](http://localhost:8080).
4. Activez et exécutez les DAGs depuis l’interface Airflow.

## Diagramme global de Kafka Confluent Streaming

![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/61c6c3d9-3dc4-4a77-977b-b8810176341d)

Le flux Kafka Confluent inclut :
- Génération de données en temps réel depuis l’API Jedha.
- Producteur Kafka publiant des données dans des topics Kafka.
- Consommateur Kafka interagissant avec FastAPI pour les prédictions.
- Données stockées dans un bucket Amazon S3 et une base de données PostgreSQL.

## ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/6386d9f5-74d6-4105-8cc2-a52700a3521d) Remarque :
En raison des limitations de taille de fichier sur GitHub (25 Mo max), les fichiers volumineux **data_cleaned.csv** et **model.pkl** ont été remplacés par des versions d’échantillon nommées **data_cleaned_sample.csv** et **model_sample.pkl**. Ces fichiers d’échantillon sont disponibles dans les répertoires correspondants sur GitHub. Les fichiers complets sont disponibles sur Google Drive.
```
