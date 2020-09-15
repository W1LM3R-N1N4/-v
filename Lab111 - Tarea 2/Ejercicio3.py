#Ejercicio3
# Wilmer Nina Parisaca
h = int(input("ingrese las horas :"))
m = int(input("ingrese los minutos :"))
s = int(input("ingrese los segundos :"))
#sumar +1segundo
s = s + 1
if (s==60):
   s=0
   m=m+1
   if(m==60):
      m=0
      h=+1
      if(h==24):
         h=0
if (h<10 and m<10 and s<10):
   print(0, h,":", 0, m, ":", 0, s)