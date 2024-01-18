/* vsrv.c */
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#define MAXBUF 768
#define M 512
char s[MAXBUF];
void mystrcpy(char *dest, char *src) {
  int i, l = strlen(src);
  for (i=0; src[i] != '\0' && i<MAXBUF; i++)
    dest[i] = src[i];
  dest[i]='\0';
}
void myoutput(char *str) {
  char msg[M];
  printf("&msg=0x%08x\n",&msg);
  mystrcpy(msg, str);
  printf("%s\n", msg);
}
int main(void) {
  setvbuf(stdout, NULL, _IONBF, 0);
  myoutput("hello");
  while (fgets(s, MAXBUF, stdin) != NULL) {
    myoutput(s);
  }
}
