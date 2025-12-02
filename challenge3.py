"""
Cryptopals Set 1 Challenge 3: Single-byte XOR cipher
challenge link : https://cryptopals.com/sets/1/challenges/3
"""

hex_encoded_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

hex_decoded = list(bytes.fromhex(hex_encoded_string))

most_english_repeated_letters = ['e', 't', "a", 'o', 'i', 'n', 's', 'h', 'r', 'l', 'd', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'x', 'q', "j", "z", " "]


def encode(hex_decoded2, numberoftries):
    string = ''
    for i in hex_decoded2:
        letter = chr(i^numberoftries)
        string += letter
    return string

def search_key():
    key = 0
    max = 0
    numberOftries = 0
    while numberOftries <= 255:
        string = encode(hex_decoded, numberOftries)
        counter = 0
        for i in string:
            if  i.lower() in most_english_repeated_letters:
                counter +=1
        if counter > max:
            max = counter
            key = numberOftries
        numberOftries += 1
    return key

key = search_key()
string = encode(hex_decoded,key)

print(f"String: {string}, key: {key}")