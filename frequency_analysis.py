from collections import Counter
import operator

cipherText = "ksjdiskdlekfabcdefghijklmnopqrstuvwxyzl"

cipher = Counter(cipherText)
print(cipher)

for ci in cipher:
    cipher[ci] /= len(cipher)

print(cipher)

# sorted_freq = sorted(cipher.items(), key=operator.itemgetter(1), reverse=True)
# print(sorted_freq)

print(cipher.keys())

