vogal = 'aeiou'
string = 'oi, sou muito foda'
string = string.casefold()
contador = {}.fromkeys(vogal, 0)
for char in string:
    if char in contador:
        contador[char] += 1
print (contador) 
input()