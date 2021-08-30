from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
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

# reading static lookup data
lookup_df = spark.\
    read.\
    format("parquet").\
    options(header='true', inferSchema='true').\
    load("")

# reading file using custom schema
schema = StructType([
    StructField('id', IntegerType(), False),
    StructField('name', StringType(), True)
])
lookup_df_schema = spark.\
    read.\
    format('parquet').\
    options(header='true').\
    schema(schema).\
    load()

# print schema of dataframe
lookup_df.printSchema()


# join streams wih lookup data
joined = streamin_df.\
    join(lookup_df_schema, on=['id'], how='left outer').\
    select(streamin_df.id, streamin_df.action, lookup_df_schema.is_applicable)

# count number of occurence of each action.
joined_agg_df = joined.groupBy(joined.action).count()

# testing result on console
query = joined_agg_df.\
    writeStream.\
    trigger(processingTime='5 seconds').\
    format("console").\
    outputMode("append").\
    start()

# using output sink to write data as parquet
query_output_sink = joined_agg_df.\
    writeStream.\
    trigger(processingTime='2 seconds').\
    format('parquet').\
    option('path', '').\
    start()

# await termination from user's end.
query_output_sink.awaitTermination()
