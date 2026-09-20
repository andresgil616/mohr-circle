import math
def esfuerzo_promedio(sigma_x, sigma_y):
    """
    Calcula el esfuerzo normal promedio para el Círculo de Mohr.
    """
    sigma_prom = (sigma_x + sigma_y) / 2
    return sigma_prom


def radio_mohr(sigma_x, sigma_y, tau_xy):
    """
    Calcula el radio del Círculo de Mohr.
    """
    radio = (((sigma_x - sigma_y) / 2) ** 2 + tau_xy ** 2) ** 0.5
    return radio


def esfuerzos_principales(sigma_x, sigma_y, tau_xy):
    """
    Calcula los esfuerzos principales sigma_1 y sigma_2.
    """
    sigma_prom = esfuerzo_promedio(sigma_x, sigma_y)
    radio = radio_mohr(sigma_x, sigma_y, tau_xy)

    sigma_1 = sigma_prom + radio
    sigma_2 = sigma_prom - radio

    return sigma_1, sigma_2


def cortante_maximo(sigma_x, sigma_y, tau_xy):
    """
    Calcula el esfuerzo cortante máximo.
    """
    tau_max = radio_mohr(sigma_x, sigma_y, tau_xy)
    return tau_max


def angulo_principal(sigma_x, sigma_y, tau_xy):
    """
    Calcula el ángulo principal del estado de esfuerzos en grados.
    """
    angulo_rad = 0.5 * math.atan2(
        2 * tau_xy,
        sigma_x - sigma_y
    )

    angulo_grados = math.degrees(angulo_rad)

    return angulo_grados
