from practica3.rsa import RSAObject
from Cryptodome.Random import get_random_bytes


__author__ = "Alejandro Garau Madrigal"


RELATIVE_PATH = '/Users/alec/Desktop/{}'


def send_protocol_using_rsa(message_to_send):
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

    ciphered = b.cipher(message_to_send)
    print("A ciphered the message using the public key of client B.")
    print(ciphered)
    print("Bytes to send: {}".format(len(ciphered)))
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
    send_protocol_using_rsa("Hola Amigos de la Seguridad")
    print("\n\n\n\n\n")
    print("Now we will send a session key using RSA.")
    key = get_random_bytes(16)
    print(key)
    send_protocol_using_rsa(key)
    ### Por algún motivo no funciona y devuelve NONE
