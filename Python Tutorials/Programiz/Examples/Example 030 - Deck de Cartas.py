import itertools, random
def cartas ():
    deck = list(itertools.product(range(1, 14), ['Espadas', 'Copas', 'Paus', 'Ouro']))
    random.shuffle(deck)
    for i in range (5):
        print (f"{deck[i][0]} de {deck[i][1]}")
while (True):
    sorte = input("Você quer sortear um deck [S ou N]? ").lower()
    if sorte == 's':
        print ("Você consegiu: ")
        cartas()
    else:
        break