"""
Cryptopals Set 1 Challenge 5: Implement repeating-key XOR
challenge link : https://cryptopals.com/sets/1/challenges/5
"""

def XORkey(Unencrypted_text, key):
    encrypted_list = []
    length = 0
    while length < len(Unencrypted_text):
        encrypted_byte = (Unencrypted_text[length]) ^ ord(key[length%len(key)])
        encrypted_list.append(encrypted_byte)
        length += 1
    return encrypted_list

def transfareBytesToHex(encrypted_list):
    encrypted_text = ""
    for i in encrypted_list:
        encrypted_text += format(i, "02x")
    return encrypted_text


encrypted_text_test = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
key = "ICE"
Unencrypted_text = list(b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
encrypted_byte = XORkey(Unencrypted_text, key)
encrypted_text = transfareBytesToHex(encrypted_byte)

print(encrypted_text)

if encrypted_text == encrypted_text_test:
    print("Success.")