# https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/
# https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
# http://www.steves-internet-guide.com/mosquitto_pub-sub-clients/

import pet_lab, config
from machine import Pin


def obter_mensagem(topico, mensagem):
    print(topico, mensagem)
    if mensagem in [b'ligar', b'on', b'1']:
        relay.value(1)
    elif mensagem in [b'desligar', b'off', b'0']:
        relay.value(0)


# Define dispositivo relay
relay = Pin(22, Pin.OUT)

# Rotina principal
estacao = None
cliente = None
try:
    estacao = pet_lab.wifi_init()
    cliente = pet_lab.mqtt_client_sub(
        config.MQTT_CLIENT_ID + '/atuador/relay',
        callback=obter_mensagem)
    while True:
        cliente.wait_msg()

except KeyboardInterrupt:
    pass
finally:
    if cliente != None: cliente.disconnect()
    if estacao.isconnected():
        estacao.disconnect()
    estacao.active(False)
    print("Fim.")
