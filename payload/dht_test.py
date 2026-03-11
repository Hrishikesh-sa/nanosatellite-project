GNU nano 8.4                                                 dht_test.py
import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temp = dhtDevice.temperature
        hum = dhtDevice.humidity

        if hum is not None and temp is not None:
            print(f"Temp: {temp:.1f}C  Humidity: {hum}%")
        else:
            print("Failed to retrieve data. Retrying...")

    except RuntimeError as error:
        print("Reading...")
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)