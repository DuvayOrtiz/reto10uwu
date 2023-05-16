# :star: Reto10uwu :star2:
## :star: Haciendo el reto 10 :sparkles:
![image](https://github.com/DuvayOrtiz/reto10uwu/assets/124726079/9776a211-9b59-4267-be4e-13d330bef310)
![image](https://github.com/DuvayOrtiz/reto10uwu/assets/124726079/6a0c7207-88f8-406d-b220-41dfbe4ecb42)
## :star: Sigo esperando que cree el canal :D :dizzy:
### :star: Ejercicios :zap:
Diferencia entre sort y sorted
sort es un método que se utiliza para ordenar una lista en su lugar, es decir, modifica la lista original. No devuelve ningún valor, simplemente ordena la lista actual (modifica el arreglo ya puesto)

sorted es una función que toma una secuencia iterable y devuelve una nueva lista ordenada con los elementos de la secuencia. (Hace un arreglo nuevo)
## :star: Punto 1 :boom:
- Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```ruby
#1
A=[] # Se crea un arreglo
A=input("Ingrese los elementos separados por comas: ").split(",") # Pido los elementos del arreglo
s=0 # Se hace un contador 
for i in range(len(A)): # Recorro el arreglo
    s+= float(A[i]) # Sumo los elementos
a=s/(len(A)) # saco el promedio
print("promedio es ", a ) # Imprimo el resultado
```
## :star: Punto 2 :collision:
- Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
```ruby
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
```
## :star: Punto 3 :sunny:
- Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```ruby
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
```
## :star: Punto 4 :high_brightness:
- Revisar que son los algoritmos de sorting, entender bubble-sort 
1. Comenzando desde el primer elemento, se compara cada par adyacente de elementos en el arreglo.
2. Si el par de elementos está en el orden incorrecto (el elemento de la derecha es menor que el de la izquierda), se intercambian.
3. Se repite el paso anterior para cada par de elementos adyacentes a lo largo del arreglo, desde el principio hasta el final.
4. Una vez que se completa un recorrido completo del arreglo, el elemento más grande se coloca en la posición final.
5. Se repiten los pasos 1 al 4 para el resto del arreglo, excluyendo el último elemento en cada iteración, ya que ya está en su posición correcta.

