Voici note projet YNOV Airlines

Projet Big Data & Data Viz RAMDANI Rayan et ABID Sabri

Voici notre projet qui permet la visualisation en temps réel du trafic aérien en Europe grâce streamlit. Nous avons utilisé l'API d'opensky pour pouvoir récuperer les données (latitude; longitude, id, vitesse, pays) Grace au canal Kafka que nous avons relié entre notre producer et notre consumer nous avons un flux de données regulier qui arrive sur notre consumer.

lien vers le site de l'API: https://openskynetwork.github.io/opensky-api/index.html Une fois les données dans notre consumer et grâce au DataFrame Sparks nous pouvons faire toute sorte de calcul. Nous avons choisi de calculer la moyenne de la vitesse des avions en vol.

De plus grâce à Stream lit nous pouvons visualiser Le DataFrame sous forme de tableau, une map de l'Europe avec des points représentant tous les avions en vols et un histogramme pour visualiser graphiquement la vitesse de chaque avion.

Il faut exécuter le setup.py pour pouvoir utiliser l'API avec la commande python setup.py install (si on se place dans le dossier qui contient le fichier setup.py) (le chemin depuis le dossier projet -> projet/open-api-master/python/setup.py)

Il faut ensuite lancer le docker avec la commande docker compose up (le fichier docker-compose.yml est présent dans le dossier projet\dok-kaf)

Il faut installer folium en local pour pouvoir faire marcher la visualisation des données avec la commande pip install folium

Il faut lancer le container avec la commande docker exec -it nom du container bash (on lance le container "jupyter/pyspark-notebook:python-3.8.8") puis on se met dans work et on execute le consumer cons_vol.py Dans le container jupyter/pyspark-notebook il faut installer les biliotheques suivante : pip install kafka-python pip install pyspark

Une fois ces installations faites on peut exécuter le consumer avec la commande python cons_vol.py (/!\ toujours depuis le dossier work du container)

En local il faut lancer le producer.py avec la commande python prod_vol.py (ce fichier se trouve dans le dossier projet projet/prod_vol.py

Avant de pouvoir faire la visualisation il faut installer Stream lit avec la commande pip install streamlit

et la commande "streamlit run projet.py" pour lancer le Stream lit viz (il faut être placé à l'endroit où est le fichier, directement dans le dossier projet)
