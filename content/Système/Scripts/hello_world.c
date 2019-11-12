#include <unistd.h>
#include <stdlib.h>

int main() {
  write(1,  "Hello\n", 6);
  exit(EXIT_SUCCESS);
}
