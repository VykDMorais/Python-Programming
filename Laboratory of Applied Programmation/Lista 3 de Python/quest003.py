argumento = []
def somador (argumento):
    soma = sum(argumento)
    return soma
for i in range (3):
    argumento.append(int(input("Digite um número inteiro: ")))
print (f"A soma desses três termos é: {somador(argumento)}")
input()