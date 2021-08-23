# Starting Kafka Connect
nohup bin/connect-standalone.sh config/connect-standalone.properties config/connect-file-source.properties \
> ~/kafka-connect-logs &

# Making sure if we can consume messages
sh bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic retail
