import matplotlib.pyplot as plt
import numpy as np

from .calculations import esfuerzo_promedio, radio_mohr


def graficar_mohr(sigma_x, sigma_y, tau_xy):
    """
    Grafica el Círculo de Mohr para un estado plano de esfuerzos.
    """
    centro = esfuerzo_promedio(sigma_x, sigma_y)
    radio = radio_mohr(sigma_x, sigma_y, tau_xy)
    theta = np.linspace(0, 2 * np.pi, 360)

    sigma = centro + radio * np.cos(theta)
    tau = radio * np.sin(theta)
    plt.figure(figsize=(8, 8))

    plt.plot(sigma, tau, label="Círculo de Mohr")

    plt.axhline(0)
    plt.axvline(centro, linestyle="--")

    plt.xlabel("Esfuerzo normal σ (MPa)")
    plt.ylabel("Esfuerzo cortante τ (MPa)")
    plt.title("Círculo de Mohr")
    plt.scatter(sigma_x, tau_xy, label="Estado X")
    plt.scatter(sigma_y, -tau_xy, label="Estado Y")

    plt.plot(
        [sigma_x, sigma_y],
        [tau_xy, -tau_xy],
        linestyle="--"
    )
    sigma_1 = centro + radio
    sigma_2 = centro - radio
    tau_max = radio

    plt.scatter(sigma_1, 0, label="σ1")
    plt.scatter(sigma_2, 0, label="σ2")
    plt.scatter(centro, tau_max, label="τ máx")
    plt.scatter(centro, -tau_max)
    plt.grid(True)
    plt.legend()
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig("circulo_mohr.png", dpi=300)
    plt.show()
