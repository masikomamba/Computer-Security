def HexToBin(hexdec):
    hex_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    binary_string = ""
    for char in hexdec.upper():
        if char in hex_map:
            binary_string += hex_map[char]
        else:
            print(f"\nWarning: Invalid hexadecimal character '{char}' ignored.")
    return binary_string


def s_box_substitution(data):
    s_box = [
        ['E','4','D','1','2','F','B','8','3','A','6','C','5','9','0','7'],
        ['0','F','7','4','E','2','D','1','A','6','C','B','9','5','3','8'],
        ['4','1','E','8','D','6','2','B','F','C','9','7','3','A','5','0'],
        ['F','C','8','2','4','9','1','7','5','B','3','E','A','0','6','D']
    ]

    s = data.strip()

    if any(c not in '01' for c in s):
        s = HexToBin(s)

    if len(s) % 6 != 0:
        pad_len = 6 - (len(s) % 6)
        s = '0' * pad_len + s

    output = []
    for i in range(0, len(s), 6):
        block = s[i:i+6]
        row = int(block[0] + block[-1], 2)   
        col = int(block[1:5], 2)           
        val = s_box[row][col]         
        output.append(format(int(val, 16), '04b'))

    return ''.join(output)


def main():
    input_string = "E4589A34209"


    encrypted_text = s_box_substitution(input_string)
    print(encrypted_text)


if __name__ == "__main__":
    main()
