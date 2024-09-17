import math

a = float (input("Informe o A: "))

b = float(input("Informe o B: "))

c = float (input("Informe o C: "))

delta = (b*b) - (4 * a *c)

x1 = (-(b) + math.sqrt(delta)) / (2 * a)
x1 = (-(b) + math.sqrt(delta)) / (2 * a)

x2 = (-(b) - math.sqrt(delta)) / (2 * a)

print("O x1 é: ",x1)
print("O x2 é: ",x2)
