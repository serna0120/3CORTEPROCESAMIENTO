import numpy as np
import matplotlib.pyplot as plt

# Datos de tiempo (segundos) y velocidad (m/s)
tiempo = np.array([20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92])
velocidad = np.array([19.44, 18.61, 20.27, 20.27, 20, 20.27, 19.44, 19.44, 19.16, 19.16, 19.16, 20, 20.83, 21.38, 22.22, 22.22, 23.33, 23.05, 23.05, 22.5, 22.22, 21.94, 21.66, 21.38, 21.38])

# Método del Trapecio
def integral_trapecio(x, y):
    h = np.diff(x)
    integral = np.sum((y[:-1] + y[1:]) * h / 2)
    return integral

# Método de Simpson 1/3
def integral_simpson_13(x, y):
    n = len(x) - 1
    if n % 2 != 0:
        raise ValueError("El método Simpson 1/3 requiere un número par de segmentos.")
    h = (x[-1] - x[0]) / n
    integral = y[0] + y[-1]
    integral += 4 * np.sum(y[1:-1:2])  # Suma de términos impares
    integral += 2 * np.sum(y[2:-2:2])  # Suma de términos pares
    integral *= h / 3
    return integral

# Método de Simpson 3/8
def integral_simpson_38(x, y):
    n = len(x) - 1
    if n % 3 != 0:
        raise ValueError("El método Simpson 3/8 requiere que el número de segmentos sea múltiplo de 3.")
    h = (x[-1] - x[0]) / n
    integral = y[0] + y[-1]
    integral += 3 * np.sum(y[1:-1:3] + y[2:-1:3])  # Términos de cada 3 posiciones
    integral += 2 * np.sum(y[3:-3:3])  # Términos restantes
    integral *= 3 * h / 8
    return integral

# Cálculo de la distancia verdadera (promedio de velocidades * tiempo total)
velocidad_promedio = np.mean(velocidad)
tiempo_total = tiempo[-1] - tiempo[0]
distancia_verdadera = velocidad_promedio * tiempo_total

# Cálculo de integrales
integral_trap = integral_trapecio(tiempo, velocidad)

try:
    integral_simp_13 = integral_simpson_13(tiempo, velocidad)
except ValueError as e:
    print(e)
    integral_simp_13 = None

try:
    integral_simp_38 = integral_simpson_38(tiempo, velocidad)
except ValueError as e:
    print(e)
    integral_simp_38 = None

# Cálculo de errores
def calcular_errores(distancia_verdadera, distancia_calculada):
    error_absoluto = abs(distancia_verdadera - distancia_calculada)
    error_porcentual = (error_absoluto / distancia_verdadera) * 100
    return round(error_absoluto, 3), round(error_porcentual, 3)

distancia_verdadera = round(distancia_verdadera, 3)
integral_trap = round(integral_trap, 3)
error_trap = calcular_errores(distancia_verdadera, integral_trap)

if integral_simp_13 is not None:
    integral_simp_13 = round(integral_simp_13, 3)
    error_simp_13 = calcular_errores(distancia_verdadera, integral_simp_13)
else:
    error_simp_13 = (None, None)

if integral_simp_38 is not None:
    integral_simp_38 = round(integral_simp_38, 3)
    error_simp_38 = calcular_errores(distancia_verdadera, integral_simp_38)
else:
    error_simp_38 = (None, None)

# Mostrar resultados
print("Distancia verdadera:", distancia_verdadera, "m")
print("Integral usando el método del Trapecio:", integral_trap, "m")
print("Error absoluto (Trapecio):", error_trap[0], "m")
print("Error porcentual (Trapecio):", error_trap[1], "%")

if integral_simp_13 is not None:
    print("Integral usando el método de Simpson 1/3:", integral_simp_13, "m")
    print("Error absoluto (Simpson 1/3):", error_simp_13[0], "m")
    print("Error porcentual (Simpson 1/3):", error_simp_13[1], "%")

if integral_simp_38 is not None:
    print("Integral usando el método de Simpson 3/8:", integral_simp_38, "m")
    print("Error absoluto (Simpson 3/8):", error_simp_38[0], "m")
    print("Error porcentual (Simpson 3/8):", error_simp_38[1], "%")
