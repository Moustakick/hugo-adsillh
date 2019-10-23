#include <fcntl.h>
#include <mqueue.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main (int argc, char * argv[])
{
  int    n;
  mqd_t  mq;
  struct mq_attr attr;
  char * buffer = NULL;
  unsigned int priority;
  if (argc != 2) {
    fprintf(stderr,"Usage: %s queue\n", argv[0]);
    exit(EXIT_FAILURE);
  }
  if ((mq = mq_open(argv[1], O_RDONLY)) == (mqd_t) -1) {
    perror("Opening message queue failed");
    exit(EXIT_FAILURE);
  }
  if (mq_getattr(mq, &attr) != 0) {
    perror("Unable to get message queue attributes");
    exit(EXIT_FAILURE);
  }
  if ((buffer = (char *) malloc(attr.mq_msgsize)) == NULL) {
    perror("Unable to allocate memory");
    exit(EXIT_FAILURE);
  }
  if ((n = mq_receive(mq, buffer, attr.mq_msgsize, &priority)) < 0) {
    perror("Unable to receive message from queue");
    exit(EXIT_FAILURE);
  }
  if (mq_close(mq) == -1) {
    perror("Unable to close queue");
    exit(EXIT_FAILURE);
  }
  fprintf(stdout,"[%d] %s\n", priority, buffer);
  free(buffer);
  return EXIT_SUCCESS;
}
