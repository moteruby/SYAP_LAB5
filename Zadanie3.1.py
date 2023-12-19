import numpy as np
import matplotlib.pyplot as plt

# Заданные значения
x = 12.1
a_values = np.arange(-5, 12.01, 1.75)

# Вычисление значений функции
f_values = np.exp(a_values * x) - 3.45 * a_values

# Вывод значений аргумента и функции
print("Значения аргумента (a):", a_values)
print("Значения функции (f):", f_values)

# Нахождение наибольшего, наименьшего, среднего и количество элементов массива
max_value = np.max(f_values)
min_value = np.min(f_values)
mean_value = np.mean(f_values)
array_length = len(f_values)

# Вывод результатов
print("\nНаибольшее значение функции:", max_value)
print("Наименьшее значение функции:", min_value)
print("Среднее значение функции:", mean_value)
print("Количество элементов массива:", array_length)

# Сортировка массива
sorted_indices_even = np.argsort(f_values)[::-1]  # четные варианты - по убыванию
sorted_indices_odd = np.argsort(f_values)  # нечетные варианты - по возрастанию

sorted_values_even = f_values[sorted_indices_even]
sorted_values_odd = f_values[sorted_indices_odd]

# Построение графика функции
plt.figure(figsize=(10, 6))
plt.plot(a_values, f_values, marker='o', label='f(x) = e^(ax) - 3.45a')

# График прямой со средним значением функции
plt.axhline(y=mean_value, color='r', linestyle='--', label='Среднее значение f(x)')

# Настройка графика
plt.title('График функции f(x)')
plt.xlabel('Значения a')
plt.ylabel('Значения f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

# Вывод графика
plt.show()
