from machine import Pin, I2C, SoftI2C
from time import sleep
import config, pet_lab
import json
import ahtx0
import bmp280

# Config & Owmo setup
MQTT_TOPIC_READ = config.MQTT_CLIENT_ID + '/reading'
MQTT_TOPIC_AHT = config.MQTT_CLIENT_ID + '/sensor/aht20'
MQTT_TOPIC_BMP = config.MQTT_CLIENT_ID + '/sensor/bmp280'

# I2C for the ESP32
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Create the sensor object using I2C
bmp = bmp280.BMP280(i2c, 0x77)
bmp.oversample_setting = 3
aht20 = ahtx0.AHT20(i2c)

# Rotina principal
estacao = None
cliente = None
try:
    estacao = pet_lab.wifi_init()
    cliente = pet_lab.mqtt_client_pub()
    reading = 0
    while True:
        reading += 1
        pet_lab.mqtt_publish(cliente,
                             MQTT_TOPIC_READ,
                             str(reading))
        if reading % 2 == 0:
            print("BMP280")
            dicio = {
                'temperatura' : str(bmp.temperature),
                'pressao' : str(bmp.pressure/100)
                    }
            pet_lab.mqtt_publish(cliente,
                         MQTT_TOPIC_BMP,
                         json.dumps(dicio))
#             pet_lab.mqtt_publish(cliente,
#                          MQTT_TOPIC_BMP + '/temp',
#                          str(bmp.temperature))
#             pet_lab.mqtt_publish(cliente,
#                          MQTT_TOPIC_BMP + '/press',
#                          str(bmp.pressure/100))
        else:            
            print("AHT20")
            pet_lab.mqtt_publish(cliente,
                         MQTT_TOPIC_AHT + '/temp',
                         str(aht20.temperature))
            pet_lab.mqtt_publish(cliente,
                         MQTT_TOPIC_AHT + '/umid',
                         str(aht20.relative_humidity))
        sleep(30)

except KeyboardInterrupt:
    pass
finally:
    if cliente != None: cliente.disconnect()
    if estacao.isconnected():
        estacao.disconnect()
    estacao.active(False)
    print("Fim.")
