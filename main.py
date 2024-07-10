#Se importan los diccionarios y la función dibujar ahorcado desde otros archivos diccionario_1, diccionario_2
#Contienen las palabras del juego
#dibujar_ahorcado se va a encargar de mostrar el tablero

from palabras import diccionario_2, diccionario_1
from ahorcado_diagramas import dibujar_ahorcado
import random


#Esta función recibe la palabra y las letras adivinadas hasta el momento, y devuelve la versión oculta de la palabra, reemplazando las letras no adivinadas por guiones bajos.
def mostrar_palabra(palabra, letras_adivinadas):
    palabra_oculta = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += '_'
    return palabra_oculta

#Esta función muestra al jugador las opciones de categoría y solicita la entrada del jugador. Si la entrada no es válida, solicita al jugador que elija de nuevo.
def obtener_categoria():
    print("Elige una categoría:")
    print("1. EQUIPOS Y PILOTOS F1.")
    print("2. EQUIPOS Y ESTADIOS DE LA LIGA MX.")

    print()
    print()

    while True:
        opcion = input("Ingrese el número de la categoría deseada: ")
        if opcion in ["1", "2",]:
            return int(opcion)
        else:
            print("Opción inválida. Por favor, elija un número válido.")

#Esta función utiliza obtener_categoria para obtener la categoría elegida por el jugador y luego selecciona una palabra aleatoria de esa categoría en el diccionario proporcionado.
def obtener_palabra_aleatoria(diccionario):
    categoria_elegida = obtener_categoria()
    categoria_seleccionada = list(diccionario.keys())[categoria_elegida - 1]
    return random.choice(diccionario[categoria_seleccionada])

#En esta sección, inicializas algunas variables, seleccionas una palabra aleatoria y muestras un mensaje de bienvenida.
def jugar_ahorcado():
    intentos_maximos = 6
    letras_adivinadas = []

    diccionarios = [diccionario_2, diccionario_1]
    palabra = obtener_palabra_aleatoria(random.choice(diccionarios))

    nombre = input("INTRODUCE TU NOMBRE: ")
    print()
    print("***************************************************")
    print(f"***   BIENVENIDO AL JUEGO DEL AHORCADO, {nombre}   ***")
    print(f"    ***   PREPARATE PARA ADIVINAR TU PALABRA   ***")
    print(f"              ***   MUCHA SUERTE   ***")
    print("***************************************************")

#Este bucle principal maneja la lógica del juego. Solicita letras al jugador, verifica si son correctas o incorrectas, actualiza la visualización de la palabra y verifica si el jugador ha ganado o perdido.
    while True:
        letra_usuario = input("\nIngresa una letra: ").lower()

        if letra_usuario in letras_adivinadas:
            print("Ya has ingresado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra_usuario)

        if letra_usuario not in palabra:
            intentos_maximos -= 1
            dibujar_ahorcado(intentos_maximos)
            print(f"¡Letra incorrecta! Te quedan {intentos_maximos} intentos.")
        else:
            print("¡Letra correcta!")

        palabra_oculta = mostrar_palabra(palabra, letras_adivinadas)
        print(f"Palabra actual: {palabra_oculta}")

        if '_' not in palabra_oculta:
            print("¡Felicidades! Has adivinado la palabra.")
            break

        if intentos_maximos == 0:
            print(f"¡Oh no! Te has quedado sin intentos. La palabra era: {palabra}")
            break

#Finalmente, esta línea ejecuta la función jugar_ahorcado
if __name__ == "__main__":
    jugar_ahorcado()