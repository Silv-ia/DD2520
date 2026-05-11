## xor two equal length buffers

inp1 = "1c0111001f010100061a024b53535009181c"
inp2 = "686974207468652062756c6c277320657965"

cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
key = "d"*len(cipher)

def xor(buf1, buf2):
    b1 = bytes.fromhex(buf1)
    b2 = bytes.fromhex(buf2)

    return bytes(x^y for x,y in zip(b1,b2))

print(xor(inp1,inp2))
print(xor(cipher, key))