# CI-CD — mathlib

[![CI](https://github.com/EJGDLG/CI-CD/actions/workflows/ci.yml/badge.svg)](https://github.com/EJGDLG/CI-CD/actions/workflows/ci.yml)

Sesión Práctica #7 — Continuous Integration
CC3047 Administración y Mantenimiento de Sistemas · Universidad del Valle de Guatemala

Librería pequeña de **matemática básica (Opción A)** escrita en Python, con pruebas unitarias en
`pytest` y un workflow de **GitHub Actions** que ejecuta las pruebas en cada Pull Request hacia `main`.
La rama `main` está protegida: no se puede hacer merge mientras las pruebas no pasen.

## Funciones

| Función | Qué retorna | Casos borde | Errores (excepciones) |
|---|---|---|---|
| `square(n)` | El cuadrado de `n` (entero o decimal) | `square(0) == 0`, negativos dan positivo | `TypeError` si `n` no es número (`"4"`, `None`, `True`) |
| `factorial(n)` | `n!` | `factorial(0) == 1` | `ValueError` si `n < 0`; `TypeError` si `n` no es entero (`3.5`, `"5"`) |
| `is_prime(n)` | `True` si `n` es primo | `0`, `1` y negativos → `False` | `TypeError` si `n` no es entero (`7.0`, `"7"`) |
| `gcd(a, b)` | Máximo común divisor (Euclides) | Negativos → resultado positivo; `gcd(0, 5) == 5`; `gcd(0, 0) == 0` | `TypeError` si `a` o `b` no son enteros |
| `lcm(a, b)` | Mínimo común múltiplo | Negativos → resultado positivo; `lcm(a, 0) == 0` | `TypeError` si `a` o `b` no son enteros |

Nota: `bool` se rechaza a propósito. En Python `True` es un `int` (vale 1), así que sin esa validación
`square(True)` retornaría `1` en lugar de reportar el error.

## Estructura

```
.
├── .github/workflows/ci.yml   # Workflow de GitHub Actions
├── mathlib/
│   ├── __init__.py
│   └── operations.py          # Implementación de las 5 funciones
├── tests/
│   └── test_operations.py     # Pruebas unitarias (58 casos)
├── docs/DEMO.md               # Guion para la demostración en clase
├── pyproject.toml             # Configuración de pytest
└── requirements.txt
```

## Cómo correr las pruebas localmente

```bash
python -m venv .venv
# Windows:      .venv\Scripts\activate
# Linux/macOS:  source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Pruebas

Cada función tiene una clase de pruebas en [tests/test_operations.py](tests/test_operations.py) con:

1. **Happy path** — al menos dos variaciones de entradas válidas (por ejemplo `factorial(1)`, `factorial(5)`, `factorial(10)`).
2. **Casos borde** — valores límite como `0`, `1` y negativos.
3. **Casos de error** — se verifica con `pytest.raises` que la función lanza la excepción correcta
   en lugar de retornar un valor cualquiera.

Si se rompe la lógica de cualquier función, las pruebas fallan. Ver [docs/DEMO.md](docs/DEMO.md)
para ejemplos concretos de qué cambio hace fallar qué prueba.

## Integración continua

El workflow [.github/workflows/ci.yml](.github/workflows/ci.yml) se ejecuta en:

- cada **Pull Request** hacia `main`
- cada **push** a `main`

Instala Python 3.13 y las dependencias, y corre `pytest`. Si alguna prueba falla, el job
**Pruebas unitarias** queda en rojo.

### Protección de la rama `main`

En **Settings → Branches → Add branch protection rule** (o **Settings → Rules → Rulesets**) para `main`:

- ✅ Require a pull request before merging
- ✅ Require status checks to pass before merging → status check: **Pruebas unitarias**
- ✅ Do not allow bypassing the above settings

Con esto, el botón de merge de un PR queda bloqueado hasta que el job **Pruebas unitarias** pase.
