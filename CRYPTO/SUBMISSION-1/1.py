# Ceaser cipher
plaintext = str(input("Enter plain text [Give only capital letters ]: "))
key = int(input("Enter key value : "))
cipher_text = ""

for i in plaintext:
    plain_char_ascii = ord(i)
    added_ascii = plain_char_ascii+key
    if added_ascii > 90:
        added_ascii = (added_ascii%90)+64
    cipher_text += chr(added_ascii)

print(cipher_text)


cipher = str(input("Enter cipher text [caps only] :"))
key = int(input("Enter key value : "))
plain_text =""
for i in cipher:
    cipher_char_ascii = ord(i)
    added_ascii = cipher_char_ascii-key
    if added_ascii < 65:
        added_ascii = 90-(64-added_ascii)
    plain_text += chr(added_ascii)

print(plain_text)



