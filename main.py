import numpy as np
# 1
a = np.arange(3, 48, 3)
print(a)

# 2
b = np.arange(0, 2, 0.2)
print(b)
c = b.astype('int64')
print(c)

# 3
def tablica(n):
    d = np.arange(1, n*n+1, 1)
    d = d.reshape((n, n))
    return d
print(tablica(4))

# 4
def potega(liczba, pot):
    e = np.logspace(1, pot, pot, endpoint=True, base=liczba)
    return e
print(potega(2, 4))

# 5
