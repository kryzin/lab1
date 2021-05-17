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
#print(df.agg({'Liczba':['sum']}))

#print("suma M i suma K:")
#print(df.groupby(['Plec']).agg({'Liczba':['sum']}))

#print("najpopularniejsza imie M i imie K rocznikowo: ")
#print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'].nth[0])

#print("najpopularniejsze imie M i K overall: ")
