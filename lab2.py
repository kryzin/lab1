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

