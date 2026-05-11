import paho.mqtt.client as mqtt
import json
import random
import time

broker = "broker.hivemq.com"
port = 1883
topic = "dairyfarm/methane"

client = mqtt.Client()
client.connect(broker, port, 60)

while True:
    sensor_data = {
        "methane": random.randint(200, 600),
        "temperature": random.randint(25, 35),
        "humidity": random.randint(50, 80),
        "ammonia": random.randint(20, 70)
    }

    client.publish(topic, json.dumps(sensor_data))
    print("Published:", sensor_data)

    time.sleep(5)