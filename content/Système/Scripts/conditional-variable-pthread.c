#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
static long goods = 0;
static pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t avail = PTHREAD_COND_INITIALIZER;
void *producer(void *arg) {
while(1) {
sleep(1); // simulate time to produce
if (pthread_mutex_lock(&mutex) != 0) {
perror("Mutex lock failed");
exit(EXIT_FAILURE);
}
goods++;
if (pthread_mutex_unlock(&mutex) != 0) {
perror("Mutex unlock failed");
exit(EXIT_FAILURE);
}
if (pthread_cond_signal(&avail) != 0) {
perror("Condition signal failed");
exit(EXIT_FAILURE);
}
}
return NULL;
}
void *consumer(void *arg) {
while(1) {
if (pthread_mutex_lock(&mutex) != 0) {
perror("Mutex lock failed");
exit(EXIT_FAILURE);
}
while(goods == 0) {
if (pthread_cond_wait(&avail, &mutex) != 0) {
perror("Condition wait failed");
exit(EXIT_FAILURE);
}
}
while(goods > 0) {
goods--;
printf("Consuming...\n");
}
if (pthread_mutex_unlock(&mutex) != 0) {
perror("Mutex unlock failed");
exit(EXIT_FAILURE);
}
}
return NULL;
}
int main(int argc, char **argv) {
pthread_t t_producer, t_consumer;
printf("Creating producer thread...\n");
if (pthread_create(&t_producer, NULL, producer, NULL) != 0) {
perror("Unable to create producer thread");
exit(EXIT_FAILURE);
}
printf("Creating consumer thread...\n");
if (pthread_create(&t_consumer, NULL, consumer, NULL) != 0) {
perror("Unable to create consumer thread");
exit(EXIT_FAILURE);
}
if (pthread_join(t_producer, NULL) != 0) {
perror("Unable to join producer thread");
exit(EXIT_FAILURE);
}
if (pthread_join(t_consumer, NULL) != 0) {
perror("Unable to join consumer thread");
exit(EXIT_FAILURE);
}
exit(EXIT_SUCCESS);
}
