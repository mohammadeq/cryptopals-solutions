"""
Cryptopals Set 1 Challenge 6: Break repeating-key XOR
challenge link : https://cryptopals.com/sets/1/challenges/6
"""
import base64

most_english_repeated_letters = ['e', 't', "a", 'o', 'i', 'n', 's', 'h', 'r', 'l', 'd', 'c', 'u',
                                 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'x', 'q', "j", "z", " "]

def encode(b64_decoded, key):
    string = ""
    for b in b64_decoded:
        string += chr(b ^ key)
    return string


def score(text):
    counter = 0
    for c in text.lower():
        if c in most_english_repeated_letters:
            counter += 1
    return counter

def search_key(b64_decoded):
    best_key = 0
    best_score = 0
    best_string = ""

    for key in range(256):
        decoded = encode(b64_decoded, key)
        s = score(decoded)

        if s > best_score:
            best_score = s
            best_key = key
            best_string = decoded

    return best_key, best_string, best_score


def hamming_distance(first_string, second_string):
    hamming_distance_counter = 0
    i=0
    while i < len(first_string) and i < len(second_string):
        hamming_distance = first_string[i] ^ second_string[i]
        hamming_distance_counter += bin(hamming_distance).count('1')
        i+=1
    return hamming_distance_counter

def get_keysize():
    with open("file.txt", "rb") as f:
        data = base64.b64decode(f.read())
        results = []
        for i in range(2, 41):
            block1 = hamming_distance(data[0:i], data[i:i*2])
            block2 = hamming_distance(data[i:2*i], data[2*i:i*3])
            block3 = hamming_distance(data[2*i:3*i], data[3*i:i*4])
            edit_distance_average = (block1 + block2+block3)/3
            edit_distance = edit_distance_average/i
            results.append((edit_distance, i))
        results.sort()
    return  results[0][1], results[1][1], results[2][1], results[3][1]

def get_password():
    password = None
    blocksizes = get_keysize()
    with open("file.txt", "rb") as f:
            data = base64.b64decode(f.read())
    potential_full_keys = []
    for size in blocksizes:
        potential_key = []
        for i in range(size):
            block = data[i::size]
            best_key, _, __ = search_key(block)

            potential_key.append(chr(best_key))
        full_key = "".join(potential_key)
        potential_full_keys.append(full_key)
    best_score = 0
    for key in potential_full_keys:
        s = score(key)
        if best_score < s:
            best_score = s
            password = key
    return password
    

def XORkey(encrypted_text, key):
    decrypted_list = []
    length = 0
    while length < len(encrypted_text):
        decrypted_byte = (encrypted_text[length]) ^ ord(key[length%len(key)])
        decrypted_list.append(decrypted_byte)
        length += 1
    return decrypted_list
def transfareBytesToText(decrypted_list):
    decrypted_text = ""
    for i in decrypted_list:
        decrypted_text += chr(i)
    return decrypted_text

key = get_password()
with open("file.txt", "rb") as f:
    data = base64.b64decode(f.read())
decrypted_list = XORkey(data, key)
print(transfareBytesToText(decrypted_list))
