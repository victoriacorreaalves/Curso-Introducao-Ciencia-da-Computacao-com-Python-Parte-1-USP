# recebe um número n e retorna a soma dos seus dígitos
n= int(input("Digite um número inteiro:"))

aux= 0 

while (n>0):
	resto= n%10
	n= (n-resto)/10
	aux= aux + resto

print (aux)