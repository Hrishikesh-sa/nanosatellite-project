import Adafruit_DHT
import smbus2
import bme280
import socket
import time

# DHT11 setup
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

# BMP280 setup (I2C)
port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

# UDP setup
UDP_IP = "192.168.10.1"   # Change to your laptop IP
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Read DHT11
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    # Read BMP280
    data = bme280.sample(bus, address, calibration_params)
    pressure = data.pressure

    if humidity is not None and temperature is not None:
        message = f"{temperature},{humidity},{pressure}"
        print("Sending:", message)

        sock.sendto(message.encode(), (UDP_IP, UDP_PORT))

    else:
        print("Failed to retrieve data from DHT11")

    time.sleep(2)