#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>
int main (int argc, char **argv)
{
  int fd;
  long int *counter;


  if (argc != 2) {
    fprintf(stderr,"Usage: %s segment\n", argv[0]);
    exit(EXIT_FAILURE);
  }
  if ((fd = shm_open(argv[1], O_RDWR | O_CREAT, 0600)) == -1) {
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
  for(long int i=0; i< 10000000; i++) {
    (*counter)++;
  }
  fprintf(stdout,"counter=%ld\n", (*counter));
  return EXIT_SUCCESS;
}
