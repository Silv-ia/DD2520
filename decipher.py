cipher = "pm aolylpzhufaopunavillujyfwalkaoludlzovbskuvailbzpunhjhlzhyjpwoly"
key = 7
# e -> l. fghijkl

alphabet=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
          'q','r','s','t','u','v','w','x','y','z', ' ')

def decrypt(key, cipher):
    plaintext = ""  

    for c in cipher:
        plaintext += alphabet[(alphabet.index(c)-key) % 26]
    return plaintext

print(decrypt(key, cipher))