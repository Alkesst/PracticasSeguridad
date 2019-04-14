import base64

from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad


class DESCipher:
    """
        Class to cipher and decipher with a key using DES algorithm.
    """

    __BLOCK_SIZE_DES = 8

    def __init__(self, key) -> None:
        """
        Initializes the object with the key we will be using to cipher and decipher.
        :param key: the mighty key we will use.
        """
        super().__init__()
        if type(key) != bytes:
            key = key.encode('utf-8')
        self.__key = key

    def cipher(self, string_to_cipher, iv) -> bytes:
        """
        Cipher the input_string with DES algorithm using the IV vector and the key initialized in
        self.
        :param string_to_cipher: input string to cipher using DES
        :param iv: input vector
        :return: ciphered text
        """
        if type(string_to_cipher) != bytes:
            string_to_cipher = string_to_cipher.encode("utf-8")
        cipher = DES.new(self.__key, DES.MODE_CBC, iv)
        ciphered_text = cipher.encrypt(pad(string_to_cipher, self.__BLOCK_SIZE_DES))
        return ciphered_text

    def decipher(self, ciphered_input: bytes, iv) -> str:
        """
        Deciphers the input bytes using the IV vector and the DES algorithm. returns a legible string.
        :param ciphered_input: ciphered input in bytes
        :param iv: input vector
        :return: deciphered text
        """
        decipher_des = DES.new(self.__key, DES.MODE_CBC, iv)
        deciphered_text = unpad(decipher_des.decrypt(ciphered_input), self.__BLOCK_SIZE_DES).decode("utf-8", "ignore")
        return deciphered_text


def main():
    key = get_random_bytes(8)
    IV = get_random_bytes(8)
    datos = "HOLA MUNDO CON DES EN MODO CBC LOL!!!!!!!!!\nbruh"
    d = DESCipher(key)
    cifrado = d.cipher(datos, IV)
    descifrado = d.decipher(cifrado, IV)
    print('Texto legible cifrado: {}\nTexto cifrado: {}\nTexto descifrado: {}'.format(
        base64.b64encode(cifrado), cifrado, descifrado)
    )


if __name__ == '__main__':
    main()
