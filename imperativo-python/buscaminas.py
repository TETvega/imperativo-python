import random
import os
import sys


# posibles   ʘ ʘ  ■ ʘ ■ □   

def instructions():
    print("""
        =================== INSTRUCCIONES DEL BUSCAMINAS EN CONSOLA ===================

        Objetivo del juego:
        El objetivo del juego es descubrir todas las casillas que no contienen minas. 
        Si descubres una mina, pierdes el juego. También puedes marcar casillas como minas 
        para evitar abrirlas accidentalmente.

        Cómo jugar:

        Tablero de juego:
        - Al iniciar el juego, deberás ingresar el tamaño del tablero con dos números: 
        n (número de columnas) y m (número de filas).
        - El tablero se generará aleatoriamente con minas, ocupando aproximadamente el 25%% de las casillas.

        Coordenadas de movimiento:
        - Para jugar, deberás ingresar las coordenadas de la casilla que deseas abrir o marcar.
        Las coordenadas se ingresan en el formato x, y, donde:
        - x es el número de la col (horizontal).
        - y es el número de la row (vertical).
        - Ejemplo: Para abrir la casilla en la col 2, row 3, ingresarías: 2 3.

        Acciones en la casilla:
        - Luego de ingresar las coordenadas, deberás indicar qué acción deseas realizar en la casilla:
        - 0: Indica que quieres descubrir la casilla. 
            Solo puedes descubrir una casilla si no ha sido marcada previamente como una mina.
        - 1: Indica que quieres marcar la casilla como una mina. 
            Puedes usar esta opción para marcar una casilla sospechosa de contener una mina.
            Si una casilla ya ha sido marcada como mina, puedes ingresar 1 de nuevo para desmarcarla.

        Reglas adicionales:
        - No puedes descubrir una casilla que ya has descubierto. 
        El sistema te avisará si intentas hacerlo.
        - Puedes marcar o desmarcar cualquier casilla en cualquier momento, incluso si ya la habías marcado antes.
        - Si descubres una casilla con una mina, pierdes el juego inmediatamente.
        - El juego termina cuando todas las casillas sin minas han sido descubiertas.

        Salir del juego:
        - En cualquier momento puedes salir del juego escribiendo 'exit'.

        Ejemplo de jugada:
        - Si estás jugando en un tablero de 5x5 (5 columnas y 5 filas):

        Ingresa las coordenadas y la acción:
        - 2 3 0 -> Abre la casilla en la col 2, row 3.
        - 4 5 1 -> Marca la casilla en la col 4, row 5 como mina.
        - 4 5 0 -> Desmarca la casilla en la col 4, row 5 (la casilla ahora está libre y su contenido se mostrara).

        Si en cualquier momento decides dejar el juego, ingresa el comando 'exit'.

        ===============================================================================
        """)
    os.system("pause")


# Funcion para pedir un numero entero y lo valida
def insertValidNumber(msg):
    while True:
            number = int(input(msg))
            if number>=2:
                return number
            print("Debes ingresar un numero util 2,3,4,5,6,7,8,9......\n Intentalo de nuevo.")
            os.system("pause")
            os.system("cls")

#Funcion para imprimir la matriz
def printMatrix(matrix,rows):
    for i in range(rows):
        #str(cell) para hacer cada celda en string
        # :>n   para alinear n caracteres a la derecha
        # ' '.join para unir todos los elementos de la row con un espacio de por medio
        # lo dentro del join se conoce como expresion generadora
        formatted_row = ' '.join(f'{str(cell) :>3}' for cell in matrix[i])
        print(formatted_row)
#Funcion para ingresar un numero desde 1 hasta el limite impuesto
def validNumber(msg,limit):
    while True:
            number = int(input(msg))
            if (number>=1 and number <=limit) :
                return number
            print("Ingrese un numero desde 1 hasta %d" % limit)
            os.system("pause")
            os.system("cls")
def validFlag(msg):
     while True:
            number = int(input(msg))
            if number==1:
                return number
            if number ==2:
                return number
            
            print("Ingrese 1 para marcar Bandera\nIngrese 2 para mostrar la casilla \n\n Intentalo de nuevo.")
            os.system("pause")
            os.system("cls")
#Funcion Principal del Juego
def game():
    
        
    rows = insertValidNumber("Ingrese el numero de Filas:  ")
    cols = insertValidNumber("Ingrese el numero de Columnas:  ")

    malla = []
    matrixA = []
    matrixB=[]
    opencells=0
    # se rellana la malla con los datos, 0 no se ha hecho nada, 1 para celdas con banderas y -1 para celdas mostradas
    for i in range ((rows)):
        malla.append([0]*cols)
    print(malla)
    # se rellenan las celdas con 0 para la matriz primera y con casilla para la inversa de juego
    for i in range(rows):
        matrixA.append([0]*cols)
        matrixB.append(["□"]*cols)
    # se reellna la matriz con minas
    matrixA =createGame(rows,cols , matrixA)
    totalMines = int((rows*cols) / 4)
    flags = totalMines
    insertedFlags=0
    print("Juego Creado con exito\n Buena Suerte ")
    os.system("pause")
    os.system("cls")
    while True :
        os.system("cls")
        print(f"El numero de bombas es de: {totalMines}\n El numero de Banderas Restantes es de {flags-insertedFlags}")
        printMatrix(matrixB,rows)
        #ingreso de las coordenadas
        while True:
            x = validNumber("Ingresa la Coordenada X: ", cols)
            y = validNumber("Ingresa la Coordenada Y: ", rows)
            flag = validFlag("1 - Bandera\n2 - Mostrar Casilla\n:  ")
            #https://realpython.com/python-string-formatting/
            print(f"x: {x}, y: {y}, flag: {flag}")

            # si es 0 no ha sido descubierta la casilla
            # si es 1 y la bandera es 2 es por que tenia una bandera y se va a descubrir

            if (malla[y - 1][x - 1] == 0 or malla[y - 1][x - 1] == 1) and flag == 2:
                print(f"La coordenada es: x: {x}, y: {y}")
                break
            if (malla[y - 1][x - 1] == 0 or malla[y - 1][x - 1] == 1) and flag == 1 and insertedFlags < flags:
                break

            print(f"la coordenada {x} , {y} ya se ha mostrado elige otra")
            os.system("pause")
        #colocando bandera
        if(flag==1):
            matrixB[y-1][x-1] = "X"
            insertedFlags+=1
            malla[y-1][x-1] = 1
        #mostrando casilla diferente de una bomba
        if (matrixA[y-1][x-1] != "*" and flag==2):
            #mostrando la casilla antes marcada como bomba y otorgando una bandera nuevamente
            if(matrixB[y-1][x-1] =="X" ):
                insertedFlags -= 1
            matrixB[y-1][x-1] = matrixA[y-1][x-1]
            malla[y-1][x-1] = -1
            opencells+=1

            if (opencells ==  (rows*cols)-totalMines):
                os.system("cls")
                print(f"Felicitaciones GANASTE")
                printMatrix(matrixA,rows)
                os.system("pause")
                break

        # mostrando la casilla con la bomba el juego termino
        if (matrixA[y-1][x-1] == "*" and flag==2):
            matrixB[y-1][x-1] = matrixA[y-1][x-1]
            malla[y-1][x-1] = -1
        
            os.system("cls")
            print(f"GAME OVERRRRR")
            print(f"en la coordenada {x} , {y} se encuentra una Bomba")

            printMatrix(matrixA,rows)
            os.system("pause")
            break


        

    
    #printMatrix(matrixA,rows)
    


def createGame(rows,cols,matrixA):
    cells = rows * cols
    totalMines = int(cells / 4)

    # Colocar minas aleatoriamente
    mines = 0
    while   mines < totalMines:
        # se crea para x una coodenada desde 0 hasta el limite de x lo mismo para y
        row = random.randint(0, rows-1)
        col = random.randint(0, cols-1)
        
        # Colocar mina si la celda esta vacía
        if matrixA[row][col] != "*":
            matrixA[row][col] = "*"
            mines += 1
            
            # Actualizar los numeros de las celdas adyacentes
            # en un rando desde una fila antes de la fila normal hasta una fila despues de la fila normal
            for i in range(row - 1, row + 2):
                # en un rango de columnas de    x-1 , x , x+1
                #       tenemos asegurado un rango 3*3

                for j in range(col - 1, col + 2):

                    # en un rango de 0 hasta el limite de x,  y de o hasta el limite de y
                    # es para que la coordenada (x,y) este dentro del limite ademas que no sea una bomba
                    if 0 <= i < rows and 0 <= j < cols and matrixA[i][j] != "*":
                        matrixA[i][j] += 1
    return matrixA

def main():
    i = 0
    while i != 1 :
        print("""
          ===================  BUSCAMINAS EN CONSOLA ===================
        Objetivo del juego:
        El objetivo del juego es descubrir todas las casillas que no contienen minas. 
        Si descubres una mina, pierdes el juego. También puedes marcar casillas como minas 
        para evitar abrirlas accidentalmente.\n\n\n""")
        option = int (input("Ingresa 1 para Jugar \nIngresa 2 para salir\nIngresa 3 para ver instruciones\n"))

        match(option):
            case 1: 
                os.system("cls")
                game()
            case 2:
                sys.exit()
            case 3: 
                os.system("cls")
                instructions()
            case other:
                print("Opcion Invalida")
                os.system("pause")
        os.system("cls")

            
        

main()



# Enteros
edad = 25
anio = 2023
# flotantes 
medio = 0.5
# Strings
nombre = "Juan"
mensaje = "Hola, ¿cómo estás?"
# Lista de enteros
numeros = [1, 2, 3, 4, 5]
# Lista de strings
nombres = ["Juan", "Ana", "Luis"]
# Lista mixta
mi_lista = [1, "Hola", True, 3.14]





# Diccionario que representa un objeto
persona = {
    "nombre": "Pedro",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceso a valores de un diccionario
print(persona["nombre"])  # Pedro
# Función sin parámetros y sin retorno
def saludar():
    print("Hola, bienvenido!")

# Función con parámetros
def sumar(a, b):
    return a + b

# Función con parámetros por defecto
def presentar(nombre="Desconocido"):
    print(f"Hola, me llamo {nombre}")

# Llamadas a las funciones
saludar()  # Imprime: Hola, bienvenido!
print(sumar(3, 4))  # Imprime: 7
presentar("Carlos")  # Imprime: Hola, me llamo Carlos
presentar()  # Imprime: Hola, me llamo Desconocido
# Bucle while
contador = 0
while contador < 5:
    print(f"El contador es {contador}")
    contador += 1  # Incrementa el contador en 1
#Bucle for
for i in range(contador):
    print("Hola mundo")
option = 0

#simulacion del switch ==>> pasa a ser match
match(option):
            case 1: 
                os.system("cls")
                game()
            case 2:
                sys.exit()
            case 3: 
                os.system("cls")
                instructions()
            case other:
                print("Opcion Invalida")
                os.system("pause")

def clasificar_fruta(fruta):
    match fruta:
        case "manzana" | "pera" | "ciruela":
            return "Fruta de hueso"
        case "fresa" | "frambuesa":
            return "Fruta del bosque"
        case "naranja" | "limón":
            return "Fruta cítrica"
        case _:
            return "Fruta desconocida"

# Ejemplo de uso
print(clasificar_fruta("manzana"))  # Imprime: Fruta de hueso
print(clasificar_fruta("fresa"))     # Imprime: Fruta del bosque
print(clasificar_fruta("naranja"))   # Imprime: Fruta cítrica
print(clasificar_fruta("kiwi"))      # Imprime: Fruta desconocida
