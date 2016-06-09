from kafka import KafkaConsumer
import avro.schema
import avro.io
import io

topic = 'my-topic'

# To consume messages
consumer = KafkaConsumer(topic,
                         bootstrap_servers=['localhost:9092'])

schema_path="user.avsc"
schema = avro.schema.parse(open(schema_path).read())

for msg in consumer:
    bytes_reader = io.BytesIO(msg.value)
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(schema)
    user1 = reader.read(decoder)
    print user1
