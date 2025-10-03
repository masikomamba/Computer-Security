import math

def decToHexa(n):
    if n == 0:
        return "0"

    hexaDeciNum = []
    while n != 0:
        temp = n % 16
        if temp < 10:
            hexaDeciNum.append(chr(temp + 48)) 
        else:
            hexaDeciNum.append(chr(temp + 55))
        n //= 16

    return ''.join(reversed(hexaDeciNum))


def hex_char_to_decimal(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    elif 'A' <= c <= 'F':
        return 10 + (ord(c) - ord('A'))
    elif 'a' <= c <= 'f':
        return 10 + (ord(c) - ord('a'))
    else:
        raise ValueError(f"Invalid hex character: {c}")

def hex_to_decimal(hex_str):
    decimal_value = 0
    base = 1
    
    for c in reversed(hex_str):
        digit = hex_char_to_decimal(c)
        decimal_value += digit * base
        base *= 16
    
    return decimal_value

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modInverse(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % phi

def main():
    p = "F7E75FDC469067FFDC4E847C51F452DF"
    q = "E85CED54AF57E53E092113E62F436F4F"
    e = "0D88C3"

    p= hex_to_decimal(p)
    q = hex_to_decimal(q)

    e = hex_to_decimal(e)
    n = p*q

    phi = (p-1) * (q-1)


    d = modInverse(e, phi)

    message = hex_to_decimal("E4589A34209")
    print("Message:", message)

    encrypted_text = pow(message, e, n)
    decrypted_text = pow(encrypted_text, d, n)


    original_message = decToHexa(decrypted_text)


    print("Encrypted text:", encrypted_text)

    print("Decrypted text:", original_message)


if __name__ == "__main__":
    main()