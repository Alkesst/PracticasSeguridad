__author__ = "Alejandro Garau Madrigal"
from practica3.rsa import RSAObject

RELATIVE_PATH = '/Users/alec/Desktop/{}'


def main():
    a = RSAObject()
    print("Created client A")
    b = RSAObject()
    print("Created client B")
    b.create_key_pair()
    print("Generated a key pair for the client B")
    b.save_public_key(RELATIVE_PATH.format("b_public.pem"))
    b.save_private_key(RELATIVE_PATH.format("b_private.pem"), "1234")
    print("Saved the keys for client b in {}".format(RELATIVE_PATH.format("")))
    a.create_key_pair()
    print("Generated a key pair for the client A")
    a.save_public_key(RELATIVE_PATH.format("a_public.pem"))
    a.save_private_key(RELATIVE_PATH.format("a_private.pem"), "1234")
    print("Saved the keys for client a in {}".format(RELATIVE_PATH.format("")))

    # Ciframos el mensaje:

    ciphered = b.cipher("Hola Amigos de la Seguridad")
    print("A ciphered the message using the public key of client B.")
    print(ciphered)

    s = a.sign(ciphered)
    print("Client A signed the content using his own public key.")
    print("Sending ciphered and signed text to B client...")
    # Se lo """""""""mandamos""""""""" al cliente B.
    if a.check_sign(ciphered, s):
        print("The sign is correct. Client A has sent this information.\n"
              "Deciphered message: {}".format(b.decipher(ciphered)))
    else:
        print("The sender of this content is not the client A. Untrusted source.\nAborting...")


if __name__ == '__main__':
    main()
