def vigenere_cipher(plaintext, encryption_key):
    
    plaintext_length = len(plaintext)
    encryption_key = [int(digit) for digit in str(abs(encryption_key))]

    plaintext = list(plaintext)

    for n in range(plaintext_length):
       if (n+1)%2 == 0:
            shift_amount = encryption_key[1]
       elif (n+1)%3 == 0:
            shift_amount = encryption_key[2]
       elif (n+1)%4 == 0:
            shift_amount = encryption_key[3]
       else:
            shift_amount = encryption_key[0]

       char_to_be_shifted = ord(plaintext[n]) - ord('A')
       new_char = (char_to_be_shifted + shift_amount) % 26
       plaintext[n] = chr(new_char + ord('A'))

    return "".join(plaintext)

def main():

    ciphertext = vigenere_cipher("LAUNCHTHEATTACKATONEPM", 4123)

    print(ciphertext)


if __name__ == "__main__":
    main()
