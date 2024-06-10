/*
 * Setar permissões da GPIO:
 * sudo chown caninos /dev/gpiochip*
 * sudo chmod g+rw /dev/gpiochip*
 *
 * Compilar:
 * gcc led.c -lgpiod -oled
 * 
 */
#include <gpiod.h>
#include <stdio.h>
#include <unistd.h>

#ifndef	CONSUMER
#define	CONSUMER "Consumer"
#endif

int main(int argc, char **argv) {
  char *nome_chip = "gpiochip2";
  unsigned int num_linha = 22;	// GPIOC22
  unsigned int valor;
  struct gpiod_chip *chip;
  struct gpiod_line *linha;
  int i;
 
  chip = gpiod_chip_open_by_name(nome_chip);
  linha = gpiod_chip_get_line(chip, num_linha);
  gpiod_line_request_output(linha, CONSUMER, 0);
  valor = 0;
  for (i = 20; i > 0; i--) {
    gpiod_line_set_value(linha, valor);
    printf("Saída %u na linha #%u\n", valor, num_linha);
    sleep(1);
    valor = !valor;
  }
  gpiod_line_release(linha);
  gpiod_chip_close(chip);
  return 0;
}
