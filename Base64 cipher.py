# Base64 cipher

import base64


def decode_message():
    encoded_message = input("Introduce a message to decode: ")
    print(base64.b64decode(encoded_message).decode())


def encode_message():
    message = input("Introduce a message to encode: ")
    print(base64.b64encode(message.encode()))


if __name__ == '__main__':
    encode_message()
    decode_message()


# The message "MjAyM19TZWd1cmlkYWRJbmZvcm1hdGljYUJhc2U2NA=="
# means "2023_SeguridadInformaticaBase64".
