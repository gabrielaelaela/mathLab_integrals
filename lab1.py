import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

n = int(input("Введите число точек разбиения: "))
print("Способы оснащения:\n1 - левое\n2 - правое\n3 - среднее")
typ = int(input("Введите способ оснащения (его виды указаны выше): "))
while typ < 0 or typ > 3:
	typ = int(input("Такого варианта нет. Введите число от 1 до 3: "))

a = 0
b = 3
x = np.arange(a, b, 0.01)
plt.plot(x, x**3, color = 'orange', linewidth = 2.5)

length = 3/n
sum = 0;
if (typ == 1):
	for i in range(n):
		x = 3*i/n
		y = x**3
		sum += length*y
		plt.bar(3*i/n + length/2, y, width = 0.9*length, color = 'cornflowerblue')
		plt.title("График функции и ее интегральной суммы для " + str(n) + " точек разбиения и левого оснащения" , fontsize=10 )

elif (typ == 3):
	for i in range(n):
		x = 3*(i+1/2)/n
		y = x**3
		sum += length*y
		plt.bar(3*i/n + length/2, y, width = 0.9*length, color = 'cornflowerblue')
		plt.title("График функции и ее интегральной суммы для " + str(n) + " точек разбиения и среднего оснащения" , fontsize=10 )

elif (typ == 2):
	for i in range(n):
		x = 3*(i+1)/n
		y = x**3
		sum += length*y
		plt.bar(3*i/n + length/2, y, width = 0.9*length, color = 'cornflowerblue')
		plt.title("График функции и ее интегральной суммы для " + str(n) + " точек разбиения и правого оснащения" , fontsize=10 )

plt.xlabel(r'$x$')
plt.ylabel(r'$x^3$')
plt.grid(True)
plt.show()
print(sum)
