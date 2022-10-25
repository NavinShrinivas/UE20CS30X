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
  char* number_str = BN_bn2hex(a);
  printf("%s %s\n",msg,number_str);
  OPENSSL_free(number_str);
}
int main() {
  BN_CTX *ctx = BN_CTX_new();
  BIGNUM *m = BN_new();
  BIGNUM *e = BN_new();
  BIGNUM *n = BN_new();
  BIGNUM *d = BN_new();
  BIGNUM *enc = BN_new();
  BIGNUM *dec = BN_new();

  char string[100];
  char res[100];
  printf("Enter string for enc : ");
  scanf("%[^\n]%*c",string);
  alphabets_to_hexcode(string,res);

  printf("Plain text in hex code : ");

  int out_print = 0;
  while(res[out_print]){
    printf("%c", res[out_print]);
    out_print++;
  }
  printf("\n");

  // Initialize
  BN_hex2bn(&m,res);
  BN_hex2bn(&e,"010001");
  BN_hex2bn(&n,"DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
  BN_hex2bn(&d,"74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");
  // Encryption
  BN_mod_exp(enc,m,e,n,ctx);
  printBN("Encrypted Message =",enc);
  // Decryption
  BN_mod_exp(dec,enc,d,n,ctx);
  printBN("Decrypted Message =",dec);
  return 0;
}
