def bhaskara (a, b, c):
    discriminante = (b**2) - (4*a*c)
    x1 = ((-b) + (discriminante**0.5))/(2*a)
    x2 = ((-b) - (discriminante**0.5))/(2*a)
    print (f"X1 = {x1}\nX2 = {x2}")
while (True):
    a = float(input("Informe a: "))
    if a != 0:
        break
b = float(input("Informe b: "))
c = float(input("Informe c: "))
bhaskara (a, b, c)
input()