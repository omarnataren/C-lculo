import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones
L1 = lambda x: 0.8 * x
f = lambda x: -0.012 * x**2 + 0.8 * x
L2 = lambda x: -1.6 * x + 120

# Rango de x
x1 = np.linspace(-10, 0, 100)  # L1 antes de 0
x2 = np.linspace(0, 100, 500)  # f entre 0 y 100
x3 = np.linspace(100, 110, 100)  # L2 después de 100

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(x1, L1(x1), label="L1: y = 0.8x", color="blue")
plt.plot(x2, f(x2), label="f(x): $-0.012x^2 + 0.8x$", color="green")
plt.plot(x3, L2(x3), label="L2: y = -1.6x + 120", color="red")

# Etiquetas y leyenda
plt.xlabel('x (pies)')
plt.ylabel('y (pies)')
plt.title('Gráfica de la montaña rusa')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()