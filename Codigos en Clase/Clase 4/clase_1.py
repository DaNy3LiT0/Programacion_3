
#---------------1---------------------------------
#SUma de listas
#En a estará laposicion de memoria de la lista1 y b la posiciópn de memoria de la lista2 
def sumar (a,b):
    suma=[]
    for i in range(len(a)):
        suma.append(a[i] + b[i])
    print(suma)




lista1 = [2,6,8,1.0]
lista2 = [1,8,2,2,1]

sumar(lista1,lista2)


#---------------1---------------------------------

#---------------2---------------------------------
def sumar (a,b):
    suma=[]
    for i in range(len(a)):
        suma.append(a[i] + b[i])
    print(suma)
    a.sort()
    print(f"Lista ordenada a : {a}")




lista1 = [2,6,8,1,0,4]
lista2 = [1,8,2,2,1,2]

sumar(lista1,lista2)

#---------------2---------------------------------



#---------------3---------------------------------
#Si ahora imprimo la lista1  y a, son las misma cosa. Lo que se pasa por como parametro es el ID (direccion de memoria como parámetro) 






#Vamos a comprobar con id si a y lista1 son lo mismo

def sumar (a,b):
    suma=[]
    for i in range(len(a)):
        suma.append(a[i] + b[i])
    print("La lista suma es :",suma)
    a.sort()
    print("la lista a ordenada es;",a)
    print("id de a es:", id(a))



#Si ahora imprimo la lista1 a y la lista1 son las misma cosa. Lo que se pasa por como parametro es el ID (direccion de memoria como parámetro) 
lista1 = [2,6,8,1,0,4]
lista2 = [1,8,2,2,1,2]

sumar(lista1,lista2)
print("La lista 1 es:",lista1)

print("id de lista1 es:", id(lista1))

#---------------4---------------------------------
#Regresamos a clase4