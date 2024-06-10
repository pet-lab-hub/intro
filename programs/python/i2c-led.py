from periphery import I2C
from time import sleep

i2c = I2C("/dev/i2c-2")

print (i2c)
while True:
  msgs = [I2C.Message(b'\x01\x01;', read=False)]
  i2c.transfer(0x0A, msgs)
  sleep(1)
  msgs = [I2C.Message(b'\x01\x00;', read=False)]
  i2c.transfer(0x0A, msgs)
  sleep(1)
i2c.close()
