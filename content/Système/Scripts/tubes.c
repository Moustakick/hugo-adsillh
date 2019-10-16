#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

#define PAGER "less"

int main () {
  pid_t pid;
  int status, fds[2];
  FILE *fdout;
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
    fdout = fdopen(fds[1], "w");

    if (fdout == NULL) {
      perror("Unable to open pipe as a stream for writing");
    }

    for(int i=1; i<=1000; i++) {
      fprintf(fdout, "%d\n", i);
    }
    fclose(fdout);
    wait(&status);
  }
  else { /* child */
    if (close(fds[1]) == -1) {
      perror("Unable to close pipe from child");
    }
    if (dup2(fds[0], STDIN_FILENO) != STDIN_FILENO) {
      perror("Unable to duplicate stdin file descriptor");
    }
    close(fds[0]);
    execlp(PAGER, PAGER, NULL);
  }
  exit(EXIT_SUCCESS);
}
