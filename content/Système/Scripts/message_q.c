#include <fcntl.h>
#include <mqueue.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main (int argc, char **argv)
{
mqd_t mq;
int  priority;
if (argc != 4) {
  fprintf(stderr, "Usage: %s queue priority message\n", argv[0]);
  exit(EXIT_FAILURE);
}
if (sscanf(argv[2],"%d", &priority) != 1) {
  fprintf(stderr, "Invalid priority: %s\n", argv[2]);
  exit(EXIT_FAILURE);
}
if ((mq = mq_open(argv[1], O_WRONLY | O_CREAT, 0644, NULL)) == (mqd_t) -1) {
  perror("Opening message queue failed");
  exit(EXIT_FAILURE);
}
if (mq_send(mq, argv[3], strlen(argv[3]), priority) == -1) {
  perror("Unable to send message to queue");
exit(EXIT_FAILURE);
}
if (mq_close(mq) == -1) {
  perror("Unable to close queue");
  exit(EXIT_FAILURE);
}
return EXIT_SUCCESS;
}
