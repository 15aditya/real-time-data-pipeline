# Get into kafka installation directory
cd kafka

# Creating kafka topic
sh bin/kafka-topics.sh --zookeeper localhost:2181 \
  --create \
  --topic retail \
  --partitions 2 \
  --replication-factor 1

# List kafka topic
sh bin/kafka-topics.sh --zookeeper localhost:2181 \
  --list \
  --topic retail

# Describe kafka topic
sh bin/kafka-topics.sh --zookeeper localhost:2181 \
  --describe \
  --topic retail

