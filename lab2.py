#Zad1
lista = ['Spirited Away','Sherlock Holmes','Gra tajemnic','Mamma Mia!','Wilcze Dzieci']
lista.reverse()
lista.append('Truman Show')
lista.append('Bao')
lista.append('Deadpool')
lista.append('Cast Away')
lista.append('Shrek 2')

#Zad2
#kluczem jest rok produkcji
slownik = {2012:'Wilcze Dzieci',2008:'Mamma Mia!',2014:'Gra tajemnic',2011:'Sherlock Holmes',2001:'Spirited Away'}
slownik[1998] = 'Truman Show'
slownik[2018] = 'Bao'
slownik[2016] = 'Deadpool'
slownik[2000] = 'Cast Away'
slownik[2004] = 'Shrek 2'
print(slownik[2008])

#Zad3
przedmioty = {'CAD':'CAD Komputerowe Wspomaganie Projektowania','ps':'Programowanie Strukturalne','emd':'elementy matematyki dyskretnej','wd':'wizualizacja danych'}
x = len(przedmioty)
print(x)

#Zad4
liczba = input("podaj liczbę: ")
liczba = int(liczba)
liczba **= liczba
print(liczba)

#Zad5
import sys as system
system.stdout.write("podaj dowolny ciąg znaków: ")
napis = system.stdin.readline()
ile = napis.count('a')
print('jest ',ile,' znaków "a" w napisie')

#Zad6
a = input('podaj a: ')
b = input('podaj b: ')
c = input('podaj c: ')
a = int(a)
b = int(b)
c = int(c)

if (a%2==0) & (b>c):
    print('warunek spełniony')
else:
    print('liczby nie spełniają warunków')
    
#Zad7
liczby = [3,5.55,89,3.14,12,12.79,15]
i = 0
for x in range(1,8):
    print(liczby[i] + liczby[i - 1])
    i += 1

#Zad8
zadanie = []
pom = 0
while pom != 10:
    wartosc = input("podaj liczbę: ")
    wartosc = float(wartosc)
    pom += 1
    if (wartosc%1 == 0):
        wartosc = int(wartosc)
        zadanie.append(wartosc)
print(zadanie)

#Zad9
litera = [1,2,3,4,5,6]

for x in litera:
    if (x == 1) or (x == 6):
        for x in litera:
            print('o', end = '')
        print('')
    else:
        for x in litera:
            if (x == 1):
                print('o', end = '')
            elif (x == 6):
                print('o')
            else:
                print(' ', end = '')
                
#Zad10
dane = input("podaj liczbę: ")
try:
   dane = int(dane)
except ValueError:
   print("znak nie jest liczbą")
