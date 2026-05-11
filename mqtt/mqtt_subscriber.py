import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "dairyfarm/methane"


def on_message(client, userdata, message):
    print("Received:", str(message.payload.decode()))


client = mqtt.Client()
client.on_message = on_message

client.connect(broker, port, 60)
client.subscribe(topic)

print("Listening for methane data...")

client.loop_forever()