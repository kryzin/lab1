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
    
