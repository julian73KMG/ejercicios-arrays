##Autor Julian Mendez, Problemas de Arreglos
#-- Problema 4 --

#Algoritmo que determine la mediana de un arreglo de enteros.
#La mediana es el numero que queda en la mitad del arreglo despues de ordenado

def mediana_array(a):
    if len(a) == 0:
         return "\nArreglo vacio"
    else:
        a.sort()    #Ordenar el arreglo
        max = len(a)-1  #Variable con la posición del máximo
        mediana = int(max/2)    #Definir la posición de la mediana

    #Determinar si la cantidad de elementos es par o impar
        if len(a)%2 == 0:

        #Si es par, la mediana son los dos elementos en medio
            s = [a[mediana] , a[mediana+1]]
        else:

        #Si es impar es igual a la mediana
            s = [a[mediana]]
    return s

print(mediana_array([3,1,4,6,2]))
#[1,2,3,4,5,6]


#-- Problema 5 --
#Algoritmo que mueva los ceros al final del arreglo

def cero_der(a):
    if len(a) == 0:
         return "\nArreglo vacio"
    else:
    #Recorrer el arreglo
        for i in range(0,len(a)):
                a.remove(0) #quitar el 0
                a.append(0) #Agregarlo al final
    return a

print(cero_der([0,11,36,-23,81,0,0,12,11,0,-1]))
