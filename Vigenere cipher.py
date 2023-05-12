# Vigenere cypher

def vigenere_shift(message, alphabet, key, mode):
    shifted_chars = []
    for key_index, letter in enumerate(message):
        shift = alphabet.index(key[key_index % len(key)]) * mode
        if letter.lower() not in alphabet:
            shifted_letter = letter
        else:
            sifted_letter_index = (alphabet.index(letter.lower()) + shift) % len(alphabet)
            if letter.isupper():
                shifted_letter = alphabet[sifted_letter_index].upper()
            else:
                shifted_letter = alphabet[sifted_letter_index]
        shifted_chars.append(shifted_letter)
    return "".join(shifted_chars)


def decode_message():
    encoded_message = input("Introduce a message to decode: ")
    key = input("Introduce the key: ")
    print(vigenere_shift(encoded_message, ALPHABET, key.lower(), -1))


def code_message():
    message = input("Introduce a message to code: ")
    key = input("Introduce the key: ")
    print(vigenere_shift(message, ALPHABET, key.lower(), 1))


ALPHABET = "abcdefghijklmnopqrstuvwxyz"

if __name__ == '__main__':
    code_message()
    decode_message()


# The message "QqmiaiiiYmisqmwmxijs" is coded with key "Vigenere"
# and means "VigenereDecodificado".
