#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
#include <stdio.h>

void sigusr1_trigger() {
	write(1, "SIGUSR1 received\n", 17);
}

int main () {
	if (signal(SIGINT, sigusr1_trigger) == SIG_ERR) {
		perror("Unable to catch SIGUSR1\n");
	}
	else {
		printf("SIGUSR1 is catched on process with PID=%d\n", getpid());
	}
	for(;;) {
		sleep(10);
	}
}
