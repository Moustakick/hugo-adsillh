/*
> gcc -Wall pipe_half-duplex.c -o pipe_half-duplex
> ./pipe_half-duplex
I am your father
*/


#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#define BUFMAX 256

int main () {
  char *buffer[BUFMAX];
  pid_t pid;
  int n, fds[2];

  if (pipe(fds) == -1) {
    perror("Unable to create pipe");
  }

  pid = fork();

  if (pid == -1) {
    perror("Unable to fork");
  }
  else if (pid > 0) { /* parent */
    if (close(fds[0]) == -1) {
      perror("Unable to close pipe from parent");
    }
    write(fds[1], "I am your father\n", 17);
  }
  else { /* child */
    if (close(fds[1]) == -1) {
      perror("Unable to close pipe from child");
    }
    n = read(fds[0], buffer, BUFMAX);
    write(STDOUT_FILENO, buffer, n);
  }

  exit(EXIT_SUCCESS);
}
