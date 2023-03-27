#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/msg.h>

struct mesg_buffer {
  long mesg_type;
  char mesg_text[10000];
} message;

int main() {
  int msgid = msgget(77777, 0666 | IPC_CREAT);

  msgrcv(msgid, &message, sizeof(message), 1, 0);

  FILE *f = fopen("file.html", "w");
  if (f == NULL) {
    printf("Error opening file!\n");
    exit(1);
  }

  fprintf(f, "%s", message.mesg_text);

  fclose(f);

  // to destroy the message queue
  msgctl(msgid, IPC_RMID, NULL);

  return 0;
}
