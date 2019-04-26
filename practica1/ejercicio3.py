__author__ = "Alejandro Garau Madrigal"


def caesar_cipher(input_text: str, offset: int = 3) -> str:
    """
    The mighty function to cipher a text using caesar algorithm.
    :param input_text: text to cipher
    :param offset: value to shift. The default is 3
    :return: ciphered text
    """
    result = ''
    for current_char in input_text:
        ord_current = ord(current_char)
        if 65 <= ord_current <= 90:
            result += chr((((ord_current - 65) + offset) % 26) + 65)
        elif 97 <= ord_current <= 122:
            result += chr((((ord_current - 97) + offset) % 26) + 97)
        else:
            result += current_char
    return result


def caesar_decipher2(input_text: str, offset: int = 3) -> str:
    """
    Versión wena y gorda.
    :param input_text: texto a descrifrar
    :param offset: el offset
    :return: el texto descifrado
    """
    return caesar_cipher(input_text, (26 - offset))
