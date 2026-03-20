import matplotlib.pyplot as plt

temperature = []
humidity = []
pressure = []

with open("sensor_data.csv", "r") as file:
    for line in file:
        t, h, p = line.strip().split(",")
        temperature.append(float(t))
        humidity.append(float(h))
        pressure.append(float(p))

plt.figure()

plt.subplot(3, 1, 1)
plt.plot(temperature)
plt.title("Temperature (°C)")

plt.subplot(3, 1, 2)
plt.plot(humidity)
plt.title("Humidity (%)")

plt.subplot(3, 1, 3)
plt.plot(pressure)
plt.title("Pressure (hPa)")

plt.tight_layout()
plt.show()