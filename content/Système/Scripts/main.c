/* main.c */
#include <stdlib.h>
#include "libfoo.h"
#include "libbar.h"
int main() {
  foo("foo");
  bar("bar");
  exit(EXIT_SUCCESS);
}
