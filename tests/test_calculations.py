from mohr_circle.calculations import (
    esfuerzo_promedio,
    radio_mohr,
    esfuerzos_principales,
    cortante_maximo,
)


def test_esfuerzo_promedio():
    resultado = esfuerzo_promedio(80, 20)
    assert resultado == 50


def test_radio_mohr():
    resultado = radio_mohr(80, 20, 30)
    assert round(resultado, 2) == 42.43


def test_esfuerzos_principales():
    sigma_1, sigma_2 = esfuerzos_principales(80, 20, 30)

    assert round(sigma_1, 2) == 92.43
    assert round(sigma_2, 2) == 7.57


def test_cortante_maximo():
    resultado = cortante_maximo(80, 20, 30)
    assert round(resultado, 2) == 42.43
