from cryptography.fernet import Fernet
import os


# Extension de los archivos que se encritparon
extension = 'IONOS'


# funcion que obtiene la llave para descifrar archivos 
def cargar_key():
    return open('key.key', 'rb').read()


# funcion que descifra los archivos y eliminas las extenciones 
def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        if item.endswith(extension):

            item_orig = item.rsplit('.', 1)[0]
            print(item)
            os.rename(item, item_orig)
            item = item_orig

            with open(item, 'rb') as file:
                encrypted_data = file.read()

            decrypted_data = f.decrypt(encrypted_data)

            with open(item, 'wb') as file:
                file.write(decrypted_data)

        else:
            print('Error decrypting "%s"' %str(item))


if __name__ == '__main__':

    try:

        # path que se va a descifrar
        path_to_decrypt = '/home/randi/python/prueba2/'

        # eliminacion del archivo de advertencia
        os.remove(path_to_decrypt + '\\README.txt')

        # obtencion de archivos para descifrar "items".
        items = os.listdir(path_to_decrypt)
        full_path = [path_to_decrypt + '//' + item for item in items]

        # traer key del cifrado creada.
        key = cargar_key()

        # descifrado de archivos .
        decrypt(full_path, key)

    except Exception as e:
        print(e)
