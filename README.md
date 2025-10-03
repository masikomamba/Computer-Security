# Computer-Security

# Lab 1

This repository contains Python scripts that implement a vigenere cipher, an S-Box substitution, and the RSA encryption.

## Requirements

This project requires Python 3 to run.

## Scripts Overview

### 1\. Vigenère Cipher (`Lab_1.py`)

#### Description

The `Lab_1.py` script implements the Vigenère cipher. It encrypts a given uppercase plaintext string using a numeric key. The key works like this:

  - The encryption key (e.g., `4123`) is converted into a list so we can get individual digits (`[4, 1, 2, 3]`).
  - The script iterates through each character of the plaintext.
  - A digit from the key is selected to shift the character's position in the string:
      - If the position is divisible by 2, the second digit of the key is used.
      - If the position is divisible by 3, the third digit is used.
      - If the position is divisible by 4, the fourth digit is used.
      - Else the first digit of the key is used.
  - The character is then shifted by the selected amount using a standard Caesar cipher operation modulo 26.

#### How to Run

The plaintext and encryption key are included in the `main` function. To run the script, run the command in your terminal:

```bash
python Lab_1.py
```

### 2\. S-Box Substitution (`S_box_Substitution.py`)

#### Description

The `S_box_Substitution.py` script demonstrates an S-Box. This script takes a binary or hexadecimal string as input and performs a substitution using a predefined S-Box.

How it works:

1.  If the string is not binary, it is converted to binary.
2.  The binary string is processed in 6-bit blocks.
3.  For each 6-bit block:
      - The first and last bits are combined to form a 2-bit number that determines the **row** in the S-Box.
      - The middle four bits are used to determine the **column**.
4.  The value at `S-Box[row][col]` is retrieved. This value is a hexadecimal character.
5.  This hexadecimal character is converted into its 4-bit binary representation.
6.  The final output is the concatenation of all the resulting 4-bit blocks.

#### How to Run

The input string is hardcoded in the `main` function.

```bash
python S_box_Substitution.py
```

#### Output

The script will print the final substituted binary string to the console.


### 3\. RSA Public-Key Cryptosystem (`RSA_Cypher_Implementation.py`)

#### Description

This script provides an implementation of the RSA encryption algorithm. It shows the process of key generation, encryption, and decryption.

How it works:

1.  **Key Generation**:
      - Start with two prime numbers, `p` and `q`, and a public exponent `e`.
      - Calculates the modulus `n = p * q`.
      - Calculates Euler's totient function `phi(n) = (p-1) * (q-1)`.
      - Calculates the private key `d` as the modular multiplicative inverse of `e` modulo `phi(n)`. This is done using the Extended Euclidean Algorithm.
2.  **Encryption**:
      - Takes a hexadecimal message, converts it to a decimal integer `m`.
      - Encrypts the message using the public key `(e, n)` with the formula: `ciphertext = (m^e) mod n`.
3.  **Decryption**:
      - Decrypts the ciphertext using the private key `(d, n)` with the formula: `plaintext = (ciphertext^d) mod n`.
      - Converts the resulting decimal value back to hexadecimal to show that it matches the original message.

#### How to Run

The values `p`, `q`, `e`, and the message included in the script. Run the script like this:

```bash
python RSA_Cypher_Implementation.py
```

#### Output

The script will print the following to the console:

  - The original message converted to a decimal integer.
  - The encrypted text (a large decimal integer).
  - The decrypted text, converted back to its original hexadecimal string form.
