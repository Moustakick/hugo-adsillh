#include <errno.h>
#include <fcntl.h>
#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main(int argc, char **argv)
{
  int i;
  sem_t *sem;
  if (argc != 2) {
    fprintf(stderr,"Usage: %s sem_name\n", argv[0]);
    exit(EXIT_FAILURE);
  }
  sem = sem_open(argv[1], O_RDWR | O_CREAT, 0666, 1);
  if (sem == SEM_FAILED) {
    perror("Unable to open semaphore");
    exit(EXIT_FAILURE);
  }
  fprintf(stdout,"[%d] Sempahore %s created\n", getpid(), argv[1]);
  for (i = 0; i < 3;  i ++) {
    fprintf(stdout,"[%d] waiting...\n", getpid());
    sem_wait(sem);
    fprintf(stdout,"\t[%d] semaphore locked\n", getpid());
    sleep(4);
    fprintf(stdout,"\t[%d] semaphore released\n", getpid());
    sem_post(sem);
  sleep(2);
  }
  return EXIT_SUCCESS;
}
