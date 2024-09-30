import random
import os
import sys

matrixA = []
matrixB=[]
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
        - x es el número de la columna (horizontal).
        - y es el número de la fila (vertical).
        - Ejemplo: Para abrir la casilla en la columna 2, fila 3, ingresarías: 2 3.

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
        - 2 3 0 -> Abre la casilla en la columna 2, fila 3.
        - 4 5 1 -> Marca la casilla en la columna 4, fila 5 como mina.
        - 4 5 0 -> Desmarca la casilla en la columna 4, fila 5 (la casilla ahora está libre y su contenido se mostrara).

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
        # ' '.join para unir todos los elementos de la fila con un espacio de por medio
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
    for i in range ((cols*rows)):
        malla.append(0)
    print(malla)

    for i in range(rows):
        matrixA.append([0]*cols)
        matrixB.append(["□"]*cols)

    createGame(rows,cols)

    print("Juego Creado con exito\n Buena Suerte ")
    os.system("pause")
    os.system("cls")

    op=0
    while op==0 :
        os.system("cls")
        printMatrix(matrixB,rows)
        while True:
            x = validNumber("Ingresa la Coordenada X: ", cols)
            y = validNumber("Ingresa la Coordenada Y: ", rows)
            flag = validFlag("1 - Bandera\n2 - Mostrar Casilla\n:  ")
            #https://realpython.com/python-string-formatting/
            print(f"x: {x}, y: {y}, flag: {flag}")

            # si es 0 no ha sido descubierta la casilla
            # si es 1 y la bandera es 2 es por que tenia una bandera y se va a descubrir
            if (malla[((x*y)-1)] == 0 or malla[((x*y)-1)] == 1):
                print(f"La coordenada es: x: {x}, y: {y}")
                break

            print(f"la coordenada {x} , {y} ya se ha mostrado elige otra")
            os.system("pause")
        
        if(flag==1):
            matrixB[y-1][x-1] = "X"
            malla[((x*y)-1)] = 1

        if (matrixA[y-1][x-1] != "*" and flag==2):
            matrixB[y-1][x-1] = matrixA[y-1][x-1]
            malla[((x*y)-1)] = -1
        if (matrixA[y-1][x-1] == "*" and flag==2):
            matrixB[y-1][x-1] = matrixA[y-1][x-1]
            malla[((x*y)-1)] = -1
            
            os.system("cls")
            print(f"GAME OVERRRRR")
            print(f"en la coordenada {x} , {y} se encuentra una Bomba")

            printMatrix(matrixA,rows)
            os.system("pause")



        

    
    #printMatrix(matrixA,rows)
    


def createGame(rows,cols):
    cells = rows * cols
    totalMines = int(cells / 4)

    # Colocar minas aleatoriamente
    minas_colocadas = 0
    while minas_colocadas < totalMines:
        fila = random.randint(0, rows-1)
        columna = random.randint(0, cols-1)
        
        # Colocar mina si la celda está vacía
        if matrixA[fila][columna] != "*":
            matrixA[fila][columna] = "*"
            minas_colocadas += 1
            
            # Actualizar los numeros de las celdas adyacentes
            for i in range(fila - 1, fila + 2):
                for j in range(columna - 1, columna + 2):
                    if 0 <= i < rows and 0 <= j < cols and matrixA[i][j] != "*":
                        matrixA[i][j] += 1


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