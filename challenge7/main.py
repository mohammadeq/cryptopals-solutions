"""
Cryptopals Set 1 Challenge 6: Break repeating-key XOR
challenge link : https://cryptopals.com/sets/1/challenges/6
"""
import base64
from Crypto.Cipher import AES

with open("file.txt") as f:
    ciphertext = base64.b64decode(f.read())


KEY = b'YELLOW SUBMARINE'
cipher = AES.new(KEY, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)

print(plaintext.decode())
