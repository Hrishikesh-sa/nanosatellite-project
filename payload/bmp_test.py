import time
import board
import busio
import adafruit_bmp280

i2c = busio.I2C(board.SCL, board.SDA)

bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

while True:
    print("Temperature:", bmp280.temperature)
    print("Pressure:", bmp280.pressure)
    print("----------------------")
    time.sleep(2)