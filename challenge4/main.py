"""
Cryptopals Set 1 Challenge 4: Detect single-character XOR
challenge link : https://cryptopals.com/sets/1/challenges/4
"""

most_english_repeated_letters = ['e', 't', "a", 'o', 'i', 'n', 's', 'h', 'r', 'l', 'd', 'c', 'u',
                                 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'x', 'q', "j", "z", " "]


def encode(hex_decoded2, key):
    string = ""
    for b in hex_decoded2:
        string += chr(b ^ key)
    return string


def score(text):
    counter = 0
    for c in text.lower():
        if c in most_english_repeated_letters:
            counter += 1
    return counter


def search_key(hex_decoded):
    best_key = 0
    best_score = 0
    best_string = ""

    for key in range(256):
        decoded = encode(hex_decoded, key)
        s = score(decoded)

        if s > best_score:
            best_score = s
            best_key = key
            best_string = decoded

    return best_key, best_string, best_score

def search_line_number(hex_encoded_string):
    counter = 0
    with open(r"D:\Script\python\cryptopals\challenge4\file.txt", "r") as f:
        for line in f:
            hex_string = line.strip()
            counter += 1
            if hex_string == hex_encoded_string:
                break
    return counter

best_alltime_score = 0
best_alltime_string = ""
best_alltime_key = None
best_alltime_hex = None

with open(r"D:\Script\python\cryptopals\challenge4\file.txt", "r") as f:
    for line in f:
        hex_string = line.strip()
        hex_decoded = list(bytes.fromhex(hex_string))

        key, decoded_string, score_value = search_key(hex_decoded)

        if score_value > best_alltime_score:
            best_alltime_score = score_value
            best_alltime_key = key
            best_alltime_string = decoded_string
            best_alltime_hex = hex_string
            line_number = search_line_number(best_alltime_hex)


print("String: ", best_alltime_string)
print("Key: ", best_alltime_key)
print("Hex encoded string:", best_alltime_hex)
print("Line number of the hex string:", line_number)