def check_key_validity ( key , alphabet ) :
   if len ( key ) != len ( alphabet ) :
       return false
   if len ( list ( key ) ) != len ( set ( key ) ) :
        return false
   return True


def generate_key ( alphabet_string ) :
    import random as r
    l = list ( alphabet_string )
    r.shuffle ( l )
    return ''.join ( l )

def encrypt(srn, key):
    fd = open(srn+".txt", "r")
    file_content = str(fd.read())
    fd.close()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_text = ''

    for i in range(0,len(file_content)):
        letter = file_content[i]
        if letter not in alphabet:
            cipher_text += letter
        else:
            cipher_text += key[alphabet.index(letter)]
    fd = open(srn+"_enc.txt", "w+")
    fd.write(str(cipher_text))
    fd = open(srn+"_enc.txt", "r")
    print(fd.read())
    return

def decrypt(srn, key):
    fd = open(srn+"_enc.txt", "r")
    file_content = str(fd.read())
    fd.close()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plain_text = ""

    for i in range(0,len(file_content)):
        letter = file_content[i]
        if letter not in key:
            plain_text += letter
        else:
            plain_text += alphabet[key.index(letter)]
    fd = open(srn+"_dec.txt", "w+")
    fd.write(str(plain_text))
    fd = open(srn+"_dec.txt", "r")
    print(fd.read())
    return





