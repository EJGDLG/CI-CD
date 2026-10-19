"""Pruebas unitarias de mathlib.

Por cada función hay:
  - Happy path: al menos dos variaciones de entradas válidas.
  - Casos borde: valores límite (0, 1, negativos...).
  - Casos de error: la función debe lanzar una excepción, no retornar un valor cualquiera.
"""

import pytest

from mathlib import factorial, gcd, is_prime, lcm, square


# --------------------------------------------------------------------------- #
# square(n)
# --------------------------------------------------------------------------- #
class TestSquare:
    def test_entero_positivo(self):
        assert square(4) == 16

    def test_entero_negativo_da_positivo(self):
        assert square(-3) == 9

    def test_decimal(self):
        assert square(1.5) == pytest.approx(2.25)

    def test_cero(self):
        assert square(0) == 0

    @pytest.mark.parametrize("entrada", ["4", None, [2], True])
    def test_tipo_invalido_lanza_type_error(self, entrada):
        with pytest.raises(TypeError):
            square(entrada)


# --------------------------------------------------------------------------- #
# factorial(n)
# --------------------------------------------------------------------------- #
class TestFactorial:
    @pytest.mark.parametrize("n, esperado", [(1, 1), (5, 120), (10, 3628800)])
    def test_enteros_positivos(self, n, esperado):
        assert factorial(n) == esperado

    def test_factorial_de_cero_es_uno(self):
        assert factorial(0) == 1

    @pytest.mark.parametrize("n", [-1, -10])
    def test_negativo_lanza_value_error(self, n):
        with pytest.raises(ValueError):
            factorial(n)

    @pytest.mark.parametrize("entrada", [3.5, "5", None])
    def test_tipo_invalido_lanza_type_error(self, entrada):
        with pytest.raises(TypeError):
            factorial(entrada)


# --------------------------------------------------------------------------- #
# is_prime(n)
# --------------------------------------------------------------------------- #
class TestIsPrime:
    @pytest.mark.parametrize("n", [2, 3, 7, 13, 97, 7919])
    def test_numeros_primos(self, n):
        assert is_prime(n) is True

    @pytest.mark.parametrize("n", [4, 9, 15, 25, 100, 7917])
    def test_numeros_compuestos(self, n):
        assert is_prime(n) is False

    @pytest.mark.parametrize("n", [1, 0, -7])
    def test_menores_que_dos_no_son_primos(self, n):
        assert is_prime(n) is False

    @pytest.mark.parametrize("entrada", [7.0, "7", None])
    def test_tipo_invalido_lanza_type_error(self, entrada):
        with pytest.raises(TypeError):
            is_prime(entrada)


# --------------------------------------------------------------------------- #
# gcd(a, b)
# --------------------------------------------------------------------------- #
class TestGcd:
    @pytest.mark.parametrize("a, b, esperado", [(12, 18, 6), (48, 180, 12), (17, 5, 1)])
    def test_enteros_positivos(self, a, b, esperado):
        assert gcd(a, b) == esperado

    def test_es_conmutativo(self):
        assert gcd(18, 12) == gcd(12, 18)

    @pytest.mark.parametrize("a, b", [(-12, 18), (12, -18), (-12, -18)])
    def test_con_negativos_retorna_positivo(self, a, b):
        assert gcd(a, b) == 6

    def test_con_un_cero_retorna_el_otro(self):
        assert gcd(0, 5) == 5
        assert gcd(5, 0) == 5

    def test_ambos_cero(self):
        assert gcd(0, 0) == 0

    @pytest.mark.parametrize("a, b", [(12.5, 6), (12, "6"), (None, 6)])
    def test_tipo_invalido_lanza_type_error(self, a, b):
        with pytest.raises(TypeError):
            gcd(a, b)


# --------------------------------------------------------------------------- #
# lcm(a, b)
# --------------------------------------------------------------------------- #
class TestLcm:
    @pytest.mark.parametrize("a, b, esperado", [(4, 6, 12), (21, 6, 42), (7, 5, 35)])
    def test_enteros_positivos(self, a, b, esperado):
        assert lcm(a, b) == esperado

    def test_uno_es_multiplo_del_otro(self):
        assert lcm(3, 9) == 9

    @pytest.mark.parametrize("a, b", [(-4, 6), (4, -6), (-4, -6)])
    def test_con_negativos_retorna_positivo(self, a, b):
        assert lcm(a, b) == 12

    def test_con_cero_retorna_cero(self):
        assert lcm(0, 5) == 0
        assert lcm(5, 0) == 0

    @pytest.mark.parametrize("a, b", [(4.0, 6), (4, "6"), (4, None)])
    def test_tipo_invalido_lanza_type_error(self, a, b):
        with pytest.raises(TypeError):
            lcm(a, b)
