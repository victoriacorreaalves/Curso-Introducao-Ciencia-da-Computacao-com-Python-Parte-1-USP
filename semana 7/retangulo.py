# imprime o retângulo de base b e altura h com caracteres no meio

b= int(input("digite a largura: "))
h= int(input("digite a altura: "))

while(h>0):
    aux = b
    while(aux>0):
        print("#",end="")
        aux=aux-1
    print()
    h=h-1
