import numpy as np
import matplotlib.pyplot as plt

 
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2.2, 2.4, 6.5, 12.5, 20.1], dtype=float)

n = 2   # Degree of polynomial
m = len(x)
 
sumX = [np.sum(x ** k) for k in range(2 * n + 1)]

 
sumY = [np.sum((x ** k) * y) for k in range(n + 1)]
 
A = np.zeros((n + 1, n + 1))
B = np.zeros(n + 1)

for i in range(n + 1):
    for j in range(n + 1):
        A[i, j] = sumX[i + j]
    B[i] = sumY[i]

 
a = np.linalg.solve(A, B)
print(f"Polynomial coefficients (a0, a1, a2,...): {a}")
 
predictedY = np.zeros_like(x)
for i in range(n + 1):
    predictedY += a[i] * (x ** i)

 
plt.scatter(x, y, label="Data points")
plt.plot(x, predictedY, label=f"Degree {n} fit")
plt.legend()
plt.show()

