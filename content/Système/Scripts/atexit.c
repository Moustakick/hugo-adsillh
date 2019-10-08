#include <stdio.h>
#include <stdlib.h>
void trigger_exit(void) {
printf("Invoking exit handler!\n");
}
int main (int argc, char **argv) {
printf("Invoking main()...\n");
if (atexit(trigger_exit) == 0) {
printf("Exit handler successfully registered\n");
}
else {
printf("Failed to register exit handler\n");
exit(EXIT_FAILURE);
}
exit(EXIT_SUCCESS);
}
