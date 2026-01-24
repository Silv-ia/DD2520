## Input and output work! No TypeError
# Wrong Answer.

import sys

##### constants
s_box = (
#    0     1    2    3    4    5    6    7    8    9    a    b    c    d   e    f
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)



r_con = (
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36
)

##### Key expansion -- checked 

# calls rotWord and subBytes
def keySchedule(key):
    round = 0
    ind1 = 0
    ind2 = 12
    rind = 0

    for i in range(10):
        round += 1
        # print("Round: ", round)
        # print(key.hex())
        key = rotWord(ind2, key)
        ind2 += 4
        # print(key.hex())
        key = subBytesKey(ind2, key)
        # print(key.hex())

        # print(key[ind2])
        # print(key[ind1])
        # print("Round const:", r_con[rind])
        key[ind2] ^= key[ind1] ^ r_con[rind]
        key[ind2+1] ^= key[ind1+1] 
        key[ind2+2] ^= key[ind1+2]
        key[ind2+3] ^= key[ind1+3]
        # print(key.hex())
        ind1 += 4
        rind += 1
        for i in range(3):
            key.append(key[ind1] ^ key[ind2])
            key.append(key[ind1+1] ^ key[ind2+1])
            key.append(key[ind1+2] ^ key[ind2+2])
            key.append(key[ind1+3] ^ key[ind2+3])
            ind1 += 4
            ind2 += 4
        # print("Key after round: ", round)
        # print(key.hex())
    return key

# creates new column -- checked, okay
def rotWord(index, key):
    # print(key.hex())
    
    key.append(key[index+1])
    key.append(key[index+2])
    key.append(key[index+3])
    key.append(key[index])
    # print(key.hex())

    return key

## checked ok
def subBytesKey(index, key):
    # print(key.hex())

    key[index] = s_box[key[index]]
    key[index+1] = s_box[key[index+1]]
    key[index+2] = s_box[key[index+2]]
    key[index+3] = s_box[key[index+3]]
    # print(key.hex())
    
    return key

#####

##### rounds

def subBytes(state):
    for i in range(len(state)):
        state[i] = s_box[state[i]]
    # print(state)
    return state

def shiftRow(state):
    state[1],state[5], state[9], state[13] = state[5], state[9], state[13], state[1]
    state[2], state[6], state[10], state[14] = state[10], state[14], state[2], state[6]
    state[3], state[7], state[11], state[15] = state[15], state[3], state[7], state[11]

    return state

# multiplication by 2, shift left.
# xor 0x1b to cut overflow
def xtime(x):
    # shift left is multiply by 2. check the MSB(?) if it is one or not, by & 1 and then this * 0x1B
    # will determine if we do ^0x1B. finally, mask
    return ((x << 1) ^ (((x >> 7) & 1) * 0x1B)) & 0xFF


## taken from "The Design of Rijndael - Joan Daemen, Vincent Rijman"
def mixColumn(state):

    # each block is a single array -> column-major -> arr[0:3] is column 1
    for i in range(0, 16, 4):
        t = state[i] ^ state[i+1] ^ state[i+2] ^ state[i+3] 
        u =  state[i] 
        state[i] ^= xtime(state[i] ^ state[i+1]) ^ t
        state[i+1] ^= xtime(state[i+1] ^ state[i+2]) ^ t
        state[i+2] ^= xtime(state[i+2] ^ state[i+3]) ^ t
        state[i+3] ^= xtime(state[i+3] ^ u) ^ t
    return state
    

def addRoundKey(roundkey, state):
    # print("addRoundKey got:", type(state))
    # print(len(roundkey))
    # print(len(plaintext))
    for i in range(16):
        # print(roundkey.hex())
        # print(state[i])
        state[i] ^= roundkey[i]
    return state


#####

##### function calls

def main():
    
    key = sys.stdin.buffer.read(16)
    plaintext = sys.stdin.buffer.read()
    
    ## input is a whole string, partitions into key and plaintext.
    # key = input[:32] # list()
    # plaintext = input[32:]
    # column-major. 
    
    key_bytes = bytearray(key)
    plain_bytes = bytearray(plaintext)
    
    round_keys = keySchedule(key_bytes)
    print(round_keys.hex())
    
    ### if several blocks -> ECB (for loop)
    for blocks in range(0, len(plain_bytes), 16):
        # print(blocks)
        roundkey = round_keys[0:16]
        plain = plain_bytes[blocks:blocks+16]
        # print(plain.hex())
        # print(roundkey.hex())
    
    ### Round 1: 
        state = addRoundKey(roundkey, plain)
        # print(cipher)
    
    ### 9 Rounds: loop
    
        for i in range(9):
            roundkey = round_keys[16+i*16:i*16+32]
            # print(roundkey.hex())
            state = subBytes(state)
            # print(state.hex())
            state = shiftRow(state)
            # print(state.hex())
            state = mixColumn(state)
            # print(state.hex())
            state = addRoundKey(roundkey, state)
    
    ### Final round:
    
        cipher = addRoundKey(roundkey, shiftRow(subBytes(state)))
    
        # concatenate all the cipher strings?
        sys.stdout.buffer.write(cipher)
       
        
if __name__ == "__main__":
    main()