import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definir variables
k, l, m, n, a, b, c, p, q, r, s = sp.symbols('k l m n a b c p q r s')

# Definir las ecuaciones
eq1 = sp.Eq(n, 0)
eq2 = sp.Eq(k*10**3 + l*10**2 + m*10 + n, a*10**2 + b*10 + c)
eq3 = sp.Eq(a*90**2 + b*90 + c, p*90**3 + q*90**2 + r*90 + s)
eq4 = sp.Eq(p*100**3 + q*100**2 + r*100 + s, -1.6*100 + 80)
eq5 = sp.Eq(m, 0.8)
eq6 = sp.Eq(3*k*10**2 + 2*l*10 + m, 2*a*10 + b)
eq7 = sp.Eq(2*a*90 + b, 3*p*90**2 + 2*q*90 + r)
eq8 = sp.Eq(3*p*100**2 + 2*q*100 + r, -1.6)
eq9 = sp.Eq(6*k*10 + 2*l, 2*a)
eq10 = sp.Eq(2*a, 6*p*90 + 2*q)
eq11 = sp.Eq(6*p*100 + 2*q, 0)

# Resolver el sistema de ecuaciones
sol = sp.solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11), (k, l, m, n, a, b, c, p, q, r, s))

k_val, l_val, m_val, n_val = sol[k], sol[l], sol[m], sol[n]
a_val, b_val, c_val = sol[a], sol[b], sol[c]
p_val, q_val, r_val, s_val = sol[p], sol[q], sol[r], sol[s]

# Definir las funciones
def t(x):
    return k_val*x**3 + l_val*x**2 + m_val*x + n_val

def q(x):
    return a_val*x**2 + b_val*x + c_val

def h(x):
    return p_val*x**3 + q_val*x**2 + r_val*x + s_val

def L1(x):
    return 0.8 * x

def L2(x):
    return -1.6 * x + 80

# Valores x para graficar
x1 = np.linspace(-10, 0, 100)
x2 = np.linspace(0, 10, 100)
x3 = np.linspace(10, 90, 100)
x4 = np.linspace(90, 100, 100)
x5 = np.linspace(100, 110, 100)

# Crear la figura
plt.figure(figsize=(10, 6))

# Graficar las funciones
plt.plot(x1, L1(x1), label='L1', color='magenta')
plt.plot(x2, t(x2), label='t', color='blue')
plt.plot(x3, q(x3), label='q', color='cyan')
plt.plot(x4, h(x4), label='h', color='green')
plt.plot(x5, L2(x5), label='L2', color='magenta')

# Configurar la gráfica
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.xlabel('x (pies)')
plt.ylabel('y (pies)')
plt.title('Gráfica de L1, t, q, h y L2')
plt.show()
