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
  int fd;
  long int *counter;

  //Semaphore 1er arg
  //SHM 2nd arg


  if (argc != 3) {
    fprintf(stderr,"Usage: %s sem_name\n", argv[0]);
    fprintf(stderr,"Usage: %s segment\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  sem = sem_open(argv[1], O_RDWR | O_CREAT, 0666, 1);

  if (sem == SEM_FAILED) {
    perror("Unable to open semaphore");
    exit(EXIT_FAILURE);
  }

  if ((fd = shm_open(argv[2], O_RDWR | O_CREAT, 0600)) == -1) {
    perror("Opening shared memory segment failed");
    exit(EXIT_FAILURE);
  }
  if (ftruncate(fd, sizeof(long int)) != 0) {
    perror("Unable to truncate shared memory segment");
    exit(EXIT_FAILURE);
  }
  counter = mmap(NULL, sizeof(long int), PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
  if (counter == MAP_FAILED) {
    perror("Unable to map shared memory segment");
    exit(EXIT_FAILURE);
  }


  fprintf(stdout,"[%d] Sempahore %s created\n", getpid(), argv[1]);
    fprintf(stdout,"[%d] waiting...\n", getpid());
    sem_wait(sem);
    fprintf(stdout,"\t[%d] semaphore locked\n", getpid());
    for(long int i=0; i< 100000000; i++) {
      (*counter)++;
    }
    fprintf(stdout,"\t[%d] semaphore released\n", getpid());
    sem_post(sem);
    fprintf(stdout,"counter=%ld\n", (*counter));

  return EXIT_SUCCESS;
}
