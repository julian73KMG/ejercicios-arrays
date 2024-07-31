##Autor Julian Mendez
#codigo principal de ejecución
import ejercicios

def main():

    #Arreglos principales de prueba
    s = [1,5]
    t = [1,"prueba",2]
    u = [1,2,3]
    v = [4,5,6]
    w = [1/2,7/5,3/2]

    
    print(ejercicios.promedio_arreglo_r(w))
    print(ejercicios.producto_punto_r(u,v))
    print(ejercicios.producto_directo_r(w,v))

    return 0

if __name__=='__main__':
    main()