import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
df = df.groupby(['Rok']).agg({'Liczba':['sum']})
x = df['Rok'] # co jest nie tak z 'Rok'???????
y = df['Liczba']
fig, wykres = plt.subplots(figsize=(10,4))
wykres.plot(x, y)

