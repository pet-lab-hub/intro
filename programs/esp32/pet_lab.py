'''
ESP32 WiFi MQTT
Infraestrutura simplificada para uso de
conexão WiFi e serviços MQTT.

Autor:	Claudio Luis V. Oliveira
Autor:	Humberto A. P. Zanetti
Autor:	Peter Jandl Jr
Data:	2026-06-20
Versão:	1.0
'''
# Importações
import config
import network
from time import sleep
from machine import Pin
from umqtt.simple import MQTTClient

led = Pin(2, Pin.OUT)
led.off()

# Sinalização do Led
def led_flash(count):
    for n in range(count):
        led.value(not led.value())
        sleep(0.3)
    led.off()


# Inicializa interface Wi-Fi
def wifi_init():
    print("[Wifi] conectando", end='')
    try:
        station = network.WLAN(network.STA_IF)
        station.active(True)
        station.connect(config.WIFI_SSID, config.WIFI_PASS)
        while station.isconnected() == False:
            print(".", end='')
            pass
        led_flash(2)
        print('\n[WiFi] conexão OK')
        print(station.ifconfig())
        return station
    except Exception as e:
        print('\n[Wifi] erro na conexão:\n', e)
        raise  # Relança exceção para obter rastreio completo


# Conexão com broker MQTT para subscrição
def mqtt_client_sub(topic, callback = None):
    print("[MQTT] conectando...")
    try:
        client = MQTTClient(
            client_id=config.MQTT_CLIENT_ID,
            server=config.MQTT_SERVER,
            port=config.MQTT_PORT)
        client.set_callback(callback)
        client.connect()
        client.subscribe(topic)
        led_flash(4)
        print('[MQTT] Conectado ao broker %s no tópico %s'
              % (config.MQTT_SERVER, topic))
        return client
    except Exception as e:
        print('[MQTT] erro na conexão:\n', e)
        raise  # Relança exceção para obter rastreio completo


# Conexão com broker MQTT para publicação
def mqtt_client_pub():
    print("[MQTT] conectando...")
    try:
        client = MQTTClient(
            client_id=config.MQTT_CLIENT_ID,
            server=config.MQTT_SERVER,
            port=config.MQTT_PORT)
        client.connect()
        led_flash(2)
        print('[MQTT] Conectado ao broker %s'
              % (config.MQTT_SERVER))
        return client
    except Exception as e:
        print('[MQTT] erro na conexão:\n', e)
        raise  # Relança exceção para obter rastreio completo


# Publica valor, no tópico indicado, usando o cliente
def mqtt_publish(client, topic, value):
    client.publish(topic, value)
    led_flash(1)
    print("[MQTT] publicado\n\t%s em %s"
          % (value, topic))
