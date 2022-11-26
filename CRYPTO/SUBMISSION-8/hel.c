#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <openssl/sha.h>
#include <string.h>
int main(int argc, const char *argv[])
{
  int i;
  unsigned char buffer[SHA256_DIGEST_LENGTH];
  SHA256_CTX c;
  char hex[] = "17a3cc37a8d2444cd9ecf81bc3b79760bd014de88105890765ab21490f8924e6";
  char subbuffer[9];
  SHA256_Init(&c);
  for (i = 0; i < 64; i++)
    SHA256_Update(&c, "*", 1);
  // MAC of the original message M (padded)
  for (i = 0; i < 8; i++)
  {
    strncpy(subbuffer, hex + i * 8, 8);
    subbuffer[8] = '\0';
    c.h[i] = htole32(strtol(subbuffer, NULL, 16));
    c.h[i] = htole32(strtol(subbuffer, NULL, 16));
  }
  // Append additional message
  SHA256_Update(&c, "&download=secret.txt", 20);
  SHA256_Final(buffer, &c);
  for (i = 0; i < 32; i++)
  {
    printf("%02x", buffer[i]);
  }
  printf("\n");
  return 0;
}
