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
c5 = np.array([[12, 13], [0, 3], [9, 10]])
a5 = np.sin(c5)
print(a5)

#6
b6 = np.cos(c5)
print(b6)

#7
a7 = np.add(a,b)
print(a7)

#8
a8 = np.array([[1, 11, 12], [2, 21, 22], [3, 31, 32]])
for i in a8:
    print(i)
    print(" ")

#9
for i in a8.flat:
    print(i)
    print(" ")

#10
m = np.arange(0,81,1).reshape(9,9)
print(m)
print("możliwości: tabele o 81 elementach")
m1 = m.reshape(3,27)
print(m1)
m2 = m.reshape(27,3)
print(m2)
m3 = m.reshape(81,1)
print(m3)
m4 = m.ravel()
print(m4)
