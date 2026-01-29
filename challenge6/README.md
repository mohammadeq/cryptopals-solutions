# Cryptopals Set 1 – Challenge 6: Break Repeating-Key XOR

## Challenge Goal
Break a repeating-key XOR cipher **without knowing the key or its length**. Basically decrypt something when I don't have the password.


## What I Learned

### I Actually Broke Encryption
- This wasn't just doing math anymore - I **actually broke something encrypted**
- Used statistics to find patterns in what looked like random garbage

### Hamming Distance
- New concept: counting how many **bits** are different between two things
- Not normal subtraction (66-65=1), but **bit-level differences**
- Letter 'A' (01000001) vs 'B' (01000010) = 2 bits different, not 1
- This is how I figured out the key length without knowing anything about the key
- Used `bin(byte1 ^ byte2).count('1')` to count the differences
### Breaking One Hard Problem Into Easy Ones
This was the key strategy:
1. Find the key length (using Hamming distance)
2. Slice the data into blocks (transposition)
3. Solve each block as single-byte XOR (already knew this from Challenge 3!)

### Transposition
- If the key is 3 bytes long, then every 3rd character was encrypted with the same byte
- So I grouped: characters 0,3,6,9... together, characters 1,4,7,10... together, etc.
- Used Python slicing: `data[0::keysize]`, `data[1::keysize]`, etc.
- This was the **hardest concept to understand** but once I got it, everything clicked

### Why I Needed to Average Multiple Blocks
- At first I only compared 2 blocks and got keysize=2 (wrong!)
- The challenge said "or take 4 blocks and average" - that's why
- More samples = more accurate guess
- Fixed it and got the potiential keysizes


**New functions:**
  - `hamming_distance()` - count bit differences
  - `get_keysize()` - find most likely key length  
  - `get_password()` - transpose and break each block
   
**Reused from earlier challenges:**
  - `score()` and `search_key()` from Challenge 4
  - `XORkey()` from Challenge 5

