# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st
import folium
from opensky_api import OpenSkyApi
st.title('YNOV AIRLINES')   
api = OpenSkyApi()

# Pour récuperer les données des avions dont les pays sont a l'interieur de la bbox ici ce sont les pays europeens 
states = api.get_states(bbox=(35.332031,71.142435,-14.238281,34.648304)) 
l=[]

#On crée une liste qui va contenir toutes les informations dont nous avons besoin 
for s in states.states:
    if s.callsign !=(" ") and s.callsign != (''):
        if s.latitude !=None and s.longitude != None: 
            if s.velocity !=None and s.velocity != 0.0000:
                l=l+[{"id":s.callsign,"time":states.time,"longitude": s.longitude,"latitude": s.latitude,'vitesse':s.velocity,'pays':s.origin_country}]
     
#Transformation de la liste en DataFrame
df = pd.DataFrame(l)
st.write(df)

t = folium.Map(location=[20,0])


#Ici on affiche tous les avions en vol en fonction de leur latitude et longitude 
for i in range(0,len(l)):
   folium.Marker(location=[l[i]["latitude"], l[i]["longitude"]],popup=l[i]['id'],icon=folium.Icon(icon='plane')).add_to(t)

l1 = [" "]
for i in range(0,30):
    l1.append(l[i]['vitesse'])
 
del l1[0]
for i in range(0,30):
        int(l1[i])
print(l1)
    
chart_data = pd.DataFrame(l1, columns=['vitesse'])

#affichage de la map 
st.map(df)
st.bar_chart(chart_data)
#Ce bouton sert a rafraichir la map 
st.button("rerun")


