from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

__author__ = "Alejandro Garau Madrigal"


class AESCipher:
    """
    The mighty power of the class that represents the ciphering and deciphering
    strings using AES algorithm. We are using the AES-128 algorithm so
    the BLOCK_SIZE is 16 bytes, the key_length must be 16 bytes and the
    IV must be 16 bytes too.
    """
    __BLOCK_SIZE_AES = 16

    def __init__(self, key) -> None:
        super().__init__()
        if len(key) != 16:
            raise RuntimeError('Key length must be 16 bytes!')
        if type(key) != bytes:
            key = key.encode('utf-8')
        self.__key = key

    def cipher(self, to_cipher, iv) -> bytes:
        """
        Ciphers the input text using the AES-128 algorithm.
        :param to_cipher: text to cipher
        :param iv: input vector. It's size must be 128 bits, otherwise, an error is raised.
        :return: ciphered bytes.
        """
        if len(iv) != 16:
            raise RuntimeError('Initializer vector length must be 16 bytes!')
        if type(to_cipher) != bytes:
            to_cipher = to_cipher.encode('utf-8')
        aes = AES.new(self.__key, AES.MODE_CBC, iv)
        encrypted = aes.encrypt(pad(to_cipher, self.__BLOCK_SIZE_AES))
        return encrypted

    def decipher(self, to_decipher, iv) -> str:
        """
        Deciphers the input string using the AES-128 algorithm
        :param to_decipher: text to decipher
        :param iv: input vector
        :return: deciphered text
        """
        aes = AES.new(self.__key, AES.MODE_CBC, iv)
        deciphered = unpad(aes.decrypt(to_decipher), self.__BLOCK_SIZE_AES)
        return deciphered.decode('utf-8', 'ignore')


def main():
    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    a = AESCipher(key)
    print(a.cipher('ASEIS JEFA', iv))
    print(a.decipher(a.cipher('ASIES JEFA', iv), iv))


if __name__ == '__main__':
    main()
