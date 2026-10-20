"""Operaciones de matemática básica.

Cada función valida sus argumentos y lanza una excepción cuando recibe
una entrada inválida, en lugar de retornar un valor arbitrario:

- TypeError  -> el tipo del argumento no es el esperado (texto, None, bool, float donde se espera entero...).
- ValueError -> el tipo es correcto pero el valor no tiene sentido matemático (ej. factorial de un negativo).
"""

from numbers import Real


def _validar_entero(valor, nombre):
    # bool es subclase de int en Python (True == 1), por eso se excluye explícitamente.
    if isinstance(valor, bool) or not isinstance(valor, int):
        raise TypeError(
            f"'{nombre}' debe ser un número entero, se recibió {type(valor).__name__}"
        )


def _validar_numero(valor, nombre):
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise TypeError(
            f"'{nombre}' debe ser un número, se recibió {type(valor).__name__}"
        )


def square(n):
    """Retorna el cuadrado de un número (entero o decimal)."""
    _validar_numero(n, "n")
    return n * n


def factorial(n):
    """Retorna n! para un entero n >= 0. Por definición, 0! = 1."""
    _validar_entero(n, "n")
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def is_prime(n):
    """Retorna True si n es primo. Los enteros menores que 2 no son primos."""
    _validar_entero(n, "n")
    if n < 2:
        return False
    if n < 4:
        return True  # 2 y 3
    if n % 2 == 0:
        return False
    # Solo hace falta probar divisores impares hasta la raíz cuadrada de n.
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def gcd(a, b):
    """Retorna el máximo común divisor de a y b (algoritmo de Euclides).

    El resultado siempre es no negativo. Por convención gcd(0, 0) = 0.
    """
    _validar_entero(a, "a")
    _validar_entero(b, "b")
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Retorna el mínimo común múltiplo de a y b.

    El resultado siempre es no negativo. Por convención lcm(a, 0) = 0.
    """
    _validar_entero(a, "a")
    _validar_entero(b, "b")
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
