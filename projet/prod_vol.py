from kafka import KafkaProducer
import json
import numpy as np

import time


from opensky_api import OpenSkyApi


p = KafkaProducer(bootstrap_servers=['localhost:9092'])
l=[]


i = 0
while True:
    api = OpenSkyApi()
    states = api.get_states(bbox=(35.332031,71.142435,-14.238281,34.648304)) #pour limiter la localisation à l'europe
    for s in states.states:
        if s.callsign !=(" ") and s.callsign != (''):                       
            if s.latitude !=None and s.longitude != None:
                l=l+[{"id":s.callsign,"time":states.time,"longitude": s.longitude,"latitude": s.latitude,'vitesse':s.velocity,'pays':s.origin_country}]
                

    p.send('test5', json.dumps(l).encode('utf-8'))
    p.flush()
    i += 1
    time.sleep(2)