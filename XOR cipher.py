# XOR cypher

def xor_shift(message, key):
    shifted_message_letters = []
    for key_index, char in enumerate(message):
        char_code = ord(char)
        key_char_code = ord(key[key_index % len(key)])
        shifted_message_letters.append(chr(char_code ^ key_char_code))
    return "".join(shifted_message_letters)


def decode_message():
    encoded_message = input("Introduce a message to decode: ")
    key = input("Introduce the key: ")
    print(xor_shift(encoded_message, key))


def code_message():
    message = input("Introduce a message to code: ")
    key = input("Introduce the key: ")
    print(xor_shift(message, key))


if __name__ == '__main__':
    # code_message()
    decode_message()


# The message "+*5-=;¡.61!47=?9;;;." is coded with key "XOR"
# and means "seguriùadinformatica".
