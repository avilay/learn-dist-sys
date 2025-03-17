import sys
from confluent_kafka import Producer


p = Producer({'bootstrap.servers': 'localhost'})
topic = sys.argv[1]

while True:
    pmsg = input('Enter partition:msg\n')
    partition, msg = pmsg.strip().split(':')
    partition = int(partition)
    p.produce(topic, msg.encode('utf-8'), partition=partition)
    p.flush()
