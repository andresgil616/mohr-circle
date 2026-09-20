from mohr_circle.calculations import (
    esfuerzo_promedio,
    radio_mohr,
    esfuerzos_principales,
    cortante_maximo,
)

# Estado plano de esfuerzos en MPa
sigma_x = 80
sigma_y = 20
tau_xy = 30

# Cálculos
sigma_prom = esfuerzo_promedio(sigma_x, sigma_y)
radio = radio_mohr(sigma_x, sigma_y, tau_xy)
sigma_1, sigma_2 = esfuerzos_principales(sigma_x, sigma_y, tau_xy)
tau_max = cortante_maximo(sigma_x, sigma_y, tau_xy)

# Resultados
print("=== CÍRCULO DE MOHR ===")
print(f"Esfuerzo promedio: {sigma_prom:.2f} MPa")
print(f"Radio: {radio:.2f} MPa")
print(f"Sigma 1: {sigma_1:.2f} MPa")
print(f"Sigma 2: {sigma_2:.2f} MPa")
print(f"Cortante máximo: {tau_max:.2f} MPa")

