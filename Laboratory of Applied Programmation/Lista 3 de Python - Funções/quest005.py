def somaimposto (taxaimposto, custo):
    return ((taxaimposto*custo) + custo)
taxaimposto = float(input("Qual é a taxa de imposto? "))
custo = int(input("Qual é o custo? "))
print (f"O novo valor é {somaimposto(taxaimposto, custo)}")
input()