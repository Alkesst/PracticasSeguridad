from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pss
from Crypto.Hash import SHA256


def crear_RSAKey():
    key = RSA.generate(2048)
    return key


def guardar_RSAKey_Privada(fichero, RSAKey, password):
    key_cifrada = key.export_key(passphrase=password, pkcs=8, protection="scryptAndAES128-CBC")
    file_out = open(fichero, "wb")
    file_out.write(key_cifrada)
    file_out.close()


def cargar_RSAKey_Privada(fichero, password):
    key_cifrada = open(fichero, "rb").read()
    key = RSA.import_key(key_cifrada, passphrase=password)

    return key


def guardar_RSAKey_Publica(fichero, RSAKey):
    key_pub = key.publickey().export_key()
    file_out = open(fichero, "wb")
    file_out.write(key_pub)
    file_out.close()

def cargar_RSAKey_Publica(fichero):
    keyFile = open(fichero, "rb").read()
    key_pub = RSA.import_key(keyFile)

    return key_pub

def cifrarRSA_OAEP(cadena, key):
    datos = cadena.encode("utf-8")
    engineRSACifrado = PKCS1_OAEP.new(key)
    cifrado = engineRSACifrado.encrypt(datos)

    return cifrado

def descifrarRSA_OAEP(cifrado, key):
    engineRSADescifrado = PKCS1_OAEP.new(key)
    datos = engineRSADescifrado.decrypt(cifrado)
    cadena = datos.decode("utf-8")

    return cadena

def firmarRSA_PSS(texto, key_private):
    h = SHA256.new(texto.encode("utf-8")) # Ya veremos los hash la semana que viene
    print(h.hexdigest())
    signature = pss.new(key_private).sign(h)

    return signature

def comprobarRSA_PSS(texto, firma, key_public):
    h = SHA256.new(texto.encode("utf-8"))  # Ya veremos los hash la semana que viene
    print(h.hexdigest())
    verifier = pss.new(key_public)
    try:
        verifier.verify(h, firma)
        return True
    except (ValueError, TypeError):
        return False

# Main
# Crear clave RSA
# y guardar en ficheros la clave privada (protegida) y publica
password = "password"
fichero_privado = "rsa_key.pem"
fichero_publico = "rsa_key.pub"
key = crear_RSAKey()
guardar_RSAKey_Privada(fichero_privado, key, password)
guardar_RSAKey_Publica(fichero_publico, key)

# Cargar la clave RSA privada del fichero, y muestra ambas en pantalla
# (La estructura de la clave privada tambien guarda la clave publica)
key = cargar_RSAKey_Privada(fichero_privado, password)
print(key.publickey().export_key())
print(key.export_key())

# Cifrar y Descifrar con PKCS1 OAEP
cadena = "Lo desconocido es lo contrario de lo conocido. Pasalo."
cifrado = cifrarRSA_OAEP(cadena, key)
print(cifrado)
descifrado = descifrarRSA_OAEP(cifrado, key)
print(descifrado)

# Firmar y comprobar con PKCS PSS
firma = firmarRSA_PSS(cadena, key)

keypub = cargar_RSAKey_Publica(fichero_publico)
if comprobarRSA_PSS(cadena, firma, keypub):
    print("La firma es valida")
else:
    print("La firma es invalida")