a = float(input("Digite a 1ª nota: "))
b = float(input("Digite a 2ª nota: "))
media = (a+b)/2
if media == 10:
    print("Aprovado com distinção")
elif media >= 7 and media < 10:
    print("Aprovado")
elif media >= 0 and media < 7:
    print("Reprovado")
else:
    print("Nota inválida")