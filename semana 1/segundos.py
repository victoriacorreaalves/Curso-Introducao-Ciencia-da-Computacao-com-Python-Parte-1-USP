# recebe o número de segundos e retorna a quantidade de dias,meses,horas e segundos
s=input ("Por favor, entre com o número de segundos que deseja converter:")
seg= int(s)
dias= seg // 86400
h= seg % 86400
horas= h // 3600
srestante= seg % 3600
min= srestante // 60
sfinal= srestante % 60

print (dias, "dias,", horas,"horas,", min,"minutos e", sfinal, "segundos.")