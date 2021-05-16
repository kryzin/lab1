import numpy as np

#1
a = np.array([2, 4, 6])
b = np.array([3, 8, 9])
c = a * b
print(c)

#2
a2 = np.array([[1, 2, 3], [4, 6, 5], [9, 7, 8]])
b2 = np.array([[3, 0, 8, 9], [2, 6, 2, 0], [4, 5, 6, 9], [12, 0, 13, 4]])
print(a2)
print(b2)
print(a2.min(axis=0))
print(a2.min(axis=1))
print(b2.min(axis=0))
print(a2.min(axis=1))

#3
c3 = np.dot(a, b)
print(c3)

#4
a4 = np.array([8, 7, 6])
b4 = np.linspace(1, 2, 3)
c4 = a4 * b4
print(c4)

#5
m5 = np.array([[12, 13], [0, 3], [9, 10]])
a5 = np.sin(m5)
print(a5)

#6
b6 = np.cos(m5)
print(b6)

#7
a7 = np.add(a,b)
print(a7)

#8
