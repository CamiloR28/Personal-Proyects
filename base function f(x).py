
import numpy as np
import matplotlib.pyplot as plt

# Definir la función base f(x)
def f(x):
    return np.sin(x)  # Ejemplo: función seno

# Definir el rango de valores de x
x = np.linspace(-10, 10, 400)

# Definir las funciones transformadas
a = lambda x: f(x-4)
b = lambda x: f(x) + 3
c = lambda x: (1/3) * f(x)
d = lambda x: -f(x+4)
e = lambda x: 2 * f(x+6)

# Graficar las funciones transformadas
plt.figure(figsize=(10, 6))

plt.plot(x, f(x), label='f(x)', color='black')
plt.plot(x, a(x), label='f(x-4)')
plt.plot(x, b(x), label='f(x) + 3')
plt.plot(x, c(x), label='1/3 * f(x)')
plt.plot(x, d(x), label='-f(x+4)')
plt.plot(x, e(x), label='2 * f(x+6)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráficas de funciones transformadas')
plt.legend()
plt.grid(True)
plt.show()
