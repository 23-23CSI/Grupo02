import hashlib
import os
import timeit
import random

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

def generarClave(datos,sal):
    # Generar una sal aleatoria si no se proporciona una
    if sal is None:
        sal = os.urandom(16)  # Generar una sal de 16 bytes
    # Concatenar la sal con los datos
    datos_con_sal = sal + datos.encode('utf-8')

    return datos_con_sal

def encriptar_datos_con_sal(datos_con_sal,sal):
    # Generar un hash único utilizando la función hash SHA-256
    hash_obj = hashlib.sha256()
    hash_obj.update(datos_con_sal)
    hash_digest = hash_obj.hexdigest()
    
    # Devolver el hash encriptado y la sal utilizada
    return hash_digest, sal

def generarMensajeEImprimimir(clave,sal):
    hash_encriptado, sal_utilizada = encriptar_datos_con_sal(clave,sal)
    print("Datos encriptados:", hash_encriptado)
    print("Sal utilizada:", sal_utilizada)

def main():
    lista_textos = leer()
    tiempo_ejecucion1 = timeit.timeit(leer, number=1)

    mensaje = lista_textos[4]
    sal = b'\x95\x1b\xf9\x1f\xb2\x11\xeb\xa3r\x99\xa8\xec&\xf2\x10'  # Sal predefinida
    clave=generarClave(mensaje, sal)
    tiempo_ejecucion2 = timeit.timeit(lambda: generarClave(mensaje, sal), number=1)

    tiempo_ejecucion3 = timeit.timeit(lambda: generarMensajeEImprimimir(clave, sal), number=1)
    
    print("Tiempo de ejecucion 1: ", tiempo_ejecucion1)
    print("Tiempo de ejecucion 2: ", tiempo_ejecucion2)
    print("Tiempo de ejecucion 3: ", tiempo_ejecucion3)
    print("Tiempo total= ",( tiempo_ejecucion1 +tiempo_ejecucion2 + tiempo_ejecucion3))

main()