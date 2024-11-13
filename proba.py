import paho.mqtt.client as mqtt
import random
import time

# Define the MQTT broker details
broker = 'test.mosquitto.org'
port = 1883
topic = "iot/sensor/temperature"

# Function to publish temperature data
def publish_temperature():
    client = mqtt.Client()
    client.connect(broker, port)
    
    while True:
        temperature = round(random.uniform(20.0, 30.0), 2)
        client.publish(topic, str(temperature))
        print(f"Published temperature: {temperature}")
        time.sleep(5)  # Simulate data every 5 seconds

if __name__ == "__main__":
    publish_temperature()
