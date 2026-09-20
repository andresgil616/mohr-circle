from mohr_circle.calculations import (
    esfuerzo_promedio,
    radio_mohr,
    esfuerzos_principales,
    cortante_maximo,
    angulo_principal,
)

from mohr_circle.plotting import graficar_mohr


print("=== CÍRCULO DE MOHR ===")
print("Ingrese los valores del estado plano de esfuerzos.\n")

# Entrada de datos
sigma_x = float(input("Ingrese σx: "))
sigma_y = float(input("Ingrese σy: "))
tau_xy = float(input("Ingrese τxy: "))

# Cálculos
sigma_prom = esfuerzo_promedio(sigma_x, sigma_y)
radio = radio_mohr(sigma_x, sigma_y, tau_xy)
sigma_1, sigma_2 = esfuerzos_principales(sigma_x, sigma_y, tau_xy)
tau_max = cortante_maximo(sigma_x, sigma_y, tau_xy)
angulo = angulo_principal(sigma_x, sigma_y, tau_xy)

# Resultados
print("\n=== RESULTADOS ===")
print(f"Esfuerzo promedio: {sigma_prom:.2f}")
print(f"Radio: {radio:.2f}")
print(f"Sigma 1: {sigma_1:.2f}")
print(f"Sigma 2: {sigma_2:.2f}")
print(f"Cortante máximo: {tau_max:.2f}")
print(f"Ángulo principal: {angulo:.2f}°")

# Gráfica
graficar_mohr(sigma_x, sigma_y, tau_xy)
