#include <stdio.h>
#include <unistd.h>
#include "i2c.h"

int main() {
  struct I2cDevice dev;
  dev.filename = "/dev/i2c-2";
  dev.addr = 0x0A;
  int res = i2c_start(&dev);
  if (!res) {
    printf("i2c Led\n");
    uint8_t led[] = {1, 1, ';'};
    for (size_t i = 0; i < 10; i++) {
      led[1] = 1;
      i2c_write(&dev, led, sizeof(led));
      sleep(1);
      led[1] = 0;
      i2c_write(&dev, led, sizeof(led));
      sleep(1);
    }
    i2c_stop(&dev);
  }
  else {
    printf("Erro: Device i2c não encontrado!\n");
  }
  return res;
}
