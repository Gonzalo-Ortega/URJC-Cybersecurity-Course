# AES cipher

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii


def initialize_cipher():
    key = input("Introduce the key: ")
    iv = input("Introduce the iv: ")
    return AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))


def code_message():
    message = input("Introduce a message to code: ")
    cipher = initialize_cipher()
    padded_message = pad(message.encode("utf8"), AES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    hex_message = binascii.hexlify(encrypted_message).decode('utf8')
    print(hex_message)


def decode_message():
    encrypted_message = input("Introduce a message to decode: ")
    cipher = initialize_cipher()
    decrypted_message = cipher.decrypt(binascii.unhexlify(encrypted_message))
    original_message = unpad(decrypted_message, AES.block_size)
    print(original_message.decode('utf8'))


if __name__ == '__main__':
    code_message()
    decode_message()


# The message "9bc43d7ec1aa11f64302287b17be9f7b",
# with key "SeguridadInforma" and iv "SeguridadInforma",
# means "AESFuncionando".
