import sys
from confluent_kafka import Consumer, KafkaError

group = sys.argv[1]
topic = sys.argv[2]

c = Consumer({
    'bootstrap.servers': 'localhost',
    'group.id': group,
    'default.topic.config': {
        'auto.offset.reset': 'smallest'
    }
})
c.subscribe([topic])
while True:
    try:
        msg = c.poll()
        if not msg.error():
            print(f'Received msg\n {msg.partition()}:{msg.value()}')
        elif msg.error().code() != KafkaError._PARTITION_EOF:
            print(msg.error())
            running = False
    except KeyboardInterrupt:
        c.close()
