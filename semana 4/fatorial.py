# recebe um número n e retorna o valor de n!
n= int(input("Digite o valor de n:"))

fatorial = 1

while not (n==1):
	if (n==0):
		fatorial=1
		n=1
	else:
		fatorial= fatorial * n
		n= n-1

print (fatorial)