from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher = "YLXEICIOHEJUQHUBPYUKPCIASVOPSNIEAGKULXFUPPOYHKAPMHMOICPANCIHAISPAEINUPMIFLXCLUQKAPMHMOIOIUUIAYIWVIXEILSUQIBHFLEOIUUIAWCIAIKAIYIXUCIYQPVONOPPJSPAHEPBKHXLPXVHXNHSUIAUQHUSPAHRPCIOUPSPOOPCWVMVUUQLYUPPLYOHEJLXFSHBLOLHALUGCLUQIXFOLYQNLFAHBYPALXUQIEHYIPSUQIMIFLXXIAHXLXYKIEULPXPSUQINLFAHBEQHAUPAUQIOLYUPSNLFAHBYYQPCYUQHUUQLYMGSHAUQIBPYUSAIWVIXUEPBMLXHULPXVYINLXUQIOHXFVHFIHXNUQHUQIHXNQHHOYPLXEOVNLXFHXQHAIRIAGKAPBLXIXUHBPXFUQIOIHNIAYSVAUQIAUQHXUQLYUQIOLYUPSUALFAHBYLXSPABYVYUQHUMPUQUQIHXNUQHHAIPSPVUYUHXNLXFSAIWVIXEGPSUQISPVAOIUUIAYLXEOVNINUQAIIHAIYPSAIWVIXUHXNHKKIHALXYPBHXGNLSSIAIXUEPBMLXHULPXYHYUPMIEPXSVYLXFMVUQUQPVFQMIOPXFLXFUPUQIQLFQSAIWVIXEGFAPVKNPIYXPUHKKIHALXBHXGNLSSIAIXUEPBMLXHULPXYHXNLYOIYYSAIWVIXUUQHXUQIPUQIAUQAIIOPPJLXFUQIXSPAQCISLXNLUUCLEILXPVAKAIYIXUEAGKUPFAHBPXEIPXUQIYIEPXNAPCHXNPXEIPXUQIYIRIXUQHXNYLXEIUQIYIRIXUQAPCYQPCYUCPUYHXNUQIYIEPXNPXOGPXIUYVKKPYICIUAGUQIYIEPXNAPCKOHELXFUPFIUQIAUQIUCPEPOVBXYYUALKYCQLEQHAIQIHNINMGUQIXVBMIAYLXPANIAUPYIUVKHNLFAHBUQPXUQIYIEPXNAPCHYYQPCXHUMXFPXFPSHMHXNPXINLXUQHUQHNALTALTFSHRPAPSEUQISPABHULPXPSUQLYNLFAHBUQPXUQIYIEPXNAPCQHYHVUPBHULEHOOGYIUVKHNLFAHBXFPXUQIUPKAPCHNLFAHBALPXUQIUQLANAPCHXNYPPXHXNCISLXNVKPXITHBLXLXFUQIYIXICOGSPABINNLFAHBYUQHUUQICQPOIYIALIYLYBHNIVKPSFPPNIXFOLYQEPBMLXHULPXYUQVYLUOPPJYHYLSPVAEPBMLXHULPXLYEPAAIEUHXNCICLOOKAPEIINCLUQHKPYYLMOIQIPAQHHUUIBKULXFUPEPBKOIUIHUALFAHBUQIPAUQHPXUQIYIEPXNAPCMPUQIHXNHHAIKAIYIXUPXUQIYIEPXNAPCHXNCIBHGPMYIARIHUUQIYUIKYBHAJINEHXNNLXUQISLFVAIZVYUCQHUCPVONMIUQIAIYVOUPSHNNLXFYUALKPAYUALKHUSLAYUFOHXEILUHKKIHAYUQHUEPBMLXHULPXYHXNHAIHMPVUIWVHOOGKAPMHMOIMVULUYPQHKKIXYUQHUMPUQYIUVKYQHRISPABINHYIWVIXEIGPPXUQISLSUQOLXIYVFFIYULXFGPVHXNCQIXUQIPXOGVPXUQHUOLXILYUALINLXMPUQKOHEIYLUMIEPBIYIRLNIXUUQHUEPBMLXHULPXLYFPLXFUPFLRIMIUUIAAIYVOUYUQHXEPBMLXHULPXCQIAICISLXNKPPAYIWVIXEIYOLJIJISQHUUQLYKPLXUPAIHAOLIAHNIEAGKUPACLOOKAPMHMOGKAPEIINPXUQIOISUYLNIPSQLYYIUVKEPBKOIULXFUQIYGOOHMOILXFHXNUQIYIALIYPSEPOVBXXVBMIAYHYYQPCXCQIXUQLYYIUULXFUPFIUQIAPSEPOVBXYHVUPBHULEHOOGMALXFYPVUPXUQIUQLANAPCHYIWVIXEIMALNFCIQHRIPVASLAYUYVFFIYULPXPSHKAPMHMOICPANYLXEIUQIBHXCQPQHNUQLYEAGKUPFAHBPXQLYKIAYPXQHNZVYUHUUIBKUINUPMOPCVKHMALNFIHSUIAUQLYHOOLYKOHLXYHLOLXFUQIXIEIYYHAGIQHKKIXYUPMIPXUQIYHBIOLXIHXNIRIXLSLUCIAIXPUCIQHRIPXOGUQAIIYUALKYOISUHXNUQIYIBHGMIKOHEINMGUALHOUQVYPVAILFQUKHKIAYUALKYHAALRIHUUQIYUHFILXNLEHUINPXUQIOISUQHXNYLNIPSSLFCLXFPSOPMGUQINAHMGUQINAHCLXFPSOPUMALNFITUYLUSHOOLAYUBPRIYUPGPVUPYUPGPVUPUHJIUQISUYLUSHOOLAYUBPRIUHJIUQISTTRLHNVETTRLHNVELSCIQHRIKAIRLPVYOGBIUUQIXLQLOLYUUAHXYKPYLULPXCIEHXYIIXPCCQHUUQIELKQIALYHXNLSLULYHUAVIXLQLOLYUCIEHXSLXLYQUQIAIEPXYUAVEULPXMGNIELKQIABIXUCLUQUQIJIGUPNPUQLYCIYLBKOGXVBMIAUQIAPCYSAPBUPHXNUQIXNLYHAAHXFIUQIYIAPCYYPUQHUUQILAXVBMIAYCLOOAIKAPNVEIUQIYIALIYPSEPOVBXXVBMIAYUQLYLYYQPCXPXUQIALFQUQHXNYLNIPSSLFCQIAIUQIKOHLXUITULYIHYLOGAIHNMGUQINAHCLXFPSOPUYLUSHOOYUPGPVUPUHJIUQISLAYUBPRIRLHNVEUMALNFIUQIFIXUOIBHXAIWVLAINUQAIIXVOOYHXNUQALSULOGBHNIVYIPSUQIBHYKVXEUVHULPXLSCIQHRIXPUKAIRLPVYOGBIUUQIXLQLOLYUIXELKQIABIXUPALSUQLYEAGKUPFAHBLYPSHJLXNAINUGKIMVUFPRIAXINMGUCPYIKHAHUIJIGYPXISPAEPOVBXYHXNHXPUQIASPAAPCYUQIPXOGNLSSIAIXEILYUQHUCIBHGQHRIUPITKIALBIXUHOLUUOICLUQAPCYMISPAISLXNLXFUQILAEPAAIEUPANIALXEPBKOIULXFPVAYPOVULPXCIQHRIPMUHLXINHJIGYQPCXLXUQIYIALIYPSEPOVBXXVBMIAYHXNYQPVONPUQIAEAGKUPFAHBYMILXUIAEIKUINQHRLXFUQIYHBIJIGHYUQISLAYUCIXIINBIAIOGNIELKQIAUQIBCLUQPVAJIGLULYQPCIRIAHUHJLXFPVUJIGCQLOIUQIXLQLOLYUHYCIQHRIYIIXLYPANLXHALOGCALUUIXLXQHRLXFILUQIAPSUQIJIGYCIBHGSLXNUQIPUQIAIHYLOGIXPVFQHYYVFFIYUINLXUQISLFVAIYLBKOGXVBMIAUQIXVBMIAYHXNKVUUQIBMHEJLXYIALHOPANIAUQIXICYIUPSXVBMIAYXPCNLYHAAHXFINCLOOYQPCGPVUQIPUQIAJIGLUCPVONXPUMILBKPYYLMOISPAUQIYUVNIXUCQPLYHFPPNFVIYYIAUPSLXNUQIJIGCPANPXCQLEQPVAKAIYIXUCALULXFLXJIGCHYMHYINUQLYJLXNPSCPAJCLUQKHKIAYUALKYLYBVEQBPAIAHKLNUQHXLUKAPMHMOGYIIBYHXNLYPSUIXNPXIHUAHXNPBUQIJIIXIGIXIINYXPNLFAHBOLYUSPAUQIYKPUULXFPSQUBIAIOGAIRIAYINCLUQFXHMPRILUYKIHJLXFXPCPSUQIPANLXHAGEPOVBXHAYSLFPXIBLXPAKPLXUYQPVONKIAQHKYMIMAPVFQUUPUQIHUUIXULPXPSUQIRIAGXICYUVNIXUWVLUIPSUIXHNLFAHBYVEQHYUQIWVPSSLFLYXPUCALUUIXPXHYLXFOIOLXIHXNLUBHGMIXIEIYYHAGUPBHUEQUQLYRHOVHMOINLFAHBLXUQIBHXXIAYQPCXHUMPSUQHUSLFVAIEPBLXFPVULXUQIIXNHYHUE".lower()
bigraphs = {
    "th": 5532,
    "he": 4657,
    "in": 3429,
    "er": 3420,
    "an": 3005,
    "re": 2465,
    "nd": 2281,
    "at": 2155,
    "on": 2086,
    "nt": 2058,
    "ha": 2040,
    "es": 2033,
    "st": 2009,
    "en": 2005,
    "ed": 1942,
    "to": 1904,
    "it": 1822,
    "ou": 1820,
    "ea": 1720,
    "hi": 1690,
    "is": 1660,
    "or": 1556,
    "ti": 1231,
    "as": 1211,
    "te": 985,
    "et": 704,
    "ng": 668,
    "of": 569,
    "al": 341,
    "de": 332,
    "se": 300,
    "le": 298,
    "sa": 215,
    "si": 186,
    "ar": 157,
    "ve": 148,
    "ra": 137,
    "ld": 64,
    "ur": 60,
}
trigraph = {
    "THE": 1.81, "AND": 0.73, "ING": 0.72, "ENT": 0.42, "ION": 0.42,
    "HER": 0.36, "FOR": 0.34, "THA": 0.33, "NTH": 0.33, "INT": 0.32,

    "ERE": 0.31, "TIO": 0.31, "TER": 0.30, "EST": 0.28, "ERS": 0.28,
    "ATI": 0.26, "HAT": 0.26, "ATE": 0.25, "ALL": 0.25, "ETH": 0.24,

    "HES": 0.24, "VER": 0.24, "HIS": 0.24, "OFT": 0.22, "ITH": 0.21,
    "FTH": 0.21, "STH": 0.21, "OTH": 0.21, "RES": 0.21, "ONT": 0.20
}


def mono(cipher, key):
    plaintext = ""
    for c in cipher:
        plaintext += key[alphabet.index(c)]

    return plaintext

def digram(cipher):
    digram = {}

    for i in range(len(cipher) - 1):
        di = cipher[i:i+2]

        if not di in digram:
            digram[di] = 1
        else:
            digram[di] += 1

    return digram

def trigram(cipher):
    trigram = {}

    for i in range(len(cipher) - 2):
        di = cipher[i:i+3]

        if not di in trigram:
            trigram[di] = 1
        else:
            trigram[di] += 1

    return trigram

def print_di(digram, digraph):
    ci = list(digram.keys())[:25]
    civ = list(digram.values())[:25]

    dig = list(digraph.keys())[:25]
    digv = list(digraph.values())[:25]


    fig, axes = plt.subplots(2, 1, figsize=(20, 4))

    axes[0].bar(ci, civ, color='skyblue')
    axes[0].set_title('Ci Digraph Frequency', fontsize=10)
    axes[0].set_xlabel('Letters', fontsize=10)
    axes[0].set_ylabel('Frequency', fontsize=10)
    axes[0].grid(axis='y', alpha=0.3)

    # Plot 2: Vowels only (sorted)
    axes[1].bar(dig, digv, color='lightcoral')
    axes[1].set_title('Eng Digraph Freq', fontsize=10)
    axes[1].set_xlabel('Letters', fontsize=10)
    axes[1].set_ylabel('Frequency', fontsize=10)
    axes[1].grid(axis='y', alpha=0.3)

    plt.tight_layout()  # Adjust spacing between subplots
    plt.show()


def freq(cipher):
    cipher = Counter(cipher).most_common()
    
    return cipher


def frequency(cipher):
    cipher = Counter(cipher).most_common()
    print(cipher)

    freqEnglish = {'e': 0.12702, 't': 0.09056, 'a': 0.08167, 'o': 0.07507, 'i': 0.06966, 'n': 0.06749, 
                's': 0.06327, 'h': 0.06094, 'r': 0.05987, 'd': 0.04253, 'l': 0.04025, 'c': 0.02782,
                'u': 0.02758, 'm': 0.02406, 'w': 0.02360, 'f': 0.02228, 'g': 0.02015, 'y': 0.01974, 
                'p': 0.01929, 'b': 0.01492, 'v': 0.00978, 'k': 0.00772, 'j': 0.00153, 'x': 0.00150,
                'q': 0.00095, 'z': 0.00074}

    letters = list(freqEnglish.keys())
    frequencies = list(freqEnglish.values())

    cipher_letters = [obj[0] for obj in cipher]
    cipher_frequencies = [obj[1] for obj in cipher]

    fig, axes = plt.subplots(2, 1, figsize=(20, 4))

    axes[0].bar(letters, frequencies, color='skyblue')
    axes[0].set_title('English Standard Frequency', fontsize=10)
    axes[0].set_xlabel('Letters', fontsize=10)
    axes[0].set_ylabel('Frequency', fontsize=10)
    axes[0].grid(axis='y', alpha=0.3)

    # Plot 2: Vowels only (sorted)
    axes[1].bar(cipher_letters, cipher_frequencies, color='lightcoral')
    axes[1].set_title('Stream 7', fontsize=10)
    axes[1].set_xlabel('Letters', fontsize=10)
    axes[1].set_ylabel('Frequency', fontsize=10)
    axes[1].grid(axis='y', alpha=0.3)

    plt.tight_layout()  # Adjust spacing between subplots
    plt.show()



digram = digram(cipher)
#print_di(dict(sorted(digram.items(), key=lambda item: item[1], reverse=True)), bigraphs)

trigram = trigram(cipher)
#print_di(dict(sorted(trigram.items(), key=lambda item: item[1], reverse=True)), trigraph)
#print(list(dict(sorted(digram.items(), key=lambda item: item[1], reverse=True)).keys())[:25])
#print(list(bigraphs.keys())[:25])
#print(list(dict(sorted(trigram.items(), key=lambda item: item[1], reverse=True)).keys())[:25])
#print(list(trigraph.keys())[:25])

## certain
# uqi in cipher -> the
# i -> e

## maybe
# ixu -> ent
# x -> n
# l -> i

# h -> a
# a -> r
# p -> o

plaintext = ""
for c in cipher:
    if c == 'u':
        plaintext += 't'
    elif c == 'q':
        plaintext += 'h'
    elif c == 'i':
        plaintext += 'e'
    elif c == 'x':
        plaintext += 'n'
    elif c == 'l':
        plaintext += 'i'
    elif c == 'h':
        plaintext += 'a'
    elif c == 'a':
        plaintext += 'r'
    elif c == 'p':
        plaintext += 'o'

    elif c == 'n':
        plaintext += 'd'
    elif c == 'f':
        plaintext += 'g'

    elif c == 'y':
        plaintext += 's'
    
    elif c == 'v':
        plaintext += 'u'
    
    
    elif c == 'e':
        plaintext += 'c'
    elif c == 'b':
        plaintext += 'm'
    elif c == 'm':
        plaintext += 'b'

    elif c == 's':
        plaintext += 'f'

    elif c == 'g':
        plaintext += 'y'
    elif c == 'c':
        plaintext += 'w'
    elif c == 'k':
        plaintext += 'p'
    elif c == 'w':
        plaintext += 'q'
    elif c == 'j':
        plaintext += 'k'
    
    elif c == 'r':
        plaintext += 'v' 
    elif c == 't':
        plaintext += 'x'
    elif c == 'z':
        plaintext += 'j'
    

    elif c == 'o':
        plaintext += 'l'
    
    else:
        plaintext += c

# cipher d or plain z does not ever appear
    

print(plaintext)