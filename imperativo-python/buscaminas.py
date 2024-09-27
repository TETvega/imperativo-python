import random

matrixA = []
matrixB=[]
# posibles   ʘ ʘ  ■ ʘ ■ □   
rows = int(input("Ingrese el numero de Filas: "))
cols = int(input("Ingrese el numero de Columnas: "))

for i in range(rows):
    matrixA.append([0]*cols)
    matrixB.append(["□"]*cols)

def printMatrix(matrix):
    for i in range(rows):
        #str(cell) para hacer cada celda en string
        # :>n   para alinear n caracteres a la derecha
        # ' '.join para unir todos los elementos de la fila con un espacio de por medio
        # lo dentro del join se conoce como expresion generadora
        formatted_row = ' '.join(f'{str(cell) :>3}' for cell in matrix[i])
        print(formatted_row)

def createGame():
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
createGame()
printMatrix(matrixA)
printMatrix(matrixB)
