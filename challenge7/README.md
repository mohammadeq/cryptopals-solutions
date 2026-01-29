# Cryptopals Set 1 – Challenge 7: AES in ECB mode

## Challenge Goal
Decrypt a file that was locked with a **"real" industry-standard cipher (AES-128)** using a specific password provided to me.

# What I Learned

  * ## What is AES? 
    - AES: The Advanced Encryption Standard is a symmetric block cipher. "Symmetric" means you use the same secret key to both encrypt and decrypt the data.
  * ## What is ECB Mode? 
    - ECB: Electronic Codebook is the simplest way to use a block cipher. It breaks the data into 16-byte blocks and encrypts each block independently using the same key.
    - The Problem: If two blocks of plaintext are *identical*, their corresponding ciphertext blocks will also be *identical*.

    