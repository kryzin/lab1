#zad1
a = 'jest luty'
aa = 'nie mam psa'
b = 2
bb = 19
c = 12.5
cc = 9.99
print('zmienna string',a,aa)
print('zmienna int',b,bb)
print('zmienna float',c,cc)

#zad2
i = 1
j = 3
k = 8
dodawanie = j+k
odejmowanie = k-i
potega = k ** j
dzielenie = j/i
dzielenie_calkowite = k // j
mnozenie = j*k
print('3+8=%d' %(dodawanie))
print('8-1=%d' %(odejmowanie))
print('8 do potegi 3=%d' %(potega))
print('3/1=%d' %(dzielenie))
print('calkowite 8/3=%d' %(dzielenie_calkowite))

#zad3
b += 10 #b zwiekszana o 10
j -= 1 #j zmiejszana o 1
k *= 2 #k zwiekszana 2 razy
b /= j #b dzielona na j
j **= b #j do potegi b
k %= j #reszta z dzielenia k na j
print(b)
print(j)
print(k)

#zad4
from math import *
zmienna = e
liczba1 = pow(zmienna,10)
print('e^10=',liczba1)

liczba2 = pow(log(5+pow(sin(8),2)),1/6)
print('pow(log(5+pow(sin(8),2)),1/6)=',liczba2)

x = 3.55
liczba3 = floor(x)
print('⌊3,55⌋=',liczba3)

y = 4.80
liczba4 = ceil(x)
print('⌈4,80⌉=',liczba4)

#zad5
imie = 'KAROLINA'
nazwisko = 'RYZINSKA'
print(imie.capitalize(),nazwisko.capitalize())

#zad6
piosenka = 'thats what makes you beautiful na na na na nanana'
ile = piosenka.count('na')
print('w tekscie "na" pojawia sie',ile,'razy')

#zad7
slowo = 'september'
print('drugi znak slowa to',slowo[2])
print('ostatni znak slowa to',slowo[-1])

#zad8
podzial = piosenka.split()
print(podzial)

#zad9
A = 'december'
B = 15.4
C = hex(2238)
print(A,B,C)
print(type(A))
print(type(B))
print(type(C))


