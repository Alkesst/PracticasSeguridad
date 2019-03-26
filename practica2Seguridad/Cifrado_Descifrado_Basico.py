from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util import Counter
import base64

# Datos necesarios
BLOCK_SIZE_DES = 8  # Bloque de 64 bits
key = get_random_bytes(BLOCK_SIZE_DES)  # Clave aleatoria de 64 bits
IV = get_random_bytes(BLOCK_SIZE_DES)  # IV aleatorio de 64 bits
data = "Hola Mundo con DES en modo CBC".encode("utf-8")  # Datos a cifrar
print(data)

# Creamos un mecanismo de cifrado DES en modo CBC con una inicializacion IV
cipher = DES.new(key, DES.MODE_CBC, IV)

# Ciframos, haciendo que data sea multiplo del tamaño de bloque
ciphertext = cipher.encrypt(pad(data, BLOCK_SIZE_DES))

# Mostramos el cifrado por pantalla en modo binario y en modo base 64
print(ciphertext)
encoded_ciphertext = base64.b64encode(ciphertext)
print(encoded_ciphertext)

# Creamos un mecanismo de (des)cifrado DES en modo CBC con una inicializacion IV
# Ambos, cifrado y descifrado, se crean de la misma forma
decipher_des = DES.new(key, DES.MODE_CBC, IV)

# Desciframos, eliminamos el padding, y recuperamos la cadena
new_data = unpad(decipher_des.decrypt(ciphertext), BLOCK_SIZE_DES).decode("utf-8", "ignore")

# Imprimimos los datos descifrados
print(new_data)

