## Find the frequencies of the ciphertext

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# cipher text, and how many times each character occurs
cipherText = "ksjdiskdlekfabcdefghijklmnopqrstuvwxyzl"

cipherAlphabet = {}
for c in cipherText:
    if c in cipherAlphabet:
        cipherAlphabet[c] += 1
    else:
        cipherAlphabet[c] = 1

print(cipherAlphabet)

# make into char array
cipherArray = list(cipherText)

cipherLen = len(cipherText)
print(cipherLen)

# alphabet
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# frequency of cipher
# cipherFrequency = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,
#             'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

cipherFrequency = {}
for ci in cipherAlphabet.keys():
    print(ci)
    cipherFrequency[ci] = cipherAlphabet[ci]/cipherLen

print(cipherFrequency)

freqEnglish = {'e': 0.12702, 't': 0.09056, 'a': 0.08167, 'o': 0.07507, 'i': 0.06966, 'n': 0.06749, 
               's': 0.06327, 'h': 0.06094, 'r': 0.05987, 'd': 0.04253, 'l': 0.04025, 'c': 0.02782,
               'u': 0.02758, 'm': 0.02406, 'w': 0.02360, 'f': 0.02228, 'g': 0.02015, 'y': 0.01974, 
               'p': 0.01929, 'b': 0.01492, 'v': 0.00978, 'k': 0.00772, 'j': 0.00153, 'x': 0.00150,
               'q': 0.00095, 'z': 0.00074}


### plot the frequencies

# sort cipher freq alphabet
dict(sorted(cipherFrequency))

# x-axis, characters
x_cipher = np.array(list(cipherFrequency.keys()))
x_english = np.array(list(freqEnglish.keys()))

# y-axis, their freq
y_cipher = np.array(cipherFrequency.values())
y_english = np.array(freqEnglish.values())


fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Frequency analysis (eng then cipher)')
ax1.plot(x_english, y_english)
ax2.plot(x_cipher, y_cipher)