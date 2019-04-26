from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Cryptodome.Hash import SHA256
from Crypto.Signature import pss

__author__ = "Alejandro Garau Madrigal"


class RSAObject(object):
    def __init__(self):
        """Inicializa un objeto RSA, sin ninguna clave"""
        # Nota: Para comprobar si un objeto (no) ha sido inicializado, hay
        # que hacer "if self.public_key is None:"
        self.__key = None
        self.__public_key = None
        self.__private_key = None

    def create_key_pair(self):
        """Crea un par de claves publico/privada, y las almacena dentro de la instancia"""
        self.__key = RSA.generate(2048)
        self.__private_key = self.__key  # va, que es sin el .export_key. El self.__key es en sí la clave privada nice.
        self.__public_key = self.__key.publickey()

    def save_private_key(self, file, password):
        """Guarda la clave privada self.private_key en un fichero file, usando una contraseña
            password
       """
        private_key_but_ciphered = self.__key.export_key(passphrase=password, pkcs=8, protection="scryptAndAES128-CBC")
        with open(file, 'wb') as f:
            f.write(private_key_but_ciphered)

    def load_private_key(self, file, password):
        """Carga la clave privada self.private_key de un fichero file, usando una contraseña
       password"""
        with open(file, 'rb') as f:
            self.__private_key = RSA.import_key(f.read(), passphrase=password)

    def save_public_key(self, file):
        """Guarda la clave publica self.public_key en un fichero file"""
        with open(file, 'wb') as el_fichero:
            el_fichero.write(self.__public_key.export_key())

    def load_public_key(self, file):
        """Carga la clave publica self.public_key de un fichero file"""
        with open(file, 'rb') as el_fichero:
            self.__public_key = RSA.import_key(el_fichero.read())

    def cipher(self, datos):
        """Cifra el parámetro datos (de tipo binario) con la clave self.public_key, y devuelve
        el resultado. En caso de error, se devuelve None"""
        if type(datos) != bytes:
            datos = datos.encode('utf-8')
        engineRSACifrado = PKCS1_OAEP.new(self.public_key)
        try:
            return engineRSACifrado.encrypt(datos)
        except ValueError:
            return None

    def decipher(self, cifrado):
        """Descrifra el parámetro cifrado (de tipo binario) con la clave self.private_key, y
       Devuelve el resultado (de tipo binario). En caso de error, se devuelve None"""
        if type(cifrado) != bytes:
            cifrado = cifrado.encode('utf-8')
        engineRSADescifrado = PKCS1_OAEP.new(self.private_key)
        try:
            datos = engineRSADescifrado.decrypt(cifrado)
            return datos
        except ValueError:
            return None

    def sign(self, datos):
        """Firma el parámetro datos (de tipo binario) con la clave self.private_key, y devuelve
       el resultado. En caso de error, se devuelve None."""
        if type(datos) != bytes:
            datos = datos.encode("utf-8")
        hashed = SHA256.new(datos)  # Ya veremos los hash la semana que viene
        print(hashed.hexdigest())
        signature = pss.new(self.__private_key).sign(hashed)
        return signature

    def check_sign(self, text, signature):
        """Comprueba el :param text: (de tipo binario) con respecto a una firma signature
        (de tipo binario), usando para ello la clave self.public_key.
        :param text: texto a comprobar
        :param signature: firma
        :return: True si la comprobacion es correcta, o False en caso contrario o
        en caso de error.
        """
        if type(text) != bytes:
            text = text.encode("utf-8")
        hashed = SHA256.new(text)
        print(hashed.hexdigest())
        verifier = pss.new(self.public_key)
        try:
            verifier.verify(hashed, signature)
            return True
        except (ValueError, TypeError):
            return False

    @property
    def public_key(self):
        return self.__public_key

    @property
    def private_key(self):
        return self.__private_key
