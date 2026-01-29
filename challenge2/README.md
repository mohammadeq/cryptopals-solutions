# Cryptopals Set 1 – Challenge 2: Fixed XOR

## Challenge Goal
The goal of this challenge was to ***take two equal-length buffers and XOR them together, byte by byte, producing a new encrypted output.***

## What I Learned

### XOR Fundamentals
- XOR (exclusive OR) is a **bitwise operation**.
- It outputs `1` if there is **exactly one `1`** in the comparison, otherwise `0`.
- It is **reversible**: `A ⊕ B = C` → `C ⊕ B = A`.
- **Position matters**: XORing different positions produces completely different results.

