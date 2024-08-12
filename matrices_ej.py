##Autor Julian Mendez, Problemas de Matrices

#-- Problema 1 --
#Algoritmo que permita sumar dos matrices de reales

def suma_matrices(A,B):
    if len(A) == 0 or len(B) ==0:
        raise Exception("Hay una matriz nula")  #Excepcion de matriz nula
    else:
        filaA = len(A)
        filaB = len(B)
        columnaA = len(A[0])
        columnaB = len(B[0])
        S = [[0]* columnaA for _ in range(filaA)]
        if filaA == filaB and columnaA == columnaB:
            for i in range(filaA):  #Recorre las filas
                for j in range(columnaA):   #Recorre la columna
                    S[i][j] = A[i][j] + B[i][j]     #Asigna el valor de cada indice en S
        else: 
            raise Exception("Diferente numero de filas o columnas") #Expcepcion de filas o columnas
    return S

#--  Problema 2 --
#Algoritmo que permita multiplicar dos matrices de numeros reales
def multipicar_matrices(A,B):
    if len(A) == 0 or len(B) == 0:
        raise Exception("Hay una matriz nula")  #Excepcion de matriz nula
    elif len(A[0])!= len(B):
        raise Exception("El numero de columnas de A debe coincidir con las filas de B") #Expcepcion del tipo matriz n*m != m*k
    else:
        filaA = len(A)
        filaB = len(B)
        columnaA = len(A[0])
        columnaB = len(B[0])
        M = [[0]* columnaA for _ in range(filaA)]
        
        for i in range(filaA): #Recorre las filas
            for j in range(columnaB):   #Recorre las columnas
                s = 0   #Variable para guardar la suma, reinicia con cada suma hecha
                for k in range(filaB):  #Recorre la fila donde hacemos las sumas
                    s += A[i][k] * B[k][j]  #Guarda el resultado de la multiplicacion y lo suma al valor previo
                M[i][j] = s
    return M

#--  Problema 3  --
#Desarrollar un programa que sume los elementos de una columna dada de una matriz.

def sumaColumna(A,C):
    fila = len(A)
    if len(A) == 0:
        raise Exception("Matriz nula.") #Excepcion de Matriz nula
    if C <= 0:
            raise Exception("El rango empieza en 1")    #Excepcion de rango, se empieza en 1 para menor dificultad
    if C > len(A):
            raise Exception("Fuera del rango")  #Excepcion de rango, fuera del rango de las columnas de la matriz
    else:
        C -= 1  #Deja el rango de acuerdo al recorrido que hace python
        s = 0
        for i in range(fila): #Recorre la Columna
            s += A[i][C]    #Suma el valor del indice
    return s

MatrizA=[[1,2],
         [3,4]]

MatrizB=[[5,6],
         [7,8]]

MatrizNula = []

print(multipicar_matrices(MatrizA,MatrizB))

