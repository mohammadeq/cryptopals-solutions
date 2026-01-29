# Cryptopals Set 1 – Challenge 3: Single-Byte XOR Cipher
------------------------------------------------------

### Challenge Goal

The goal was to **decrypt a hex-encoded string that had been XORed against a single character.** The trick was to figure out which character was the key without being told what it was.

### What I Learned

*   **Frequency Analysis:** Since English text isn't random, you can score "decrypted" strings based on how frequently letters like 'E', 'T', and 'A' appear.
    
*   **Brute Forcing:** With only 256 possible single-byte keys (0–255), it is computationally trivial to try every single one and check the results.
    
*   **Scoring Heuristics:** To automate the process, I learned to build a function that ranks sentences based on their resemblance to standard English.