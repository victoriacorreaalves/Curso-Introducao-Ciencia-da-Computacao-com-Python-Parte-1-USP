# testa se um número inteiro n é primo
n= int(input("Digite um número para testar se é primo: "))
teste= False
aux1= n
aux2 = n-1

while (aux1>1):
    while(aux2>1):
        if(aux1%aux2==0):
            teste= True
        aux2= aux2 -1
    aux1=aux1-1


if (teste== False):
    print("É primo!")
else:
    print("Não é primo!")
