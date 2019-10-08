#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
void *tmain(void *arg) {
char *msg = (char *) arg;
printf("[T] %s", msg) ;
pthread_exit((void *) strlen(msg));
}
int main(int argc, char **argv) {
pthread_t t;
int r;
void *res;
printf("Creating thread...\n");
r = pthread_create(&t, NULL, tmain, (void *) "Hello World!\n");
if (r != 0) {
perror("Unable to create thread");
exit(EXIT_FAILURE);
}
r = pthread_join(t, &res);
if (r != 0) {
perror("Unable to join thread");
exit(EXIT_FAILURE);
}
printf("Thread return: %ld\n", (long) res);
exit(EXIT_SUCCESS);
}
