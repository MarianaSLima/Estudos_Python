#um programa que recebe em centimetros e passa para polegadas 1-(2.54) 2-pes(30.48) 3-jardas(91.44)
#e mostre o tipo de conversão e o valor convertido

tipo = int(input("Iforme o tipo de conversão\n 1-polegadas | 2-pes | 3-jardas:"))
cm = int(input("Iforme um número a ser convertido:"))

if tipo == 1:
    conv = cm * 2.54
    print("A opção escolhida foi polegadas: " + "{} centímetros são {} polegadas" .format(cm, conv))
elif tipo == 2:
    conv = cm * 30.48
    print("A opção escolhida foi pes: " + "{} centímetros são {} pes" .format(cm, conv))
elif tipo ==3:
    conv = cm * 91.44
    print("A opção escolhida foi jardas: " + "{} centímetros são {} jardas" .format(cm, conv))
else:
    print("Você não escolheu uma opção válida!")