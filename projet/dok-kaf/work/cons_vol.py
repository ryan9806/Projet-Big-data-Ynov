# -*- coding: utf-8 -*-

import pandas as pd
from kafka import KafkaConsumer
import json

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, FloatType, IntegerType,StringType

# Spark session & context
spark = (SparkSession
         .builder
         .master('local')
         .appName('avions')
         # Add kafka package
         .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1")
         .getOrCreate())

#sc = spark.sparkContext

c = KafkaConsumer('test5', bootstrap_servers=['kafka:9093'], api_version=(2,6,0))

# Event data schema
cSchema = StructType([StructField("id", StringType())\
                     ,StructField("time", IntegerType())\
                     ,StructField("longitude", FloatType())\
                     ,StructField("latitude", FloatType())\
                     ,StructField("vitesse", FloatType())\
                     ,StructField("pays", StringType())])


for msg in c:
    df = pd.DataFrame(json.loads(msg.value))    #charger le message dans un Data-Frame df
    df1=df[~df['vitesse'].isna()]               #suprimmer les vitesses null
        
    dfs = spark.createDataFrame(df1,schema=cSchema)    #charger la Data-Frame df dans un Data-Frame SPARK dfs 
    print(dfs.show())                                  #affichage de la dfs
    print(dfs.agg({'vitesse' : 'mean'}).show())        #calcul et affichage de la moyenne des vitesses
    print("le nombre d'avions en vol actuellement est de : " , dfs.count())
    
    