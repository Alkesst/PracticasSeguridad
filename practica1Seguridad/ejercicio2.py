def caesar_cipher2(input_text: str) -> str:
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
        elif 97 <= ord_current <= 122:
            result += chr((((ord_current - 97) + 3) % 26) + 97)
        else:
            result += current_char
    return result
