#Calcular peso ideal
print("1-Mulher")
print("2-Homem")
sexo = int(input("Sexo:"))
altura = float(input("Altura:"))

if sexo == 1:
    peso = (62.1 * altura) - 44.7
else:
    peso = (72.7 * altura) - 58

print("Seu peso ideal é de: {}" .format(peso))