#Ejercicio1
# Wilmer Nina Parisaca
x = int(input("Ingrese el tiempo en segundos: "))

print("Ingrese el tiempo de la tarea")
s = int(input("segundos: "))
m = int(input("minutos: "))
h = int(input("horas : "))
z = (h * 3600) + (m * 60) + s
y = x / z
if y >= 1 :
    print("Se puede realizar tarea")
else :
    print("La tarea no se puede realizar")
