#fazendo contas e criando variáveis

num1 = input("Qual o primeiro número?")
num2 = input("Qual o segundo número?")

soma = num1 + num2
#nesse caso por ter juntado automaticamente o resultado vai dar 55, pois quando a soma foi feita os dois números eram STRINGS e não INTEIROS
print("A soma entre {} e {} é igual {}" .format(num1, num2, soma))

print(type(num1))
print(type(num2))

soma = int(num1) + int(num2)

#Nesse outro exemplo a soma ocorreu corretamente, pois os números foram transformados em inteiros antes de serem somados.
print("A soma correta é: {}" .format(soma))

#format = formata as variáveis para string
#int = passa as variáveis para int.
#print = é tipo o 'alert' do javascript, exibe o que estiver dentro do parêntese no terminal