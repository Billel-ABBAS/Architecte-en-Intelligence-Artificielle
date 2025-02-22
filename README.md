# LEAD-Bloc1-Netflix-Recommendation-Jedha
## ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/f17d64a9-3922-4cee-87dc-9b881085659c) Moteur de recommandation Netflix ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/f17d64a9-3922-4cee-87dc-9b881085659c)
![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/2f002cd8-a41b-4e93-a357-b8eba4d86e69)

Ce dépôt (situé sur GitHub) / fichier Word (situé sur Google Drive) contient toutes les ressources relatives à la présentation du projet sur le moteur de recommandation de Netflix.

## Toutes les ressources :

Le diaporama de la présentation est accessible dans le fichier nommé **Présentation_Certification_Bloc _1_Netflix_reco_en.pptx**.  
Des ressources supplémentaires, y compris le modèle et les données d'entraînement, sont disponibles à ce lien : [https://drive.google.com/drive/folders/14qz8C2JKb7AuaLz6VbQjgEoHbhNFNw5S?usp=drive_link](https://drive.google.com/drive/folders/14qz8C2JKb7AuaLz6VbQjgEoHbhNFNw5S?usp=drive_link).  
Le sujet du projet peut être trouvé ici : [https://app.jedha.co/course/final-projects-l/netflix-automation-engine-l](https://app.jedha.co/course/final-projects-l/netflix-automation-engine-l). Une description du contenu et des objectifs de chaque dossier de ce dépôt est fournie ci-dessous.  
Si vous avez des questions ou besoin de plus d'informations sur ce projet, n'hésitez pas à contacter le propriétaire du dépôt sur GitHub : **billel0912** (billel_abbas@yahoo.fr).

## ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/54ed3921-f6f6-4603-92b7-89904323f64d) Dossier Préprocessing et entraînement du modèle : ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/3b255f3b-1bc7-4eb1-9c02-512b41a4839b)

Ce répertoire, nommé **Preprocessing_Netflix**, contient un script appelé **data_preprocessing.ipynb**. Ce script effectue l'intégration des données de Kaggle et construit le jeu de données d'entraînement pour le modèle de recommandation.  
Le dossier **data** contient les données brutes, qui ont été extraites de [https://www.kaggle.com/code/laowingkin/netflix-movie-recommendation](https://www.kaggle.com/code/laowingkin/netflix-movie-recommendation).  
En outre, ce répertoire comprend également des informations relatives à l'entraînement du modèle. Le dossier **model** contient une version sérialisée du modèle de recommandation entraîné, stockée sous forme de fichier pickle nommé **model.pkl**. Ce modèle est utilisé pour générer des prédictions de films.  
Les fichiers de sortie, **data_cleaned.csv** et **data_reco.csv**, ainsi que **model.pkl**, qui contiennent les données prétraitées, nettoyées et le modèle entraîné, sont disponibles sur Google Drive.

## Dossier Airflow![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/9679373f-f151-4117-9696-7a712769d2e4), Kafka![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/8a330337-5048-4ce4-9e7b-7e24e0362887) et FASTAPI![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/92dbeb3f-bb06-442a-81f9-e661b7754ada) :
Dans le dossier **Project_Netflix_Kafka**, nous trouvons :

**airflow.cfg** : Il s'agit d'un fichier de configuration pour Apache Airflow, une plateforme pour créer, planifier et surveiller des workflows. Il contient les paramètres d'Airflow et peut être modifié pour les ajuster.  
**airflow.db** : C'est la base de données utilisée par Airflow pour gérer ses DAGs et tâches. Ce fichier est au format SQLite3 et peut être utilisé pendant le développement, mais il est fortement recommandé de passer à un autre type (comme PostgreSQL ou MySQL) lors du passage en production.  
**dags** : Ce dossier dans Airflow est le répertoire où vos pipelines Airflow, ou DAGs (Directed Acyclic Graphs), sont stockés. L'emplacement de ce dossier est spécifié dans le fichier **airflow.cfg**, situé dans votre répertoire **$AIRFLOW_HOME**. Vous pouvez trouver le chemin du dossier **dags** en vérifiant le paramètre **dags_folder** dans le fichier **airflow.cfg**.  
Dans ce dossier **dags**, nous trouvons :  
1. **Script “dag.py”** : Il s'agit d'un script Python qui définit un DAG (Directed Acyclic Graph) dans Apache Airflow. Un DAG est le concept central d'Airflow et regroupe des tâches, organisées avec des dépendances et des relations pour spécifier leur ordre d'exécution. Dans ce script, trois tâches sont définies : **run_start**, **run_all**, et **run_end**. La tâche la plus importante est **run_all**, qui doit lancer trois scripts : **app.py** (FastAPI), **producer.py**, et **consumer.py**. Ces scripts sont lancés en utilisant une commande Bash dans le paramètre **bash_command** de **BashOperator**. Les tâches sont organisées en séquence en utilisant l'opérateur **>>**, de sorte que **run_start** est exécuté en premier, suivi de **run_all**, et enfin **run_end**.

2. **Dossier “FASTAPI”** : Dans le dossier **FASTAPI**, vous avez le script **app.py**, le dossier **data** contenant le fichier **data_reco**, et le dossier **model** contenant le modèle de prédiction **model.pkl**. Le script **app.py** est une application FastAPI qui fournit une API pour faire des recommandations de films pour un utilisateur donné. L'API a deux endpoints : **/**, qui renvoie un simple message "Hello world!", et **/suggested_movies**, qui renvoie les 10 meilleurs films recommandés pour un ID utilisateur donné. Le modèle utilisé pour faire les prédictions est chargé en utilisant la bibliothèque **joblib**, et les prédictions sont faites en appliquant la méthode **predict** du modèle aux ID de films dans le fichier **data_reco.csv**.

3. **Dossier ‘kafka_netflix”** : Nous trouvons dans ce dossier :
   
**ccloud_lib.py** : Il s'agit d'un script Python qui fournit des fonctions d'aide pour interagir avec Confluent Cloud, un service Apache Kafka entièrement géré. Le script inclut des classes pour définir des schémas et des enregistrements Avro, ainsi que des fonctions pour analyser les arguments de ligne de commande, lire les fichiers de configuration de Confluent Cloud et créer des topics Kafka.

**python.config** : Il s'agit d'un fichier de configuration utilisé pour stocker les paramètres d'une application Python qui interagit avec Confluent Cloud. Le fichier contient les configurations de connexion requises pour le producteur Kafka, le consommateur et l'administrateur, ainsi que les configurations de connexion requises pour Confluent Cloud Schema Registry. Les paramètres incluent les serveurs bootstrap, le protocole de sécurité, les mécanismes SASL, le nom d'utilisateur et le mot de passe SASL, le délai d'expiration de session, l'URL du registre de schémas et les informations d'identification d'authentification de base.

**Script “producer.py”** : Ce script est un producteur Kafka qui envoie des données à un topic Kafka dans Confluent Cloud. Le script lit la configuration de Confluent Cloud à partir du fichier **python.config** et crée une instance **Producer** en utilisant ces paramètres. Le script inclut également une fonction, **movie_api_get**, qui envoie une requête GET à une API et traite la réponse en un DataFrame pandas. Les données de ce DataFrame sont ensuite envoyées au topic Kafka sous forme de chaîne JSON en utilisant la méthode **produce** de l'instance **Producer**. Le script inclut une fonction de rappel, **acked**, qui est appelée lorsqu'un message a été livré avec succès ou a échoué de manière permanente. Le script fonctionne dans une boucle infinie, envoyant des données au topic Kafka toutes les 20 secondes jusqu'à ce qu'il soit interrompu par l'utilisateur.

**Script “consumer.py”** : Ce script est un consommateur Kafka qui reçoit des données d'un topic Kafka dans Confluent Cloud et les traite. Le script lit la configuration de Confluent Cloud à partir du fichier **python.config** et crée une instance **Consumer** en utilisant ces paramètres. Le script s'abonne au topic Kafka et interroge de nouveaux messages dans une boucle infinie. Lorsqu'un nouveau message est reçu, le script décode la valeur du message, qui est une chaîne JSON, et la convertit en un DataFrame pandas. Le script extrait ensuite l'ID utilisateur de ce DataFrame et envoie une requête GET à une application FastAPI locale pour obtenir les 10 meilleurs films recommandés pour cet utilisateur. Les données résultantes sont ensuite insérées dans une base de données PostgreSQL en utilisant la méthode **to_sql** du DataFrame pandas.

**Remarque** : Avant de procéder à l'installation et à l'exécution des trois scripts (**app.py**, **producer.py**, et **consumer.py**), il est essentiel de configurer l'environnement approprié avec les dépendances nécessaires. Pour ce faire, suivez ces étapes :
1. **Installer Miniconda** : Commencez par installer Miniconda, un installateur minimal de Conda, en téléchargeant le script d'installation depuis le site web de Miniconda et en suivant les instructions d'installation spécifiques à la plateforme.
2. **Ouvrir un terminal** : Ouvrez un terminal sur votre système Ubuntu.
3. **Créer un environnement Conda** : Utilisez le terminal pour créer un nouvel environnement Conda nommé "kafka_airflow_fasapi" avec Python version 3.10 :  
**conda create -n kafka_airflow_fasapi python=3.10**
4. **Activer l'environnement** : Activez le nouvel environnement :  
**conda activate kafka_airflow_fasapi**
5. **Installer les bibliothèques** : Dans l'environnement activé, installez les bibliothèques requises en utilisant Conda et Pip. Les bibliothèques installées dans l'environnement incluent **argparse**, **sys**, **confluent_kafka**, **confluent_kafka.avro**, **confluent_kafka.admin**, **uuid**, **joblib**, **pandas**, **io**, **requests**, **datetime**, **time**, **psycopg2**, et **sqlalchemy** :  
**conda install -c conda-forge argparse pandas  
pip install confluent-kafka confluent-kafka[avro] joblib requests psycopg2 sqlalchemy**

## Comment lancer : Airflow dags, FASTAPI et Kafka streaming :

### Étapes pour lancer :

a. **Vérifier la version de Python** : Vérifiez votre version de Python. Si c'est Python 3.10, utilisez cette version dans les étapes suivantes. Par exemple : **python3.10 –version**

b. **Installer Apache Airflow** : Installez Apache Airflow 2.6.3 en utilisant pip avec la version de Python spécifiée et les contraintes :  
**pip install 'apache-airflow==2.6.3' --constraint https://raw.githubusercontent.com/apache/airflow/constraints-2.6.3/constraints-3.10.txt**

c. **Définir AIRFLOW_HOME** : Définissez la variable d'environnement **AIRFLOW_HOME** sur le répertoire courant :  
**export AIRFLOW_HOME=.**

d. **Initialiser la base de données Airflow** : Initialisez la base de données Airflow :  
**airflow db init**

e. **Démarrer le serveur web Airflow** : Démarrez le serveur web Airflow pour gérer vos DAGs localement. Choisissez un numéro de port (par exemple, 8080) :  
**airflow webserver -p 8080** (Accédez à l'interface utilisateur d'Airflow en visitant [http://localhost:8080](http://localhost:8080) dans votre navigateur web.)

![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/4e788f86-8ad0-4fc0-bbd1-4cdb01a1f9ef)

f. **Créer un utilisateur admin** : Créez un utilisateur admin pour l'authentification dans l'interface utilisateur d'Airflow :  
**airflow users create --username admin --firstname PRÉNOM --lastname NOM --password admin --role Admin --email admin@example.org**

g. **Démarrer le planificateur Airflow** : Lancez le planificateur Airflow pour gérer la planification des DAGs :  
**airflow scheduler**  
Après avoir démarré le planificateur, ouvrez votre navigateur web et accédez à [http://localhost:8080](http://localhost:8080) pour accéder à l'interface utilisateur d'Airflow. Une fois l'interface ouverte, vous devriez voir le **daily_dag** listé parmi vos DAGs. Cela vous permet de surveiller, déclencher et gérer l'exécution de votre **daily_dag** depuis l'interface utilisateur d'Airflow.

![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/1b320555-3699-4259-988b-26d063f890eb)

h. **Exécuter daily_dag depuis l'interface utilisateur d'Airflow** : Après avoir accédé à l'interface utilisateur d'Airflow à [http://localhost:8080](http://localhost:8080), localisez et déclenchez le **daily_dag** depuis l'interface. Cela exécutera le DAG selon son planning et les tâches définies.

![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/2879e135-a0e9-40dc-982d-0902ea8e898d)

i. **Définition du DAG** : Le **daily_dag** est défini dans le script **dag.py**. Ce DAG inclut des tâches telles que **run_start**, **run_all**, et **run_end**. La tâche **run_all** est responsable de l'exécution des trois scripts. Elle commence par lancer **app.py** (FASTAPI) en premier. Pour tenir compte de la taille importante du modèle FASTAPI, il y a un délai de 500 secondes pour s'assurer que FASTAPI se lance avec succès avant que le script **consumer.py** ne démarre. Ce délai est crucial pour éviter que le script **consumer.py** ne échoue car il dépend de **FASTAPI**. De plus, les scripts **producer.py** et **consumer.py** sont lancés en arrière-plan dans le shell Ubuntu.

Si nous lançons dans le shell **python3 producer.py** :

![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/c89156bc-1647-4a21-8cf8-1e2be66a73d2)

Si nous lançons dans le shell **python3 consumer.py** :

![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/6998b725-ed37-4e69-b612-44f799b1af37)

Cela leur permet de fonctionner simultanément sans se bloquer mutuellement, améliorant ainsi l'efficacité globale du processus de streaming de données.  
Pendant l'exécution du **daily_dag**, le script **app.py** (FASTAPI) peut être accessible via un navigateur web en naviguant vers [http://localhost:4000](http://localhost:4000). Cela vous permet d'interagir avec l'application FastAPI et de faire des recommandations de films pour un ID utilisateur donné.  
Pendant que ces scripts s'exécutent, vous pouvez observer la progression et les interactions dans Confluent Kafka. Les graphiques correspondants du producteur et du consommateur seront affichés, montrant le flux de données en temps réel et la communication entre les composants. Cette représentation graphique fournit des informations précieuses sur la fonctionnalité et les performances de votre système de streaming de données.

![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/782096a2-ee46-466d-9617-5b99fb2ef2cb)

j. **Stockage des données** :  
Les données générées par le producteur Kafka et traitées par le consommateur Kafka seront gérées de deux manières :

• **Stockage Amazon S3** : En utilisant Amazon S3 Sink, les données produites par votre producteur Kafka seront stockées efficacement dans un bucket Amazon S3 (AWS). Cette solution de stockage scalable garantit que vos données sont préservées et facilement accessibles pour une analyse et un traitement ultérieurs.

• **Stockage dans une base de données PostgreSQL** : Du côté du consommateur, les données traitées seront stockées dans une base de données PostgreSQL. Cette base de données relationnelle offre un stockage structuré pour vos données, les rendant adaptées à divers besoins de requêtes et de rapports.

• **Surveiller l'exécution du DAG** : Surveillez l'exécution de notre DAG dans l'interface utilisateur d'Airflow. Vous devriez pouvoir voir la progression de chaque tâche et leur statut.

![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/809820da-c434-4f41-8aea-d569b5480694)

## Diagramme global du streaming Kafka Confluent :

Le flux de données Kafka Confluent implique la génération de données en temps réel à partir de l'API Jedha, traitées par **producer.py** pour être publiées dans des topics Kafka. Kafka Confluent, intégré à Amazon S3 Sink, stocke les données dans un bucket S3. Le script **consumer.py** consomme les données, FastAPI prédit les recommandations de films, et PostgreSQL stocke les résultats. DataClips visualise les données, tandis que Zapier automatise les notifications par e-mail pour les nouvelles prédictions.  
Ce flux orchestré permet un streaming, un traitement et un stockage efficaces des données, améliorant la fonctionnalité et l'expérience utilisateur du moteur de recommandation Netflix.

![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/61c6c3d9-3dc4-4a77-977b-b8810176341d)

# ![image](https://github.com/billel0912/LEAD-Bloc1-Netflix-Recommendation-Jedha/assets/114284427/6386d9f5-74d6-4105-8cc2-a52700a3521d) Remarque :  
**En raison des limitations de taille de fichier de GitHub (les fichiers de plus de 25 Mo ne peuvent pas être téléchargés), les fichiers originaux de grande taille **data_cleaned.csv** et **model.pkl** ont été remplacés par des versions échantillons plus petites nommées **data_cleaned_sample.csv** et **model_sample.pkl**. Ces fichiers échantillons sont disponibles dans les répertoires correspondants **Preprocessing_Netflix_Sample_GitHub** et **Project_Final_Kafka_Sample_GitHub** sur GitHub. Pour les fichiers de taille complète, référez-vous aux répertoires Google Drive.**
