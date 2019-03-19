def basic_caesar_cipher(input_text: str) -> str:
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
            result += chr((((ord_current - 65) + 3) % 26) + 65)
        else:
            result += current_char
    return result


def caesar_decipher(input_text: str) -> str:
    """
    Versión cutre de descrifrar. La versión wena y gorda está en el ejercicio 3
    :param input_text:
    :return:
    """
    result = ''
    for current_char in input_text:
        ord_current = ord(current_char)
        if 65 <= ord_current <= 90:
            result += chr((((ord_current - 65) - 3) % 26) + 65)
        else:
            result += current_char
    return result
