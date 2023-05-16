#1
A=[] # Se crea un arreglo
A=input("Ingrese los elementos separados por comas: ").split(",") # Pido los elementos del arreglo
s=0 # Se hace un contador 
for i in range(len(A)): # Recorro el arreglo
    s+= float(A[i]) # Sumo los elementos
a=s/(len(A)) # saco el promedio
print("promedio es ", a ) # Imprimo el resultado