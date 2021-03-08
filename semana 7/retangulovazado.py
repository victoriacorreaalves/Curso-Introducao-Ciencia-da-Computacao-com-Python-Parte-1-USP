# imprime o retângulo de base b e altura h sem caracteres no meio

b = int(input("Digite a largura: "))
h = int(input("Digite a altura: "))

aux=h
aux2=b
while(aux>0):
    if (aux==h) or (aux==1):
        while(aux2>0):
            print("#",end="")
            aux2=aux2-1
        print()
        aux2=b
    else:
        print("#",end="")
        while(aux2>2):
            print(" ",end="")
            aux2=aux2-1
        print("#")
        aux2=b
    aux=aux-1
        
