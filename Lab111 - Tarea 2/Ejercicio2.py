#Ejercicio2
# Wilmer Nina Parisaca
#D = b2 - 4ac

a = int(input("Ingrese la variable a :"))
b = int(input("Ingrese la variable b :"))
c = int(input("Ingrese la variable c :"))

D = b * b - 4 * a * c
if(D > 0):
    print("Como D > 0 las raíces serán reales y diferentes :", D)
if(D < 0):
    print("Como D < 0, las raíces serán complejas :", D)
if(D == 0):
    print("Como D = 0, las raíces serán reales e iguales :", D)
