import numpy as np

X = np.column_stack((np.ones(12), np.random.randint(9, 21, 12), np.random.randint(60, 82, 12)))

Y = np.random.uniform(13.5, 18.6, (12, 1))

A = np.linalg.inv(X.T @ X) @ (X.T @ Y)

print("Вектор оценок A:")
print(A)

Y_new = X @ A

print("\nСравнение с исходными значениями Y:")
print(np.column_stack((Y, Y_new)))