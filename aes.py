## Take stdin
import sys
import numpy as np

# input = sys.stdin.read()
input = "a8f9e7dc8b782f618ade628f7b7c83421829f9eba8e8d8c8b72a7f7e7d6c2b38"

## input is a whole string, partitions into key and plaintext.
key = input[:32] # list()
plaintext = input[32:]
# column-major. 

# key and plaintext are both turned into lists, with two char per item, hex.
key_hex = [key[i:i+2] for i in range(0, len(key), 2)]
# print(key_hex)
plain_hex = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]

##### constants
s_box = (
#    0     1    2    3    4    5    6    7    8    9    a    b    c    d   e    f
    '63','7c','77','7b','f2','6b','6f','c5','30','01','67','2b','fe','d7','ab','76',
    'ca','82','c9','7d','fa','59','47','f0','ad','d4','a2','af','9c','a4','72','c0',
    'b7','fd','93','26','36','3f','f7','cc','34','a5','e5','f1','71','d8','31','15',
    '04','c7','23','c3','18','96','05','9a','07','12','80','e2','eb','27','b2','75',
    '09','83','2c','1a','1b','6e','5a','a0','52','3b','d6','b3','29','e3','2f','84',
    '53','d1','00','ed','20','fc','b1','5b','6a','cb','be','39','4a','4c','58','cf',
    'd0','ef','aa','fb','43','4d','33','85','45','f9','02','7f','50','3c','9f','a8',
    '51','a3','40','8f','92','9d','38','f5','bc','b6','da','21','10','ff','f3','d2',
    'cd','0c','13','ec','5f','97','44','17','c4','a7','7e','3d','64','5d','19','73',
    '60','81','4f','dc','22','2a','90','88','46','ee','b8','14','de','5e','0b','db',
    'e0','32','3a','0a','49','06','24','5c','c2','d3','ac','62','91','95','e4','79',
    'e7','c8','37','6d','8d','d5','4e','a9','6c','56','f4','ea','65','7a','ae','08',
    'ba','78','25','2e','1c','a6','b4','c6','e8','dd','74','1f','4b','bd','8b','8a',
    '70','3e','b5','66','48','03','f6','0e','61','35','57','b9','86','c1','1d','9e',
    'e1','f8','98','11','69','d9','8e','94','9b','1e','87','e9','ce','55','28','df',
    '8c','a1','89','0d','bf','e6','42','68','41','99','2d','0f','b0','54','bb','16',
)



r_con = (
    '01', '02', '04', '08', '10', '20', '40', '80', '1B', '36'
)

##### Key expansion 

# calls rotWord and subBytes
def keySchedule(key):
    ind1 = 0
    ind2 = 12
    rind = 0
    key_count = 0

    while key_count < 10:
        key_count += 1
        # print(key_count)
        key = rotWord(ind2, key)
        ind2 += 4
        # print(key)
        key = subBytesKey(ind2, key)
        # print(key)

        key[ind2] = '%02x' % (int(key[ind1], 16)^int(key[ind2], 16)^int(r_con[rind], 16))
        key[ind2+1] = '%02x' % (int(key[ind1+1], 16)^int(key[ind2+1], 16))
        key[ind2+2] = '%02x' % (int(key[ind1+2], 16)^int(key[ind2+2], 16))
        key[ind2+3] = '%02x' % (int(key[ind1+3], 16)^int(key[ind2+3], 16))
        # print(key)
        ind1 += 4
        rind += 1
        for i in range(3):
            key.append('%02x' % (int(key[ind1], 16)^int(key[ind2], 16)))
            key.append('%02x' % (int(key[ind1+1], 16)^int(key[ind2+1], 16)))
            key.append('%02x' % (int(key[ind1+2], 16)^int(key[ind2+2], 16)))
            key.append('%02x' % (int(key[ind1+3], 16)^int(key[ind2+3], 16)))
            ind1 += 4
            ind2 += 4
        # print(key)
        

    # keys = []
    # s = str.join(key)
    # keys = [s[i:i+32] for i in range(0, len(s), 32)]
    return key

# creates new column
def rotWord(index, key):
    
    key.append(key[index+1])
    key.append(key[index+2])
    key.append(key[index+3])
    key.append(key[index])

    return key

def subBytesKey(index, key):

    # x, row
    # y, col
    # acces the first and second letter for coordinates
    key[index] = s_box[int(key[index][0], 16)*16 + int(key[index][1], 16)]
    key[index+1] = s_box[int(key[index+1][0], 16)*16 + int(key[index+1][1], 16)]
    key[index+2] = s_box[int(key[index+2][0], 16)*16 + int(key[index+2][1], 16)]
    key[index+3] = s_box[int(key[index+3][0], 16)*16 + int(key[index+3][1], 16)]
    # print(key)
    
    return key

#####

##### rounds

def round(roundkey, plaintext):
    return 0

def subBytes(plain):
    cipher = list()

    for i in range(len(plain)):
        cipher.append(s_box[int(plain[i][0], 16)*16 + int(plain[i][1], 16)])
        # print(cipher)
    print(cipher)
    return cipher

def shiftRow(cipher):
    cipher[1],cipher[5], cipher[9], cipher[13] = cipher[5], cipher[9], cipher[13], cipher[1]
    cipher[2], cipher[6], cipher[10], cipher[14] = cipher[10], cipher[14], cipher[2], cipher[6]
    cipher[3], cipher[7], cipher[11], cipher[15] = cipher[15], cipher[3], cipher[7], cipher[11]

    return cipher

def mixColumn():
    return 0

def addRoundKey(roundkey, plaintext):
    cipher = list()
    # print(roundkey)
    # print(plaintext)
    for i in range(len(roundkey)):
        cipher.append('%02x' % (int(roundkey[i], 16)^int(plaintext[i], 16)))
    return cipher


#####

##### function calls

round_keys = keySchedule(key_hex)

### if several blocks -> ECB (for loop)
for blocks in range(0, len(plain_hex), 16):
    # print(blocks)
    roundkey = round_keys[blocks+16:blocks+32]
    plain = plain_hex[blocks:blocks+16]

### Round 1: 
    cipher = addRoundKey(roundkey, plain)
    print(cipher)

### 9 Rounds: loop

    for i in range(9):
        cipher = shiftRow(subBytes(cipher))
        mixColumn(cipher)
        # addRoundKey(roundkey, cipher)

### Final round:

    cipher = shiftRow(subBytes(cipher))
    # addRoundKey()

    # concatenate all the cipher strings?
    #sys.stdout.write(cipher)
    print(cipher)

