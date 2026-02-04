## a=0, b=1, etc.
# Encryption: C = (P + K) mod 26
# Decryption: P = (C - K) mod 26
# Each individual character is shifted differently. 

# 

cipher = ""
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# [index+1] -- to find the corresponding. plain+key % 26 - 1, something. then decr, 
