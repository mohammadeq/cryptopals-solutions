"""
Cryptopals Set 1 Challenge 1: convert hex to base64
challenge link : https://cryptopals.com/sets/1/challenges/1
"""
import base64

hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expected_output = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

binary = bytes.fromhex(hex_string)

base64_encoded_bytes = base64.b64encode(binary)

base64_string = base64_encoded_bytes.decode('utf-8')

print(f"Hex: {hex_string}")
print(f"Base64: {base64_string}")
if expected_output == base64_string:
    print("\nSuccess.\n")
    print(f"\nThe expected output is: \"{expected_output}\"\n")