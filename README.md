# Mohr Circle

Librería de Python para el **cálculo y visualización del Círculo de Mohr**, orientada al análisis de estados planos de esfuerzos en Ingeniería Civil.

## Descripción

**Mohr Circle** permite ingresar un estado plano de esfuerzos definido por:

- `σx`: esfuerzo normal en la dirección x.
- `σy`: esfuerzo normal en la dirección y.
- `τxy`: esfuerzo cortante.

A partir de estos datos, la librería calcula automáticamente los principales parámetros asociados al Círculo de Mohr y genera su representación gráfica.

Los valores de entrada deben utilizar la misma unidad, por ejemplo MPa, kPa o Pa.

## Funcionalidades

La librería permite calcular:

- Esfuerzo normal promedio.
- Radio del Círculo de Mohr.
- Esfuerzo principal máximo `σ1`.
- Esfuerzo principal mínimo `σ2`.
- Esfuerzo cortante máximo `τmax`.
- Ángulo principal `θp`.
- Representación gráfica del Círculo de Mohr.

## Ecuaciones utilizadas

### Esfuerzo normal promedio

\[
\sigma_{prom} = \frac{\sigma_x + \sigma_y}{2}
\]

### Radio del Círculo de Mohr

\[
R =
\sqrt{
\left(
\frac{\sigma_x-\sigma_y}{2}
\right)^2
+
\tau_{xy}^2
}
\]

### Esfuerzos principales

\[
\sigma_1 = \sigma_{prom} + R
\]

\[
\sigma_2 = \sigma_{prom} - R
\]

### Esfuerzo cortante máximo

\[
\tau_{max}=R
\]

### Ángulo principal

\[
\theta_p =
\frac{1}{2}
\operatorname{atan2}
\left(
2\tau_{xy},
\sigma_x-\sigma_y
\right)
\]

El ángulo obtenido por la librería se expresa en grados.

## Convención utilizada

Para la representación del Círculo de Mohr se utilizan los puntos:

\[
X=(\sigma_x,\tau_{xy})
\]

\[
Y=(\sigma_y,-\tau_{xy})
\]

Los dos puntos representan planos perpendiculares y forman los extremos de un diámetro del círculo.

El signo del ángulo principal depende de la convención adoptada para el esfuerzo cortante y el sentido positivo de rotación.

## Requisitos

- Python 3.10 o superior.
- pip.
- NumPy.
- Matplotlib.

## Instalación

Clone el repositorio:

```bash
git clone https://github.com/andresgil616/mohr-circle.git
```

Ingrese a la carpeta:

```bash
cd mohr-circle
```

Cree un entorno virtual:

```bash
python3 -m venv .venv
```

Active el entorno virtual en Linux o WSL:

```bash
source .venv/bin/activate
```

Instale la librería:

```bash
pip install -e .
```

Para instrucciones más detalladas consulte:

[Manual de instalación](docs/manual_instalacion.md)

## Uso interactivo

Ejecute:

```bash
python3 examples/ejemplo_basico.py
```

El programa solicitará:

```text
Ingrese σx:
Ingrese σy:
Ingrese τxy:
```

Por ejemplo:

```text
Ingrese σx: 100
Ingrese σy: 40
Ingrese τxy: 20
```

El programa calcula automáticamente los parámetros del Círculo de Mohr.

Para este ejemplo se obtienen aproximadamente:

```text
Esfuerzo promedio: 70.00
Radio: 36.06
Sigma 1: 106.06
Sigma 2: 33.94
Cortante máximo: 36.06
Ángulo principal: 16.85°
```

## Uso como librería de Python

También se pueden utilizar directamente las funciones:

```python
from mohr_circle.calculations import (
    esfuerzo_promedio,
    radio_mohr,
    esfuerzos_principales,
    cortante_maximo,
    angulo_principal,
)

sigma_x = 80
sigma_y = 20
tau_xy = 30

sigma_prom = esfuerzo_promedio(sigma_x, sigma_y)
radio = radio_mohr(sigma_x, sigma_y, tau_xy)
sigma_1, sigma_2 = esfuerzos_principales(sigma_x, sigma_y, tau_xy)
tau_max = cortante_maximo(sigma_x, sigma_y, tau_xy)
angulo = angulo_principal(sigma_x, sigma_y, tau_xy)

print(sigma_1)
print(sigma_2)
print(tau_max)
print(angulo)
```

## Gráfica del Círculo de Mohr

La gráfica puede generarse mediante:

```python
from mohr_circle.plotting import graficar_mohr

graficar_mohr(80, 20, 30)
```

La implementación actual guarda la gráfica generada como:

```text
circulo_mohr.png
```

En entornos sin interfaz gráfica, como algunas configuraciones de WSL, Matplotlib puede mostrar una advertencia indicando que la figura no puede abrirse en una ventana. Esto no afecta los cálculos ni la generación del archivo PNG.

## Pruebas

El proyecto incluye pruebas automáticas de las funciones principales.

Para ejecutarlas:

```bash
pytest
```

## Estructura del proyecto

```text
mohr-circle/
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
├── mohr_circle/
│   ├── __init__.py
│   ├── calculations.py
│   └── plotting.py
├── examples/
│   └── ejemplo_basico.py
├── docs/
│   └── manual_instalacion.md
└── tests/
    └── test_calculations.py
```

## Autor

**Andrés Gil**

Proyecto desarrollado como herramienta académica para la aplicación del Círculo de Mohr mediante Python.
