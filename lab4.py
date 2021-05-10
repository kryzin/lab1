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

