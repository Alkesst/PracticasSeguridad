from practica1 import ejercicio1, ejercicio2, ejercicio3


def main():
    print(ejercicio1.basic_caesar_cipher("CIFRADO BASICO SOLO MAYUSCULAS"))
    print('Descifrando....')
    print(ejercicio1.caesar_decipher(ejercicio1.basic_caesar_cipher("CIFRADO BASICO SOLO MAYUSCULAS")))
    print('cifrando el siguiente texto: \t Ahora Soporta Tambien Minusculas')
    print(ejercicio2.caesar_cipher2('Ahora Soporta Tambien Minusculas'))
    print(ejercicio3.caesar_cipher('Y ahora soporta diferentes offsets!!!', 8))
    print(ejercicio3.caesar_decipher2(ejercicio3.caesar_cipher('Y ahora soporta diferentes offsets!!!', 8), 8))


if __name__ == '__main__':
    main()
