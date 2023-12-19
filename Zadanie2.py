import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# 1. Импортировать датасет.
df = pd.read_csv('startdata.csv')

# 2. Взять 1000 хначений из датасета.
df = df.sample(n=1000)

# 3. Проврека на пропуски.
null_counts = df.isnull().sum()

if not any(null_counts):
    print('\n\tДанные не содержат нулевых значений.')
else:
    print('\n\tНайдены нулевые значения:\n', null_counts)

# 4. Проверка на нормальность распределения и выбросы.
plt.figure(figsize=(12,12))
plt.subplot(1,2,1)
df['Square'].plot(kind='box', logy=True)
plt.title('Boxplot with Logarithmic Scale')

plt.subplot(1, 2, 2)
df['Square'].plot(kind='hist', bins=30, logy=True)
plt.title('Histogram with Logarithmic Scale')

plt.show()

# 5. Заполнить пропуски и обрабоать аномаьные значения.
numeric_columns = ['Square', 'LifeSquare', 'KitchenSquare', 'Healthcare_1']

# Заполняем пропуски сред. знач.
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Фильтруем
df = df[(df['Square'] > 20) & (df['Square'] < 200)]

# Повторная проверка
null_counts_after_fill = df.isnull().sum()

if not any(null_counts_after_fill):
    print('\n\tДанные не содержат нулевых значений.')
else:
    print('\n\tНулевые значения, найденны:\n', null_counts_after_fill)

# Повторная проверка на нормальность распределения и выбросы после обработки
plt.figure(figsize=(12, 12))

plt.subplot(1, 2, 1)
df['Square'].plot(kind='box', logy=True)
plt.title('Boxplot with Logarithmic Scale (After Processing)')

plt.subplot(1, 2, 2)
df['Square'].plot(kind='hist', bins=30, logy=True)
plt.title('Histogram with Logarithmic Scale (After Processing)')

plt.show()

# 6. Определить сколько в выборке 1, 2, 3 …комнатных квартир.
room_counts = df['Rooms'].value_counts()
print(f"\n\tКоличество квартир по числу комнат:\n{room_counts}")

# 7. Построить сводную таблицу: подписи строк – районы, подписи колонок – комнаты,
#    пересечение строк и столбцов – количество квартир в этом районе.
pivot_table = df.pivot_table(index='DistrictId', columns='Rooms', values='Id', aggfunc='count', fill_value=0)
print(f"\n\tСводная таблица"f"\n{pivot_table}")

#8 Итоговый обработанный массив сохраните в файл Kovzovich.csv
df.to_csv('finishdata.csv', index=False)
print('\n\tОбработанный массив данных сохранен в файл "Kovzovich.csv".')