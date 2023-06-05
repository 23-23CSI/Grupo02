import random
import os
import timeit

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



# Función para calcular el inverso multiplicativo módulo p
def multiplicative_inverse(a, p):
    for i in range(1, p):
        if (a * i) % p == 1:
            return i
    return None

# Función para generar una clave privada aleatoria
def generate_private_key(p):
    return random.randint(2, p - 2)

# Función para generar una clave pública a partir de la clave privada
def generate_public_key(g, private_key, p):
    return pow(g, private_key, p)

# Función para cifrar un mensaje
def encrypt(message, public_key, g, p):
    cipher_text = []
    k = random.randint(2, p - 2)
    s = pow(public_key, k, p)
    for char in message:
        cipher_text.append((pow(g, k, p), (ord(char) * s) % p))
    
    return cipher_text

# Función para descifrar un mensaje cifrado
def decrypt(cipher_text, private_key, p):
    decrypted_text = ""
    for c1, c2 in cipher_text:
        s = pow(c1, private_key, p)
        decrypted_text += chr((c2 * multiplicative_inverse(s, p)) % p)
    #print("\nMensaje descifrado:", decrypted_text)
    return decrypted_text


def generarMensajeEImprimimir(message, key, g, p,boleano):
    if boleano:
        cipher_text = encrypt(message, key, g, p)
        print("Mensaje encriptado:",cipher_text)

        #for c1, c2 in cipher_text:
         #   print("({}, {})".format(c1, c2))
    else:
        decrypted_text=decrypt(message, key, p)
        print("Mensaje desencriptado:", decrypted_text)




def main():
    # Mensaje original
    lista_textos = leer()
    tiempo_ejecucion1 = timeit.timeit(leer, number=1)
    
    message =  lista_textos[5]  

    # Parámetros del cifrado ElGamal
    p = 353 # Número primo grande
    g = 3   # Generador del grupo multiplicativo módulo p

    # Generar clave privada y clave pública
    private_key = generate_private_key(p)
    public_key = generate_public_key(g, private_key, p) 
    tiempo_ejecucion2_1 = timeit.timeit(lambda: generate_private_key(p), number=1)
    tiempo_ejecucion2_2 = timeit.timeit(lambda: generate_public_key(g, private_key, p), number=1)

   
    cipher_text = encrypt(message, public_key, g, p)
    #for c1, c2 in cipher_text:
    #        print("({}, {})".format(c1, c2))

    tiempo_ejecucion3 = timeit.timeit(lambda: generarMensajeEImprimimir(message, public_key, g, p,True), number=1)

    # Descifrar el mensaje cifrado
    
    decrypted_text=decrypt(cipher_text, private_key, p)
    #print("Mensaje desencriptado:", decrypted_text)
    
    tiempo_ejecucion4 = timeit.timeit(lambda: generarMensajeEImprimimir(cipher_text, private_key, g ,p, False), number=1)
    print("Tiempo de ejecucion 1: ", tiempo_ejecucion1)
    print("Tiempo de ejecucion 2: ", tiempo_ejecucion2_1 +tiempo_ejecucion2_2)    
    print("Tiempo de ejecucion 3: ", tiempo_ejecucion3)
    print("Tiempo de ejecucion 4: ", tiempo_ejecucion4)
    print("Tiempo de ejecucion Total: ", tiempo_ejecucion1+tiempo_ejecucion2_1  +tiempo_ejecucion2_2 +tiempo_ejecucion3+tiempo_ejecucion4)

        
main()