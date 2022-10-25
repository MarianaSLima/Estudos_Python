#calcula a área de um retângulo

lado1 = input("Informe o valor do 1º lado:")
lado2 = input("Informe o valor do 2º lado:")

print("Lado númerico?", lado1.isnumeric())
print("Lado decimal?", lado2.isdecimal())


area = float(lado1) * float(lado2)


print("A área do retângulo é de: {}" .format(area))