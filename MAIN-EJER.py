#Bitácora de prácticas
#Edoardo Martín Ricalde Ché

#=============================
#Optimización Local
#=============================
#Ejercicio 1
#Original
Edo = 3
Victor = 5
Sobra = 2
total = a + b
diferencia = a - b
print(total) 
#Optimizado
#Las variables y operaciones que no se necesitan o utilizan se eliminan
Edo = 3
Victor = 5
print(Edo + Victor)
#Ejercicio 2
#Original
x = 4
y = 1
z = 3
op1 = x-1
op2 = y * z
final = op1 + op2
print(final)
#Optimizado
#Asignación de una sola línea a las variables y simplificación de operaciones en la variable final
x,y,z = 4,1,3
final = (x-1) + (y * z)
print(final)

#EEjercicio 3
#Original
x = 1
y = 2
z = x + x 
z2 = x + x
a = y + y 
b = x + y 
print(b)
#Optimizado
#Eliminación de Redundancia
x,y = 1,2
b = x + y
print (b) 

#============================
#Optimización de ciclos
#============================
#Ejercicio 4 
#Original
for j in [0,1,2]:
    print("Hola")
#Optimizado
#Se crea una variable para almacenar el arreglo en vez de instanciarlo en el for
g = [0,1,2]
for j in g:
    print("Hola ", end='')
print("\n")

#Ejercicio 5
#Original
x2 = 0
y2 = "England"
while x2 < 5:
    x2 += 1
    print(y2)
print("\n")
#Optimizado
#No es necesario almacenar la información a imprimir en una variable, se cambia a que directamente se imprima ese texto en la función print
x1 = 0
while x1 < 5:
    x1 += 1
    print("England")

#Ejercicio 6
#Original
a1 = [1,2,3]
for b1 in a1:
    c1 = b1 + 1
    res = "Suma de 1 + " + str(b1) + " = " + str(c1)
    print(res)
#Optimizado
#Eliminación de concatenación y exceso de variables
a1 = [1,2,3]
for b1 in a1:
    print(f"Suma de 1 + {b1} = {b1+1}")

#*****************************
#Ejercicios de Mirilla
#*****************************

#Ejercicio 7
#Original
z1 = 0
while z1 < 4:
    z1 += 1
    if z1 == 3:
        print(z1)
    else:
        pass
#CODIGO OPTIMIZADO
#Terminamos de manera definida con un break evitando elementos inecesarios al quitar pass, interrumpiendo el flujo
z1 = 0
while z1 < 4:
    z1 += 1
    if z1 == 3:
        print(z1)
        break
#Ejercicio 8
#Original
for z in "itsva":
    v = "v"
    if z == v:
        pass
    else:
        print(z)
#Optimizado
#Eliminacion de variable para liberar espacio y el uso del break para terminar de manera definida, interrumpiendo el flujo

for z in "itsva":
    if z == "v":
        break
    print(z)

#Ejercicio 9
#Original
i = 0
j = "Linea 1"
while i < 3:
    i += 1
    print(j)
#Optimizado
#Eliminación de la variable innecesaria
i = 0
while i < 3:
    i += 1
    print("Hola")
    break

#==============================
#Ejercicios Globales
#==============================
#Ejercicio 10
#Original
contenido = "Después de todo este tiempo? Siempre...!"
file = "archivo.txt"
archivo = open(file, 'w')
archivo.write(contenido) 
archivo.close()

archivo2 = open(file, "r")
for linea in archivo2.readlines():
    print(linea)
archivo2.close() 
#Optimizado
#En vez de escribir el contenido en el archivo que queremos mostrar, se hace una búsqueda de posición para imprimir la primera línea del archivo, estando ahí el contenido que buscamos
archivo3 = open(file,"r")
archivo3.seek(0)
print(archivo3.read())
archivo3.close()  