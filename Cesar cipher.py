# Cesar cipher

def cesar_shift(message, shift):
    shifted_chars = []
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char.upper()) - 65 + shift) % 26 + 65)
            if char.islower():
                shifted_char = shifted_char.lower()
        else:
            shifted_char = char
        shifted_chars.append(shifted_char)
    return "".join(shifted_chars)


def decode_message():
    encoded_message = input("Introduce a message to decode: ")
    for shift in range(26):
        print(str(shift) + ": " + cesar_shift(encoded_message, -shift))


def encode_message():
    message = input("Introduce a message to encode: ")
    shift = int(input("Introduce the desired shift: "))
    print(cesar_shift(message, shift))


if __name__ == '__main__':
    encode_message()
    decode_message()


# The message "MyaolcxuxChzilguncwuWymul" is encoded with shift 20,
# and means "SeguridadInformaticaCesar".
