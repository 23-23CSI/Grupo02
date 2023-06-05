import os
import timeit
import random


# Reemplaza "ruta_de_la_carpeta" con la ruta de la carpeta que contiene los archivos
def leer():
    carpeta = "textos"

    lista_archivos = os.listdir(carpeta)
    lista_textos = []

    for archivo in lista_archivos:
        if archivo.endswith(".txt"):
            ruta_archivo = os.path.join(carpeta, archivo)
            with open(ruta_archivo, "r") as f:
                contenido = f.read()
                lista_textos.append(contenido)
    
   

    return   list(lista_textos)



def generarClave():
    numero_aleatorio = random.randint(4, 26)
    return numero_aleatorio


# XOR Cipher
def xor_cipher(message, key):
    encrypted_message = ""  # Variable para almacenar el mensaje cifrado
    for char in message:
        # Realiza la operación XOR entre el carácter y la clave y convierte el resultado en un nuevo carácter
        encrypted_char = chr(ord(char) ^ key)
        # Agrega el carácter cifrado al mensaje cifrado
        encrypted_message += encrypted_char
    return encrypted_message  # Devuelve el mensaje cifrado


def xor_decipher(encrypted_message, key):
    decrypted_message = ""  # Variable para almacenar el mensaje descifrado
    for char in encrypted_message:
        # Realiza la operación XOR entre el carácter cifrado y la clave para obtener el carácter original
        decrypted_char = chr(ord(char) ^ key)
        # Agrega el carácter descifrado al mensaje descifrado
        decrypted_message += decrypted_char
    return decrypted_message  # Devuelve el mensaje descifrado

def generarMensajeEImprimimir(mensaje, clave,boleano):
    if boleano:
        encrypted_message = xor_cipher(mensaje, clave)
        print("Mensaje encriptado:", encrypted_message)
    else:
        decrypted_message = xor_decipher(mensaje, clave)
        print("Mensaje desencriptado:", decrypted_message)

def main():
    lista_textos = leer()
    tiempo_ejecucion1 = timeit.timeit(leer, number=1)

    mensaje = lista_textos[5]
    clave = generarClave()
    tiempo_ejecucion2 = timeit.timeit(generarClave, number=1)

    tiempo_ejecucion3 = timeit.timeit(lambda: generarMensajeEImprimimir(mensaje, clave,True), number=1)
    
    encrypted_message = xor_cipher(mensaje, clave)
    tiempo_ejecucion4 = timeit.timeit(lambda: generarMensajeEImprimimir(encrypted_message, clave,False), number=1)

    print("Tiempo de ejecucion 1: ", tiempo_ejecucion1)
    print("Tiempo de ejecucion 2: ", tiempo_ejecucion2)
    print("Tiempo de ejecucion 3: ", tiempo_ejecucion3)
    print("Tiempo de ejecucion 4: ", tiempo_ejecucion4)

    print("Tiempo total= ",( tiempo_ejecucion1 +
          tiempo_ejecucion2 + tiempo_ejecucion3+tiempo_ejecucion4))



main()