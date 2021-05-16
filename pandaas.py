import pandas as pd
import numpy as np
import xlrd
import openpyxl

#1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
#print(df)


#2
#print("ilosc imion > 1000:")
#print(df[df['Liczba']>1000])

#print("imię == Karolina:")
#print(df[df['Imie']=='KAROLINA'])

#print("sumy dzieci rocznikami:")
#print(df.groupby(['Rok']).agg({'Liczba':['sum']}))

#print("suma M i suma K:")
#print(df.groupby(['Plec']).agg({'Liczba':['sum']}))

print("najpopularniejsza imie M i imie K rocznikowo: ")
#grupa = df.groupby(['Rok']) #?? co dalej


print("najpopularniejsze imie M i K overall: ")
grupaPlec = df.groupby(['Plec'])
print(grupaPlec.get_group('M').head(1))
print(grupaPlec.get_group('K').head(1))