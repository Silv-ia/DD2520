from collections import Counter
import operator

cipherText = "oxmanaosnflsåwöwkdölsnajfksjdiskdlekfabcdefghijklmnopqrstuvwxyzl"

cipher = Counter(cipherText)
print(cipher)

print(cipher.keys())

