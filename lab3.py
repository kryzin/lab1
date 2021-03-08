#Zad1
A = [1-x for x in range(1,11)]
print(A)
B = [4**x for x in range(8)]
print(B)
C = [x for x in B if x%2 == 0]
print(C)

#Zad2
import random
lista1 = []
lista2 = []
for x in range(1,11,1):
    a = random.randint(-100,100)
    lista1.append(a)
    if (a%2 == 0):
        lista2.append(a)

print(lista1)
print(lista2)
