## Real Time Data Pipeline

This repository contains data pipeline architecture, code 
and test scripts of building real time data piplines.

#### Technology Stack
* Kafka
* Spark Structured Streaming
* Databricks
* AWS
* Python 3+

#### Architecture

![plot](./real-time-pipeline-arch.png)


#### Steps to Navigate and Consume the repository code for own perusal.

TODO

aws cloudformation package --template-file master.yaml --output-template-file temp-template.templat
e --region ap-south-1 --s3-bucket aws-lab-real-time-datapipeline

aws cloudformation deploy --template-file C:\Users\Aditya\PycharmProjects\real-time-data-pipeline\t
emp-template.template --stack-name real-time-datapipeline
