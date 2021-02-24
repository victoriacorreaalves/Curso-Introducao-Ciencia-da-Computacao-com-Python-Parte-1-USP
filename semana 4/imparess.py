# recebe um número n e retorna os n primeiros números ímpares
n= int(input("Digite o valor de n:"))
aux=1
while not (n==0):
	print(aux)
	aux=aux+2
	n=n-1