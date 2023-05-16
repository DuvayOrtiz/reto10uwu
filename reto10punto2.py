#2
def pp(A1, A2): 
    if len(A1) != len(A2):
        return "no miden lo mismo" # Si no miden lo mismo no se comparam
    s = 0 # Se hace un contador 
    for i in range(len(A1)): # Recorro el arreglo
        s += float(A2[i]) * float(A1[i]) # se usa el contador
    return "el producto punto es" + str(s)
A1=[] # Se crea un arreglo
A2=[] # Se crea un arreglo
A1=input("Ingrese los elementos separados por comas: ").split(",") # Pido los elementos del arreglo
A2=input("Ingrese los elementos separados por comas: ").split(",") # Pido los elementos del arreglo
print(pp(A1,A2)) # Imprimo el resultado