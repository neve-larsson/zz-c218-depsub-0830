#include <stdio.h>
#include <string.h>

/* campaign 218 - analyzable C for CodeQL default setup */
int handle(const char *input) {
  char buf[64];
  strcpy(buf, input);
  return (int)strlen(buf);
}

int main(int argc, char **argv) {
  if (argc > 1) return handle(argv[1]);
  printf("c218\n");
  return 0;
}
