"""
Cryptopals Set 1 Challenge 8: Detect AES in ECB mode
challenge link : https://cryptopals.com/sets/1/challenges/8
"""
from Crypto.Cipher import AES

def socre(string_bytes):
    i = 0
    blocks = []
    while i < len(string_bytes):
        blocks.append(string_bytes[i:i+16])
        i+=16
    counter = len(blocks) - len(set(blocks))
    return counter
best_score = 0
detected = None
line_counter = 0
line_number = 0
with open('file.txt') as file:
    for line in file:
        bytes_ = bytes.fromhex(line)
        s = socre(bytes_)
        line_counter += 1
        if s > best_score:
            line_number = line_counter
            detected = bytes_
            best_score = s
print(f"Detected on line : {line_number} which is \" {detected.hex()} \" ")