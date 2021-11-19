Projet Big Data & Data Viz RAMDANI Rayan et ABID Sabri

Voici notre projet qui permet la visualisation en temps reel du trafic aerien en europe grace a streamlit.
Nous avons utilisé l'API d'opensky pour pouvoir récuperer les données (latitude; longitude, id, vitesse, pays) 
Grace au canal kafka qui nous avons relié entre notre producer et notre consumer nous avons un flux de données regulier qui arrive sur notre consumer.

Une fois les données dan notre consumer et grace a la df Spark nous pouvons faire toute sorte de calcul nous avons choisit de calculer la moyenne de la vitesse dse avions. 


Il faut executer le setup.py present dans le dossier python lui meme present 
python setup.py install (une fois placé dans le dossier python qui lui est dans le dossier opensky-api-master)

Tout d'abord il faut lancer le docker avec la commande docker compose up (le fichier docker-compose.yml est present dans le dossier projet\dok-kaf)


Il faut installer folium en local pour pouvoir faire marcher la visualisation des données 
pip install folium


il faut lancer le container avec la commande 
	docker exec -it nom du container bash 
Dans le container jupyter/pyspark-notebook il faut installer les biliotheques suivante : 
	pip install kafka-python 
	pip install pyspark 

Une fois ces installations faites on peut executer le consumer avec la commande python cons_vol.py




streamlit run Projet.py pour lancer le streamlit viz (il faut etre placé a l'endroit ou est placé le fichier dans notre cas directement dans le dossier Projet