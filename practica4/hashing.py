from Cryptodome.Hash import SHA512, HMAC


__author__ = "Alejandro Garau Madrigal"
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
    secret = b'S3cr3tK3y'
    hash_object = HMAC.new(secret, digestmod=SHA512)
    check = HMAC.new(secret, digestmod=SHA512)

    with open(RELATIVE_PATH.format('text.txt'), 'rb') as file:
        current_line = file.readline()
        while current_line != b'':
            hash_object.update(current_line)
            current_line = file.readline()
    mac = hash_object.hexdigest()

    message = b''
    with open(RELATIVE_PATH.format('text.txt'), 'rb') as file:
        current_line = file.readline()
        while current_line != b'':
            check.update(current_line)
            message += current_line
            current_line = file.readline()
    try:
        check.hexverify(mac)
        print("The message '%s' is authentic" % message)
    except ValueError:
        print("The message or the key is wrong")


if __name__ == "__main__":
    ejercicio1()
    ejercicio2()
