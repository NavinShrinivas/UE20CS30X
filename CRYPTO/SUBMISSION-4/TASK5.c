#include <stdio.h>
#include <openssl/bn.h>
#define NBITS 256

void alphabets_to_hexcode(char* string, char* res){
  int i = 0;
  int out = 0;
  while(string[i]) {
    sprintf((char*)(res+out),"%02X",string[i]);
    out+=2;
    i++;
  }
}

void printBN(char*msg, BIGNUM*a) {
  /* Use BN_bn2hex(a) for hex string
     Use BN_bn2dec(a) for decimal string*/
  char* number_str = BN_bn2hex(a);
  printf("%s %s\n",msg,number_str);
  OPENSSL_free(number_str);
}
int main() {
  BN_CTX *ctx = BN_CTX_new();
  BIGNUM *m = BN_new();
  BIGNUM *n = BN_new();
  BIGNUM *d = BN_new();
  BIGNUM *sign = BN_new();
  // Initialize
  char hex_code[1000];
  char plain_text[] = "I owe you $2000";
  alphabets_to_hexcode(plain_text, hex_code);
  BN_hex2bn(&m,hex_code);
  BN_hex2bn(&n,"DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
  BN_hex2bn(&d,"74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");
  // Signing
  BN_mod_exp(sign,m,d,n,ctx);
  printBN("Sign =",sign);
  return 0;
}
