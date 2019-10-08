#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#define LOOP_COUNT 100000000
#define THREADS_COUNT 2
static long glob = 0;
static pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
void *tmain(void *arg) {
long loc;
for(long i = 0; i< LOOP_COUNT; i++) {
if (pthread_mutex_lock(&mutex) != 0) {
perror("Mutex lock failed");
exit(EXIT_FAILURE);
}
loc = glob;
loc++;
glob = loc;
if (pthread_mutex_unlock(&mutex) != 0) {
perror("Mutex unlock failed");
exit(EXIT_FAILURE);
}
}
return NULL;
}
int main(int argc, char **argv) {
pthread_t tlist[THREADS_COUNT];
int r;
void *res;
for(int i=0; i<THREADS_COUNT; i++) {
printf("Creating thread %d...\n", i);
r = pthread_create(&tlist[i], NULL, tmain, NULL);
if (r != 0) {
perror("Unable to create thread");
exit(EXIT_FAILURE);
}
printf("Thread %d running...\n", i);
}
for(int i=0; i<THREADS_COUNT; i++) {
printf("Joining thread %d...\n", i);
r = pthread_join(tlist[i], &res);
if (r != 0) {
perror("Unable to join thread");
exit(EXIT_FAILURE);
}
printf("Thread %d terminated...\n", i);
}
printf("%ld =? %ld\n", glob, (long) THREADS_COUNT * (long) LOOP_COUNT);
exit(EXIT_SUCCESS);
}
