#desafio de fazer o calculo da média de um amigo

nota1 = float(input("1º nota:"))
nota2 = float(input("2º nota:"))
nota3 = float(input("3º nota:"))
nota4 = float(input("4º nota:"))

media = (nota1 + nota2 + nota3 + nota4)/4

if media < 5:
    print("Sua média é de: {} e você está reprovado" .format(media))
else:
    print("Sua média é de: {} e você está aprovado" .format(media))


