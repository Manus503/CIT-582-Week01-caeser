


def encrypt(key,plaintext):
    ciphertext=""
    #encrypt
    for x in range(len(plaintext)):
        char = plaintext[x]
        ciphertext += chr((ord(char) + key - 65) % 26  + 65)        
    return ciphertext


def decrypt(key,ciphertext):
    plaintext=""
    #decript
    for x in range(len(ciphertext)):
        char = ciphertext[x]
        plaintext += chr((ord(char) - key - 65) % 26  + 65)        
    return plaintext
