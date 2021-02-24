# pede um número para o usuário e retorna o número da dezena desse número
n= input("Digite um número inteiro:") 
num= int(n)

d= (num // 10) % 10
print ("O dígito das dezenas é", d)