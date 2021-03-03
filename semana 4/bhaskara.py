# pede os coeficientes a,b e c de uma função de 2º grau
# imprime as raízes
import math
a= float(input("Digite a:"))
b= float(input("Digite b:"))
c= float(input("Digite c:"))

delta = b**2 - 4*a*c

if delta ==0:
    raiz1= (-b+ math.sqrt(delta))/ (2*a)
    print ("A única raíz é", raiz1)
else:
    if delta<0:
        print("Essa equação não possui raízes em R")
    else:
        raiz1= (-b+ math.sqrt(delta))/ (2*a)
        raiz2= (-b- math.sqrt(delta))/ (2*a)
        print ("As raízes são", raiz1, raiz2)
