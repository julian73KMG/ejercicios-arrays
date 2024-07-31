#i = int(input("\n¿Cuantos elementos tendrá el arreglo?\n-> "))
#array=[]
#
#for i in range(0,i):
#    valor = float(input("Ingrese un valor real:\n-> "))
#    array.append(valor)
#
#print(array)

def pos_maximo(A):
        m = 0
        for i in range(0,len(A)):
            if A[i] > A[m]:
                m = i
        return m

s=0
p=0

for i in range(0,3):
        p = i*i
        print("p es: ", p)
        s += p 
        print("s es: ", s)

def lee_arreglo_reales():
    return [float(x) for x in input("Arreglo:").split(",")]

print(lee_arreglo_reales())