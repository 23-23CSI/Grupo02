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
    numero_aleatorio = random.randint(1, 20)
    return numero_aleatorio


#Caesar Cipher
def cifrado_cesar(texto, desplazamiento):
    resultado = ""  # Variable para almacenar el resultado cifrado o descifrado
    for caracter in texto:  # Itera sobre cada carácter del texto
        if caracter.isalpha():  # Comprueba si el carácter es una letra
            if caracter.isupper():  # Comprueba si el carácter es una letra mayúscula
                codigo = ord('A')  # Obtiene el valor ASCII de 'A'
            else:
                codigo = ord('a')  # Obtiene el valor ASCII de 'a'
            nuevo_caracter = chr(codigo + (ord(caracter) - codigo + desplazamiento) % 26)
            # Calcula el valor ASCII del nuevo carácter cifrado o descifrado
            # La fórmula (ord(caracter) - codigo + desplazamiento) % 26 realiza el desplazamiento circular en el alfabeto
            # chr(codigo + ...) convierte el valor ASCII resultante en el nuevo carácter
            resultado += nuevo_caracter  # Agrega el nuevo carácter al resultado
        else:
            resultado += caracter  # Si el carácter no es una letra, se mantiene sin cambios
    return resultado  # Devuelve el resultado cifrado o descifrado


def imprimirResultado(texto, desplazamiento):
    mensaje = cifrado_cesar(texto, desplazamiento)
    print(mensaje)

def main():
        lista_textos = leer()
        tiempo_ejecucion1 = timeit.timeit(leer, number=1)
        mensaje = lista_textos[5]                                                                                         
        clave = generarClave()
        tiempo_ejecucion2 = timeit.timeit(generarClave, number=1)

        encrypted_message =  cifrado_cesar(mensaje, clave)
        print("Mensaje encriptado:", encrypted_message)

        tiempo_ejecucion3 = timeit.timeit(lambda: imprimirResultado(mensaje, clave), number=1)


        decrypted_message = cifrado_cesar(encrypted_message, - clave)
        print("Mensaje desencriptado:", decrypted_message)

        tiempo_ejecucion4 = timeit.timeit(lambda: imprimirResultado(encrypted_message, -clave), number=1)
        print("Tiempo de ejecucion 1: ", tiempo_ejecucion1)
        print("Tiempo de ejecucion 2: ", tiempo_ejecucion2)
        print("Tiempo de ejecucion 3: ", tiempo_ejecucion3)
        print("Tiempo de ejecucion 4: ", tiempo_ejecucion4)

        print("Tiempo total= ",( tiempo_ejecucion1 +
          tiempo_ejecucion2 + tiempo_ejecucion3+tiempo_ejecucion4))

main()