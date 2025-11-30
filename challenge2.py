"""
Cryptopals Set 1 Challenge 2: Fixed XOR 
Challenge link: https://cryptopals.com/sets/1/challenges/2
"""


def XOR(frist_string, second_string):
    first_string_bytes = list(bytes.fromhex(frist_string))
    second_string_bytes = list(bytes.fromhex(second_string))
    i = 0
    produced_combination_bytes = []
    while i < len(first_string_bytes) and i < len(second_string_bytes) :
        f_bit = first_string_bytes[i]
        s_bit = second_string_bytes[i]
        fs_bit = f_bit^s_bit
        produced_combination_bytes.append(fs_bit)
        i +=1 
    produced_combination_string = bytes(produced_combination_bytes).hex()
    return produced_combination_string    

frist_string = "1c0111001f010100061a024b53535009181c"
second_string = "686974207468652062756c6c277320657965"
expected_combination = "746865206b696420646f6e277420706c6179"

the_combination = XOR(frist_string, second_string)

print(f"The First String: \"{frist_string}\"")
print(f"The Second String: \"{second_string}\"")

if expected_combination == the_combination:
    print("Success.")
else:
    print("Failure")


print(f"The Combination String \"{the_combination}\"")
print(f"The Expected Combination String: \"{expected_combination}\" ")




