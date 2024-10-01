import random
categorias_palabras = {
  "animales": [ "gato", "perro", "elefante", "tigre", "leon", "jirafa", "cebra", "mono", "delfin", "rinoceronte" ],
  "alimentos": [ "manzana", "banana", "zanahoria", "fresa", "aguacate", "brocoli", "naranja", "mango", "piña", "lechuga" ],
  "paises": [ "honduras", "colombia", "argentina", "brasil", "mexico", "chile", "peru", "venezuela", "ecuador", "uruguay" ],
  "colores": [ "rojo", "azul", "verde", "amarillo", "naranja", "morado", "blanco", "negro", "rosa", "gris" ],
  "deportes": [ "futbol", "baloncesto", "tenis", "natacion", "voleibol", "golf", "beisbol", "atletismo", "hockey", "boxeo" ],
  "frutas": [ "manzana", "pera", "uva", "kiwi", "papaya", "sandia", "cereza", "durazno", "melon", "limon" ],
  "vehiculos": [ "carro", "bicicleta", "camion", "avion", "barco", "motocicleta", "tren", "helicoptero", "submarino", "patineta" ],
  "instrumentos": [ "guitarra", "piano", "bateria", "violin", "flauta", "trompeta", "arpa", "clarinete", "saxofon", "tambor" ],
  "profesiones": [ "doctor", "ingeniero", "maestro", "abogado", "arquitecto", "enfermera", "policia", "bombero", "chef", "periodista" ],
  "marcas": [ "nike", "adidas", "microsoft", "pepsi", "samsung", "apple", "sony", "mcdonalds", "starbucks", "google" ]
}
categorias ={
    "1": "animales",
    "2": "alimentos",
    "3": "paises",
    "4": "colores",
    "5": "deportes",
    "6": "frutas",
    "7": "vehiculos",
    "8": "instrumentos",
    "9": "profesiones",
    "10": "marcas",
}
print("¡Bienvenido al juego de adivinanza de palabras!")

def obtener_palabra_aleatoria():
    while True:
        print("\n1. Animales\n2. Alimentos\n3. Países\n4. Colores\n5. Deportes\n6. Frutas\n7. Vehículos\n8. Instrumentos\n9. Profesiones\n10. Marcas")
        
        numeroCategoria = input("Ingrese el número de la categoría: ")
        
        if numeroCategoria in categorias:  # validamos que sea una key de 'categorias'
            categoria_seleccionada = categorias[numeroCategoria]
            lista_de_palabras = categorias_palabras[categoria_seleccionada]
            palabra_aleatoria = random.choice(lista_de_palabras)

            print(f"Has escogido la categoría {categoria_seleccionada.upper()}")
            print(f"\nIntentos Permitidos: {obtener_intentos(palabra_aleatoria)}")
            print("Tienes que adivinar la palabra de esta categoría.")
            return palabra_aleatoria
        else:
            print("Por favor ingrese un número válido entre 1 y 10.")  

def obtener_intentos(palabra_secreta):
    return round((len(palabra_secreta) / 2) + 1)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = " "
    for letra in palabra_secreta: # para cada letra en la palabra, si ya ha sido adivinada, se muestra. Si no, se muestra un guion bajo.
        if letra in letras_adivinadas:
            tablero += letra
        else:
            tablero += "_"
    print(tablero)

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos_restantes = obtener_intentos(palabra_secreta)

    while intentos_restantes>0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra = input("Ingrese una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya ingresaste esa letra, intenta con otra")
            continue # para saltarse el resto del codigo de esta iteracion y volver al inicio del bucle

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            if set(letras_adivinadas)==set(palabra_secreta):
                print(f"Felicidades! Ganaste! La palabra es: {palabra_secreta.upper()}")
                break
        else:
            intentos_restantes-=1
            print(f"Letra incorrecta. Te quedan {intentos_restantes}")
        
    if intentos_restantes == 0:
        print(f"Lo siento, la palabra era {palabra_secreta.upper()}.")

jugar_ahorcado()