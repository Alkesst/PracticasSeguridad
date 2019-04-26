from Cryptodome.Hash import SHA512


RELATIVE_PATH = '/Users/alec/Documents/Universidad/Tercero/2Cuatri/Seguridad/{}'


def ejercicio1():
    # Ejercicio 1
    hash_object = SHA512.new()
    with open(RELATIVE_PATH.format('text.txt'), 'rb') as file:
        current_line = file.readline()
        while current_line != b'':
            hash_object.update(current_line)
            current_line = file.readline()
    hashed_lines = hash_object.digest()
    print(hashed_lines)
    print(hash_object.hexdigest())


def ejercicio2():
    pass


if __name__ == "__main__":
    ejercicio1()
    ejercicio2()
