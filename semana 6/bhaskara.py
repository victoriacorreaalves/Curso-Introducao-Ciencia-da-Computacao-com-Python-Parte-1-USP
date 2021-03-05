# pede os coeficientes a,b e c de uma função de 2º grau
# imprime as raízes
import math

def delta (a,b,c):
    return b**2 - 4*a*c

def main ():
    a= float(input("Digite a:"))
    b= float(input("Digite b:"))
    c= float(input("Digite c:"))
    imprime_raizes(a,b,c)


def imprime_raizes(a,b,c):
    d= delta(a,b,c)
    if d ==0:
        raiz1= (-b+ math.sqrt(delta))/ (2*a)
        print ("A única raíz é", raiz1)
    else:
        if d<0:
            print("Não possui raízes em R")
        else:
            raiz1= (-b+ math.sqrt(d))/ (2*a)
            raiz2= (-b- math.sqrt(d))/ (2*a)
            print ("As raízes são", raiz1, raiz2)
