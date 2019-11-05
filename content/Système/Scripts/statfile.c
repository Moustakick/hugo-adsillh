#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
int main(int argc, char *argv[]) {
int i;
struct stat statbuf;
for (i = 1; i < argc; i++) {
  printf("%s: ", argv[i]);
  if (lstat(argv[i], &statbuf) < 0) {
    perror("Unable to get stats");
    continue;
  }
  if (S_ISREG(statbuf.st_mode)) {
    printf("regular\n");
  }
  else if (S_ISDIR(statbuf.st_mode)) {
    printf("directory\n");
  }
  else if (S_ISCHR(statbuf.st_mode)) {
    printf("character special\n");
  }
  else if (S_ISBLK(statbuf.st_mode)) {
    printf("block special\n");
  }
  else if (S_ISFIFO(statbuf.st_mode)) {
    printf("fifo\n");
  }
  else if (S_ISLNK(statbuf.st_mode)) {
    printf("symbolic link\n");
  }
  else if (S_ISSOCK(statbuf.st_mode)) {
    printf("socket\n");
  }
  else {
    printf("*unknown*\n");
  }
}
exit(EXIT_SUCCESS);
}
