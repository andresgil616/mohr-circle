import matplotlib.pyplot as plt
import numpy as np

from .calculations import (
    esfuerzo_promedio,
    radio_mohr,
    esfuerzos_principales,
    cortante_maximo,
    angulo_principal,
)


def graficar_mohr(sigma_x, sigma_y, tau_xy):
    """
    Grafica el Círculo de Mohr para un estado plano de esfuerzos.
    """

    # Cálculos
    centro = esfuerzo_promedio(sigma_x, sigma_y)
    radio = radio_mohr(sigma_x, sigma_y, tau_xy)
    sigma_1, sigma_2 = esfuerzos_principales(
        sigma_x, sigma_y, tau_xy
    )
    tau_max = cortante_maximo(
        sigma_x, sigma_y, tau_xy
    )
    angulo = angulo_principal(
        sigma_x, sigma_y, tau_xy
    )

    # Puntos del círculo
    theta = np.linspace(0, 2 * np.pi, 360)

    sigma = centro + radio * np.cos(theta)
    tau = radio * np.sin(theta)

    # Crear figura
    plt.figure(figsize=(8, 8))

    # Círculo de Mohr
    plt.plot(sigma, tau, label="Círculo de Mohr")

    # Ejes
    plt.axhline(0)
    plt.axvline(centro, linestyle="--")

    plt.xlabel("Esfuerzo normal σ (MPa)")
    plt.ylabel("Esfuerzo cortante τ (MPa)")
    plt.title("Círculo de Mohr")

    # Estado inicial de esfuerzos
    plt.scatter(sigma_x, tau_xy, label="Estado X")
    plt.scatter(sigma_y, -tau_xy, label="Estado Y")

    plt.plot(
        [sigma_x, sigma_y],
        [tau_xy, -tau_xy],
        linestyle="--"
    )

    # Puntos principales
    plt.scatter(sigma_1, 0, label="σ1")
    plt.scatter(sigma_2, 0, label="σ2")
    plt.scatter(centro, tau_max, label="τ máx")
    plt.scatter(centro, -tau_max)

    # Resultados dentro de la gráfica
    resultados = (
        f"σprom = {centro:.2f} MPa\n"
        f"σ1 = {sigma_1:.2f} MPa\n"
        f"σ2 = {sigma_2:.2f} MPa\n"
        f"τmáx = {tau_max:.2f} MPa\n"
        f"θp = {angulo:.2f}°"
    )

    ax = plt.gca()

    ax.text(
    0.03,
    0.97,
    resultados,
    transform=ax.transAxes,
    verticalalignment="top",
    horizontalalignment="left",
    fontsize=10,
    zorder=10,
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="white",
        edgecolor="black",
        alpha=0.9
    )
)

    # Configuración final
    plt.grid(True)
    plt.legend(loc="upper right")
    plt.axis("equal")
    plt.tight_layout()

    # Guardar imagen
    plt.savefig("circulo_mohr.png", dpi=300)

    # Mostrar gráfica
    plt.show()
