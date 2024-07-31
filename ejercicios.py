##Autor Julian Mendez
##Se presentarán tres funciones cuya finalidad es realizar operaciones de arreglos

#-- Problema 1 --
# Algoritmo que calcule el promedio de un arreglo de reales
def promedio_arreglo_r(ar):
    #Comprueba si el arreglo no es vacío
    if len(ar) == 0:
        return "\nEl arreglo está vacío."
    #Ejecuta el algoritmo
    else:
        s = 0   #Variable s de suma declarada e inicializada en 0
        
        #Ciclo que recorre el arreglo y suma cada índice
        for i in range(0,len(ar)):

            #Comprueba si hay un string
            if type(ar[i]) == str:
                 return "\nEntrada invalida, solo numeros"
            else:
                 s += ar[i]
        #Se calcula el promedio
        p = s / len(ar)
        return p
    
#-- Problema 2 --
# Algoritmo que calcule el producto punto de dos arreglos de reales

def producto_punto_r(v,w):
    #Comprueba si el arreglo no es vacío
    if len(v) == 0 or len(w) == 0:
        return "\nUn arreglo está vacío."
    #Comprueba si los arreglos tienen la misma cantidad de elementos
    elif len(v) == len(w):    s = 0
    #Recorre los arreglos, multiplica los indices y guarda su valor, suma con cada vuelta al valor previo
        for i in range(0,len(v)):

            if type(v[i]) == str or type(w[i]) == str:
                 return "\nEntrada invalida, solo numeros."
            else:
                s += v[i] * w[i]
        return s 
    #Termina si hay una diferencia en la cantidad de elementos
    else:
        return "\nCantidad de elementos desigual."  

#-- Problema 3 --
# Algoritmo que calcula el producto directo de dos arreglos de reales

def producto_directo_r(v,w):
    #Comprueba si el arreglo no es vacío
    if len(v) == 0 or len(w) == 0:
        return "\nUn arreglo está vacío."
    #Comprueba si los arreglos tienen la misma cantidad de elementos
    elif len(v) == len(w):    pd = []
    #Recorre los arreglos, multiplica los indices y guarda su valor, luego lo asigna a un array vacío
        for i in range(0,len(v)):
            p = v[i] * w[i]
            pd.append(p)
        return pd
    #Termina si hay una diferencia en la cantidad de elementos
    else:
        return "\nCantidad de elementos desigual." 
