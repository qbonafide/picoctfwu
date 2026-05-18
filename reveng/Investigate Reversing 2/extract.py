def extract_flag():
    with open('./encoded.bmp','rb') as f:
        f.seek(2000)
        hidden_bytes = f.read(400)

    flag=""

    for i in range(0, 400, 8):
        chunk = hidden_bytes[i:i+8]

        binary_str=""
        for byte in chunk:
            lsb = byte & 1
            binary_str = str(lsb) + binary_str

        char_dec = int(binary_str, 2)
        original_char_dec = char_dec + 5
        flag += chr(original_char_dec)

    print("Flag:", flag)

if __name__ == "__main__":
    extract_flag()