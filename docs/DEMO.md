# Guion de la demostración en vivo

Objetivo: mostrar un Pull Request con una prueba que falla y el merge bloqueado, luego la corrección
y el merge habilitado.

## Antes de la clase

- [ ] La regla de protección de `main` está activa (ver README → *Protección de la rama `main`*).
- [ ] En la pestaña **Actions** del repo, el último run en `main` está en verde.
- [ ] Tu copia local está actualizada: `git checkout main && git pull`.

## 1. Crear una rama y romper una función a propósito

```bash
git checkout -b demo/romper-factorial
```

En `mathlib/operations.py`, dentro de `factorial`, cambiar:

```python
resultado = 1
```

por:

```python
resultado = 0
```

Opcional, para mostrarlo localmente antes de subirlo:

```bash
pytest
# 4 failed, 54 passed
```

```bash
git add mathlib/operations.py
git commit -m "Cambiar valor inicial de factorial"
git push -u origin demo/romper-factorial
```

## 2. Abrir el Pull Request y mostrar el bloqueo

1. En GitHub aparece el aviso *"demo/romper-factorial had recent pushes"* → **Compare & pull request** → **Create pull request**.
2. El check **CI / Pruebas unitarias** corre y queda en ❌ rojo.
3. Se muestra **"Merging is blocked"** y el botón de merge deshabilitado.
4. Clic en **Details** del check para mostrar en el log qué pruebas fallaron:
   `test_enteros_positivos[1-1]`, `[5-120]`, `[10-3628800]` y `test_factorial_de_cero_es_uno`.

## 3. Corregir y mostrar el merge habilitado

Volver a poner `resultado = 1` en `factorial`, y luego:

```bash
git add mathlib/operations.py
git commit -m "Corregir valor inicial de factorial"
git push
```

El check vuelve a correr en el mismo PR, queda en ✅ verde y el botón **Merge pull request** se habilita.
Hacer el merge.

Después del merge:

```bash
git checkout main
git pull
git branch -d demo/romper-factorial
```

## Otras formas de romper funciones (por si piden otra en vivo)

Todas fueron probadas: en cada caso las pruebas fallan.

| Cambio en `mathlib/operations.py` | Pruebas que fallan |
|---|---|
| `square`: `return n * n` → `return n * 2` | 3 — `test_entero_positivo`, `test_entero_negativo_da_positivo`, `test_decimal` |
| `square`: borrar la línea `_validar_numero(n, "n")` | 1 — `test_tipo_invalido_lanza_type_error[True]` (`True * True` retorna `1` en vez de dar error) |
| `factorial`: `range(2, n + 1)` → `range(2, n)` | 2 — `[5-120]` y `[10-3628800]` |
| `factorial`: borrar el bloque `if n < 0: raise ValueError(...)` | 2 — `test_negativo_lanza_value_error` (retorna 1 en vez de lanzar la excepción) |
| `is_prime`: `divisor * divisor <= n` → `divisor * divisor < n` | 2 — `test_numeros_compuestos[9]` y `[25]` (los cuadrados de primos se detectan como primos) |
| `is_prime`: en `if n < 2:` cambiar `return False` → `return True` | 3 — `test_menores_que_dos_no_son_primos` |
| `gcd`: borrar la línea `a, b = abs(a), abs(b)` | 4 — `test_con_negativos_retorna_positivo` de `TestGcd` y de `TestLcm` (porque `lcm` usa `gcd`) |
| `lcm`: `abs(a * b) // gcd(a, b)` → `abs(a * b)` | 6 — `test_enteros_positivos`, `test_uno_es_multiplo_del_otro`, `test_con_negativos_retorna_positivo` |

## Preguntas que pueden hacer

- **¿Por qué `TypeError` y no `ValueError`?** `TypeError` es para cuando el tipo es incorrecto (un texto en lugar de un número).
  `ValueError` es para cuando el tipo es correcto pero el valor no tiene sentido (el factorial de un negativo).
- **¿Por qué se rechaza `True`?** En Python `bool` es subclase de `int`. Sin la validación, `factorial(True)` retornaría `1` silenciosamente.
- **¿Por qué `is_prime` solo prueba hasta la raíz cuadrada?** Si `n = a·b` con `a ≤ b`, entonces `a ≤ √n`, así que si no hay divisor hasta `√n`, no hay ninguno.
- **¿Cómo funciona `gcd`?** Algoritmo de Euclides: `gcd(a, b) = gcd(b, a mod b)` hasta que `b = 0`.
- **¿Y `lcm`?** `lcm(a, b) = |a·b| / gcd(a, b)`.
- **¿Qué impide el merge?** La regla de protección de `main` exige que el status check *Pruebas unitarias* esté en verde.
