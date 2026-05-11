## hex to base 64

base64_chars = (
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    '0','1','2','3','4','5','6','7','8','9','+','/'
)

def hex_to_base64(hex_string):

    binary = bytes.fromhex(hex_string)
    bits = int.from_bytes(binary, "big")
    size = len(binary)*8

    letters = []
    for l in range(size - 6, -1, -6):
        le = (bits >> l) & 0b111111
        letters.append(base64_chars[le])
        
    return ''.join(letters)

def main():
    input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(hex_to_base64(input))

if __name__ == "__main__":
    main()