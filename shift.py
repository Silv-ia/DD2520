## a=0, b=1, etc.
# Encryption: C = (P + K) mod 26
# Decryption: P = (C - K) mod 26
# Each individual character is shifted differently. 

import matplotlib.pyplot as plt
import numpy as np

# i mod key_len =- 0, 1, 2, ..., n-1
# this way get all the streams to analyse

cipher = "vycrthkjzghkprlsjiktipgrelrtuivkftwcizqpegqmcgrqwkciasarptusukdgbspuquhfgmcgtbfjmhhvcgnnmcivrwxfvycqhcmjygxypfuaxrivyqes"
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# [index+1] -- to find the corresponding. plain+key % 26 - 1, something. then decr, 

def stream(cipher, key_len):
    streams = [""] * len(cipher)/key_len
    

def offset(cipher):
    n = len(cipher)
    counts = []
    
    # set the n to maximum key length, maybe 50?
    for shift in range(1, 30):
        count = 0

        # cipher[i] is the shifted cipher
        # cipher[i+shift] is the original one. 
        # c0 c1 c2 c3 c4 | original starts on the shift index
        #    c0 c1 c2 c3 | shifted starts on index 0 of original.
        # we end on n-shift
        for i in range(n-shift):
            if cipher[i] == cipher[i+shift]:
                count += 1
        counts.append(count)

    return counts
             
counts = offset(cipher)
print(counts)
plt.figure(figsize=(30, 4))
plt.bar(range(len(counts)), counts)
plt.xticks(range(len(counts)))

#plt.figure(figsize=(18, 4))
#plt.plot(counts)
plt.show() 
