# Cryptopals Set 1 – Challenge 5: Repeating-Key XOR
=================================================

### Challenge Goal
--------------

The goal of this challenge was to **encrypt a multi-line string using a sequential, repeating key.** Unlike a single-byte XOR, this required cycling through the bytes of a key (e.g., "ICE") to encrypt the plaintext.

### What I Learned
--------------

### Key Rotation & Modulo

*   The key must "wrap around" to the beginning once it reaches the end.
    
*   I used **modular arithmetic** to track the key index: key\_byte = key\[index % key\_length\].
    
*   This is the fundamental mechanism behind **polyalphabetic ciphers**.
    

### Sequential Processing

*   Each byte of the plaintext is XORed with the corresponding byte of the rotating key.
    
*   Pi XOR Ki (mod L)= Ci
    
    *   P = Plaintext
        
    *   K = Key
        
    *   L = Length of Key
        
    *   C = Ciphertext
        

### Handling Formatted Text

*   I learned that **line breaks (\\n) and punctuation** are part of the plaintext and must be XORed just like letters or numbers to maintain the integrity of the original structure.
    
*   The final output is typically represented in **hexadecimal** to make the non-printable encrypted bytes readable.