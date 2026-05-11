from collections import Counter

chars = (
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    '0','1','2','3','4','5','6','7','8','9'
)

input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

cipher = bytes.fromhex(input)
print(cipher)

# 3 -> 0110
# e -> 1110
# k -> 1000 -> 8.

# 3 -> 0110
# t -> 

def xor(b1, b2):
    return bytes(x^y for x,y in zip(b1,b2))

with open("cryptopals4.txt") as file:
    for line in file:
        for c in range(256):
            key = bytes([c])*len(input)
            # print("Key:", key)
            # print(xor(cipher, key))
        print(line.rstrip())

# print(xor(cipher, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX".encode()))

# Key: b'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# b"Cooking MC's like a pound of bacon"