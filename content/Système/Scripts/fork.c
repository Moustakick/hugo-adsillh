#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main (int argc, char **argv) {
pid_t pid;
printf("Starting process with PID=%d\n", getpid());
pid = fork();
if (pid < 0) {
perror("Unable to fork");
}
else if (pid == 0) {
printf("Starting child with PID=%d (my parent PID=%d)\n", getpid(), getppid());
}
else {
printf("Still in process with PID=%d\n", getpid());
}
printf("Finishing process with PID=%d\n", getpid());
exit(EXIT_SUCCESS);
}
