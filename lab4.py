#Zad1
liczby = [a for a in range(0,50) if a % 4 == 0]
plik = open('lab4_1.txt','w')
plik.writelines(str(liczby))
plik.close()

#Zad2
plik = open('lab4_1.txt','w')
wplik = plik.read()
print(wplik)
plik.close()

#Zad3
with open('lab4_1.txt','r+') as plik:
  plik.write("tekst do ploku")
  
with open('lab4_1.txt','r+') as plik:
  wplik = plik.read()
print(wplik)

#Zad4
class NaZakupy():
  def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
    self.nazwa_produktu = nazwa_produktu
    self.ilosc = ilosc
    self.jednostka_miary = jednostka_miary
    self.cena_jed = cena_jed
    
  def wyswietl_produkt(self):
    print("produkt to {}, w ilości {}{}, przy cenie {}zł za {}".format(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed, self.jednostka_miary))
    
  def ile_produktu(self):
    print("{} {}".format(self.ilosc, self.jednostka_miary))
    
  def ile_kosztuje(self):
    return self.ilosc * self.cena_jed
  
produkt = NaZakupy("banany", 10, "kg", 6.5)
produkt.wyswietl_produkt()
produkt.ile_produktu()
print(str(produkt.ile_kosztuje()) + "zl")
produkt2 = NaZakupy("zeszyt", 1, "sztuka", 2)
produkt2.wyswietl_produkt()

#Zad5
class ciag_arytmetyczny():
  def __init__(self):
    self.a1 = None
    self.r = None
    self.n = None
    self.ciag = []
    
  def wyswietl_dane(self):
    for element in self.ciag:
      print(element)
     
  def pobierz_elementy(self):
    while True:
      element = input("podaj liczbe / 'koniec': ")
      if element != 'koniec':
        self.ciag.append(float(element))
        else:
          break
  def pobierz_parametry(self):
    a = input(" pierwszy wyraz: ")
    self.a1 = int(a)
    r = input(" roznica: ")
    self.r = int(r)
    n = input(" dlugosc ciagu")
    self.n = int(n)
  
  def policz_sume(self):
    return sum(self.ciag)
  
  def policz_elementy(self):
    if (self.a1 is not None) & (self.r is not None) & (self.n is not None):
      indeks = 1
      self.ciag.append(self.a1)
      while indeks != self.n:
        self.a1 += self.r
        self.ciag.append(self.a1)
        indeks += 1
        
ciag = ciag_arytmetyczny()
ciag.pobierz_parametry()

#Zad6
class Robaczek():
     def __init__(self, x, y, krok):
         self.x = x
         self.y = y
         self.krok = krok
 
     def idz_w_gore(self, ile_krokow):
         self.y = self.y + (ile_krokow * self.krok)
         self.x = self.x
 
     def idz_w_dol(self, ile_krokow):
         self.y = self.y - (ile_krokow * self.krok)
         self.x = self.x
 
     def idz_w_lewo(self, ile_krokow):
         self.y = self.y
         self.x = self.x - (ile_krokow * self.krok)
 
     def idz_w_prawo(self, ile_krokow):
         self.y = self.y
         self.x = self.x + (ile_krokow * self.krok)
 
     def pokaz_gdzie_jestes(self):
         print("współrzędne robaczka to x={} y={}".format(self.x, self.y))
 
 robak = Robaczek(1,0,1)
 robak.pokaz_gdzie_jestes()
 robak.idz_w_gore(5)
 robak.pokaz_gdzie_jestes()
 robak.idz_w_lewo(3)
 robak.pokaz_gdzie_jestes()
 robak.idz_w_dol(2)
 robak.pokaz_gdzie_jestes()
 robak.idz_w_prawo(4)
 robak.pokaz_gdzie_jestes()

