# TinyCircuits Temp/Press/Hum/VOC BME680 Wireling Example
# Prints values of temperature, VOC, humidity, pressure,
# and altitude read by the sensor every 2 seconds.
# Initialized: 01-21-2020
# Last Updated: 01-21-2020

from busio import I2C
import adafruit_bme680
import time
import board
import tinycircuits_wireling

# Initialize and enable power to Wireling Pi Hat
wireling = tinycircuits_wireling.Wireling()

# Toggle this variable to use the Light Sensor Wireling on a different port (0-3)
port = 0
wireling.selectPort(port)

# Create library object using our Bus I2C port
i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, 0x76) # our Wireling has an address of 0x76

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)

    time.sleep(2)