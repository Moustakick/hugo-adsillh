#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
int main(int argc, char **argv) {
  int v = 0;
  if (argc > 1) {
    v = atoi(argv[1]);
  }
  printf("%.0f\n", pow(v, 2));
  exit(EXIT_SUCCESS);
}
