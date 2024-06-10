https://github.com/vsergeev/python-periphery
https://pypi.org/project/python-periphery/
https://python-periphery.readthedocs.io/en/latest/index.html

from periphery import GPIO
from time import sleep

led = GPIO ('/dev/gpiochip2', 22, 'out')

while True:
  led.write(True)
  sleep(1)
  led.write(False)
  sleep(1)
  