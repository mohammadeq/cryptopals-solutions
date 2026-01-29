# Cryptopals Set 1 – Challenge 8: Detect AES in ECB mode

## Challenge Goal
Find the **needle in the haystack**: identify which hex string in a list has been encrypted with AES-ECB by looking for repeated patterns.


# What I Learned
## The Flaw of Determinism 
  * Determinism: In ECB mode, the same 16-byte input always produces the same 16-byte output. This makes the encryption predictable.

## Thinking in Blocks 
  * Alignment: AES operates on a fixed grid. To detect ECB, you cannot just look for any repeating patterns; you must look for identical sequences that are aligned to 16-byte boundaries.


### A lesson:
 - * Confidentiality is more than just hiding letters; it’s about hiding the existence of patterns within the data