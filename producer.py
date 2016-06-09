from kafka import KafkaProducer
import avro.schema
import io, random
from avro.io import DatumWriter

# To send messages synchronously
producer = KafkaProducer(bootstrap_servers='http://172.19.0.4:9092')

# Kafka topic
topic = "my-topic"

# Path to user.avsc avro schema
schema_path="user.avsc"
schema = avro.schema.parse(open(schema_path).read())


for i in xrange(10):
    writer = avro.io.DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write({"name": "123", "favorite_color": "111", "favorite_number": random.randint(0,10)}, encoder)
    raw_bytes = bytes_writer.getvalue()
    producer.send_messages(topic, raw_bytes)
