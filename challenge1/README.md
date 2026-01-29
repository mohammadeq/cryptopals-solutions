# Cryptopals Set 1 – Challenge 1: Convert Hex to Base64

## Challenge Goal
The goal of this challenge was to **convert a hex-encoded string into a Base64-encoded string**

## What I Learned


### 1.Hexadecimal Representation
- Hex is base 16
- Each hex character represents nible (4bits)
- Two hex digits = 1 byte 

### 2.Base64 Encoding
- Base64 represents data using 64 characters (A-Z, a-z, 0-9, +, /)
- Every 3 bytes ---> 4 Base64 characters
- If the length isn't divisible by 3 then it adds padding `=`

