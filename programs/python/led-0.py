# Referência:
# https://pypi.org/project/gpiod/
import gpiod
import time

from gpiod.line import Direction, Value

LED = 22

with gpiod.request_lines(
  "/dev/gpiochip2",
  consumer="blink",
  config={
    LED: gpiod.LineSettings(
      direction=Direction.OUTPUT, output_value=Value.ACTIVE
    )
  },
) as request:
  print("Blink")
  while True:
    request.set_value(LED, Value.ACTIVE)
    time.sleep(1)
    request.set_value(LED, Value.INACTIVE)
    time.sleep(1)