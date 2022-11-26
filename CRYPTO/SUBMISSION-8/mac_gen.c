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
  SHA256_Init(&c);
  SHA256_Update(&c, "123456:myname=pes2ug20cs237&uid=1001&lstcmd=1\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x68""&download=secret.txt",64+20);
  SHA256_Final(buffer, &c);
  for (i = 0; i < 32; i++)
  {
    printf("%02x", buffer[i]);
  }
  printf("\n");
  return 0;
}
