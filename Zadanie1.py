import numpy as np

x = 2.57 * 10**3
f = 0.873

y = (np.sin((np.pi/8) - f)**2 + (3 + x**2)**(1/4)) / 2

print("Результат выражения:", y)
