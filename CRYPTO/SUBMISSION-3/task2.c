/* task2.c */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define KEYSIZE 16
void main() {
  int i, j;
  FILE *f;
  char key[KEYSIZE];
  int value1, value2;
  value1 = 1524013729;
  value2 = 1524020929;
  f = fopen("keys.txt", "w");
  for (j = value1; j <= value2; j++) {
    srand (j);
    for (i = 0; i< KEYSIZE; i++) {
      key[i] = rand()%256;
      fprintf(f, "%.2x", (unsigned char)key[i]);
    }
    fprintf(f,"\n");
  }
}
