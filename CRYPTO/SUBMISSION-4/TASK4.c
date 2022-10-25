#include <stdio.h>
#include <openssl/bn.h>
#define NBITS 256

void hex_to_string(char* msg, char* hex)
{
   int hex_sz = 0;
   while(hex[hex_sz]){
     hex_sz+=1;
   }
   int msg_sz = (hex_sz/2)+1;
   if (hex_sz % 2 != 0 || hex_sz/2 >= msg_sz)
      return;

   for (int i = 0; i < hex_sz; i+=2)
   {
      uint8_t msb = (hex[i+0] <= '9' ? hex[i+0] - '0' : (hex[i+0] & 0x5F) - 'A' + 10);
      uint8_t lsb = (hex[i+1] <= '9' ? hex[i+1] - '0' : (hex[i+1] & 0x5F) - 'A' + 10);
      msg[i / 2] = (msb << 4) | lsb;
      msg[i+1] = '\0';
   }
}
void printBN(char*msg, BIGNUM*a) {
  /* Use BN_bn2hex(a) for hex string
     Use BN_bn2dec(a) for decimal string*/
  char* number_str = BN_bn2hex(a);
  char res[100];
  hex_to_string(res,number_str);
  printf("%s in hex = %s\n",msg,number_str);
  printf("%s in ascii = %s\n",msg,res);
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
  // Initialize
  BN_hex2bn(&n,"DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
  BN_hex2bn(&d,"74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");
  BN_hex2bn(&enc,"8C0F971DF2F3672B28811407E2DABBE1DA0FEBBBDFC7DCB67396567EA1E2493F"
      );
  // Decryption
  BN_mod_exp(dec,enc,d,n,ctx);
  printBN("Decrypted Message",dec);
  return 0;
}
