#pip install kafka-python
import kafka-python
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')
# bootstrap_servers="localhost:9092" argument specifies the host/IP and port that the consumer should contact to bootstrap initial cluster metadata
# client_id specifies an id of current admin client

topic_list=[]

# create new topics:
new_topic = NewTopic(name="bankbranch", num_partitions= 2, replication_factor=1)
topic_list.append(new_topic)
admin_client.create_topics(new_topics=topic_list)

# describe a topic
configs = admin_client.describe_configs(
    config_resources=[ConfigResource(ConfigResourceType.TOPIC, "bankbranch")])
# we have a new bankbranch topic created

# kafka producer
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# using KafkaProducer to produce messages in JSON format:
producer.send("bankbranch", {'atmid':1, 'transid':100})
producer.send("bankbranch", {'atmid':2, 'transid':101})

# kafka consumer
consumer = KafkaConsumer('bankbranch')
for msg in consumer:
    print(msg.value.decode("utf-8"))
# iterate through all available messages and print
