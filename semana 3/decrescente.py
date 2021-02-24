# verifica se uma sequencia está em ordem decrescente
# ele para de a sequência não está em ordem decrescente ou o usuário digitou 0
decrescente = True
anterior= int(input("Digite o primeiro número da sequência: "))
print("Para parar digite 0")

valor = 1
while valor !=0 and decrescente:
	valor= int(input("Digite o próximo número da sequência: "))
	if valor > anterior:
		decrescente = False
	anterior = valor

if decrescente:
	print("A sequência está em ordem decrescente! :)")
else:
	print("A sequência não está em ordem decrescente! :(")