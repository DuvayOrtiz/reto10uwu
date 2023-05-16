#3
def excluir(A1):
    C=[] # Se crea un arreglo
    D=[] # Se crea un arreglo
    E=[] # Se crea un arreglo
    for i in range(len(A1)): # Recorro el arreglo
        A1[i] = int(A1[i]) # Lo vuelvo entero
        if A1[i] != 0: # Si es distinto a cero se meten en un arreglo
            C.append(A1[i]) 
        else:
            D.append(A1[i]) # Si es cero se meten en otro arreglo
    E = C+D # Los meto en otro arreglo
    return E

A1 = input("Ingrese los elementos separados por comas: ").split(",") # Pido los elementos del arreglo
print(excluir(A1)) # Imprimo el resultado