#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
void *tmain(void *arg) {
long no = (long) arg;
printf("[T%ld] Hello world!\n", no);
return (void *) no;
}
int main(int argc, char **argv) {
pthread_t *tlist;
int count;
void *res;
if (argc != 2) {
fprintf(stderr, "Wrong arguments\n");
exit(EXIT_FAILURE);
}
count = atoi(argv[1]);
if ((tlist = calloc(count, sizeof(pthread_t))) == NULL) {
perror("Memory allocation failed");
exit(EXIT_FAILURE);
}
for(long i=0; i<count; i++) {
printf("Creating thread no %ld\n", i);
if (pthread_create(&tlist[i], NULL, tmain, (void *) i) != 0) {
perror("Unable to create thread");
}
}
for(long j=0; j<count; j++) {
printf("Trying to join thread no %ld\n", j);
if (pthread_join(tlist[j], &res) != 0) {
perror("Unable to join thread");
}
printf("Thread no %ld terminated with status: %ld\n",
j, (long) (long *) res);
}
free(tlist);
exit(EXIT_SUCCESS);
}
