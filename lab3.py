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

#Zad3
produkty = {"paczka mąki": "sztuka", "pomidory": "kg", "ziemniaki": "kg", "szampon": "sztuka"}
lista_prod = [key for key, value in produkty.items() if value.count("sztuka")]
print(lista_prod)

#Zad4
def czy_prostokatny(a, b, c):
    if((a ** 2 + b ** 2) == (c ** 2)) or ((b ** 2 + c ** 2) == (a ** 2)) or ((c ** 2 + a ** 2) == (b ** 2)):
        print('jest prostokatny')
    else:
        print('nie jest prostokatny')

print(czy_prostokatny(5,3,4))

#Zad5
def pole_trapezu(a=20, b=26, h=12):
    return ((a + b) * h)/2

print(pole_trapezu())

#Zad6
def ciag(a=1, b=4, ile=10):
    iloczyn = a
    for i in range(ile):
        iloczyn *= b ** i
    return iloczyn

print(ciag())

#Zad7
def ciag2(* ile, a=1, b=4):
    wynik = a
    if len(ile) == 0:
        return 0
    else:
        for i in ile:
            wynik *= (b ** i)
         return wynik

print(ciag2())
#Zad8

def zakupy(** produkty):
    return len(produkty),sum(produkty.values())

print(zakupy(zeszyt = 3.99, długopis = 2.99, ołówek = 1.99))
