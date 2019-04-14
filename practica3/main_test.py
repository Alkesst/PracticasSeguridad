from practica3.rsa import RSAObject

RELATIVE_PATH = '/Users/alec/Desktop/{}'


def main():
    rsa = RSAObject()
    rsa.create_key_pair()
    rsa.load_private_key(RELATIVE_PATH.format("private.pem"), "123456")
    rsa.load_public_key(RELATIVE_PATH.format("public.pem"))
    a = rsa.cipher("Vaya poya que tienes compae XD")
    print(a)
    b = rsa.decipher(a)
    print(b)
    a = rsa.sign("El mendizábal")
    print(a)
    print(rsa.check_sign("El mendizábal", a))


if __name__ == '__main__':
    main()
