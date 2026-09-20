# Manual de instalación - Mohr Circle

## 1. Descripción

Mohr Circle es una librería desarrollada en Python para realizar cálculos relacionados con el Círculo de Mohr aplicado al análisis de estados planos de esfuerzos.

La librería permite calcular:

- Esfuerzo normal promedio.
- Radio del Círculo de Mohr.
- Esfuerzos principales σ1 y σ2.
- Esfuerzo cortante máximo.
- Ángulo principal.
- Representación gráfica del Círculo de Mohr.

## 2. Requisitos

Para utilizar la librería se recomienda tener instalado:

- Python 3.10 o superior.
- pip.
- Git.

Las dependencias principales del proyecto son:

- NumPy.
- Matplotlib.

## 3. Descargar el proyecto

Abra una terminal y ejecute:

    git clone https://github.com/andresgil616/mohr-circle.git

Después ingrese a la carpeta del proyecto:

    cd mohr-circle

## 4. Crear un entorno virtual

Se recomienda utilizar un entorno virtual para mantener las dependencias del proyecto separadas de otras instalaciones de Python.

En Linux o WSL:

    python3 -m venv .venv
    source .venv/bin/activate

En Windows PowerShell:

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

## 5. Instalar la librería

Con el entorno virtual activado, ejecute:

    pip install -e .

La opción `-e` instala el proyecto en modo editable, permitiendo que los cambios realizados en el código se reflejen sin tener que reinstalar la librería.

## 6. Comprobar la instalación

Puede comprobar que la librería fue instalada correctamente ejecutando:

    pip show mohr-circle

## 7. Ejecutar el ejemplo

Desde la carpeta principal del proyecto ejecute:

    python examples/ejemplo_basico.py

En algunos sistemas Linux o WSL puede utilizar:

    python3 examples/ejemplo_basico.py

## 8. Datos de entrada

La librería trabaja con un estado plano de esfuerzos definido mediante:

- σx: esfuerzo normal en la dirección x.
- σy: esfuerzo normal en la dirección y.
- τxy: esfuerzo cortante.

Los tres valores deben utilizar la misma unidad, por ejemplo MPa, kPa o Pa.

## 9. Ejemplo

Para el estado de esfuerzos:

    σx = 80 MPa
    σy = 20 MPa
    τxy = 30 MPa

se obtienen aproximadamente:

    Esfuerzo promedio = 50.00 MPa
    Radio = 42.43 MPa
    σ1 = 92.43 MPa
    σ2 = 7.57 MPa
    τmax = 42.43 MPa
    Ángulo principal = 22.50°

## Autor

Andrés Gil
