sitrn = 'aIBohPhobiA'
sitrn = sitrn.casefold()
reverso = reversed(sitrn)
if list(sitrn) == list(reverso):
    print("É palíndromo")
else:
    print("Não é palíndromo")
input()