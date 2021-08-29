from pyspark.sql import SparkSession
import json

# create spark session, utilizing all the available cores on the machine.
spark = SparkSession.\
    builder.\
    master("local[*]").\
    appName("streamin application version 1").\
    getOrCreate()

# reading streamin data
streamin_df = spark.readStream.\
    format("kafka").\
    option("kafka.bootstrap.servers", "").\
    option("subscribe", "retail").\
    option("startingOffsets", "latest").\
    option("minPartitions", "2").\
    option("failOnDataLoss", "true").\
    load()

# testing result on console
query = streamin_df.\
    writeStream.\
    trigger(processingTime='5 seconds').\
    format("console").\
    outputMode("append").\
    start()


