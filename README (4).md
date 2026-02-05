# geometry-volume-app-course

Una pequeña aplicación educativa para calcular volúmenes de figuras geométricas (caja, cono, cilindro y esfera). Contiene funciones modulares en el paquete `geometry` y un conjunto de tests con `pytest`.

## Estructura del proyecto

- `main.py`: Script principal de ejemplo que muestra el uso de las funciones de volumen.
- `geometry/`: Paquete que contiene las implementaciones de las funciones de volumen.
	- `box.py` — `volume_box(width, height, depth)`
	- `cone.py` — `volume_cone(base_radius, height)`
	- `cylinder.py` — `volume_cylinder(radius, height)`
	- `sphere.py` — `volume_sphere(radius)`
- `tests/`: Pruebas unitarias usando `pytest`.

## Cómo ejecutar `main.py`

Desde la raíz del proyecto ejecuta:

```bash
python main.py
```

Esto mostrará ejemplos de uso para algunas de las funciones de volumen.

## Cómo ejecutar los tests

Instala `pytest` si no lo tienes y ejecuta los tests:

```bash
pip install -U pytest
pytest -q
```

Los tests comprueban valores esperados y comportamiento ante entradas negativas.

## Dependencias

- Python 3.8 o superior
- `pytest` (solo para ejecutar pruebas)

No se usan librerías externas para el cálculo geométrico (se usa `math` de la librería estándar).

---

Si quieres que haga un commit con estos cambios, dímelo y lo hago por ti.
