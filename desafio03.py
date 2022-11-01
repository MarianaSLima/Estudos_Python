#faça um programa que leia 3 numeros e fale o maior e o menor deles

num1 = int(input("Informe o primeiro número:"))
num2 = int(input("Informe o segundo número:"))
num3 = int(input("Informe o terceiro número:"))

print("O maior número é:")
if(num1 > num2 and num1 > num3):
    print(num1)
elif(num2 > num1 and num2 > num3):
    print(num2)
else:
    print(num3)

print("O menor número é:")
if(num1 < num2 and num1 < num3):
    print(num1)
elif(num2 < num1 and num2 < num3):
    print(num2)
else:
    print(num3)


#maior = 0
#menor = 99999
#
#if num1 < menor:
#    menor = num1
#if num2 < menor:
#    menor = num2
#if num3 < menor:
#    menor = num3
#
#if num1 > maior:
#    maior = num1
#if num2 > maior:
#    maior = num2
#if num3 > maior:
#    maior = num3
#
#print("O maior número é: {} e o menor número é: {}" .format(maior, menor))