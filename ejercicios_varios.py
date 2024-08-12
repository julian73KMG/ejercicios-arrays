# 1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
def max(a,b):
    if a > b:
        max = a
    elif b > a:
        max = b
    else:
        return " \nLos numeros son iguales."
    return max

#2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def max_tres(a,b,c):
    if a>b and a>c:
        max = a
    elif b>c and b>a:
        max = b
    elif c>a and c>b:
        max = c
    else:
        return "\nDos o mas numeros son iguales"
    return max

#3 - Definir una función que calcule la longitud de una lista o una cadena dada.
def longitud(a):
    l = 0
    for _ in a:
        l+=1
    return l

#4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
def esVocal(v):
    if v=='a' or v=='A':
        r = True
    elif v=='e' or v=='E':
        r = True
    elif v=='i' or v=='I':
        r = True
    elif v=='o' or v=='O':
        r = True
    elif v=='u' or v=='U':
        r = True
    else:
        r = False
    return r

#5 - Escribir una función sum() que sume todos los números de una lista.
def sum(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s

#5 - Escribir función multip() que multiplique todos los números de una lista.
def mult(a):
    s = 1
    for i in range(len(a)):
        s *= a[i]
    return s

#6 - Definir una función inversa() que calcule la inversión de una cadena.
def inverso(a):
    inv=()
    for _ in a:
        inv = a[::-1]
    return inv

#7 - Definir una función es_palindromo() que reconoce palíndromos
def palindromo(a):
    if a[::-1] == a:
        p = True
    else:
        p = False

    return p

#8 -  Definir una función superposicion() que tome dos listas y devuelva True si tienen
#  al menos 1 miembro en común o devuelva False de lo contrario.

def superposicion(a,b):
    for i in range(len(a)):
        if a[i] in b:
            s = True
        else: s = False
    return s

#9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 

def generarCaracter(n,c):
    for _ in c:
        r = n*c
    return r

#10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.

def  histograma(a):
    for i in range(0,len(a)):
        h = a[i]*'*'
        print(h)
    return " "

print(histograma([4,9,7,6]))