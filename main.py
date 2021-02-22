from math import *

a, b, c = 2, 4, 6
print(a)
print(b)
print(c)

dzielenie = b/c
dzielenie_calkowite = b // c
print(dzielenie_calkowite)

dodawanie = a+b
potega = b ** a
print(dodawanie)
print(potega)

potega = pow(b,a)
print(potega)

a += 10
print(a)
imie = 'Karol'
wiek = 99
print('mam na imie %s i mam %d lat' %(imie,wiek))

z= 6 - 4
print('wynik dzialania %(z1)d-%(z2)d=%(z3)d' % {'z1':c, 'z2':b, 'z3':z})
