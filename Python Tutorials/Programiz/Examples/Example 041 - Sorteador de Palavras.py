palavra = input("Digite uma palvra: ")
words = [word.lower()for word in palavra.split()]#se fosse palavra.split() funcionaria tbm
words.sort()
print ("As palavras sorteados foram: ")
for i in words:
    print(i)
input()