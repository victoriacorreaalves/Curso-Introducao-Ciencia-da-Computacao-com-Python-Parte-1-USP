# recebe um número e retorna FizzBuzz se for divisivel por 5 e 3
# caso não seja divisível por 5 e 3, retorna o próprio número
n= int(input("Digite um número inteiro:"))

if n%5==0 and n%3==0:
 print("FizzBuzz")
else:
 print(n)