# Problem 001 - Multiples of 3 and 5

## Enunciado

If we list all the natural numbers below 10 that are multiples of 3 or 5,  
we get 3, 5, 6 and 9. The sum of these multiples is 23.

**Find the sum of all the multiples of 3 or 5 below 1000.**

👉 [Enlace al problema original](https://projecteuler.net/problem=1)

## Enfoque

La idea es recorrer todos los números naturales menores a 1000 y sumar aquellos que sean divisibles por 3 o por 5.

Esto se puede resolver eficientemente usando una **comprensión de listas** o simplemente un bucle `for` con una condición de divisibilidad (`% 3 == 0 or % 5 == 0`).

Además, en versiones más optimizadas se puede usar una fórmula matemática para la suma de múltiplos (no implementada aquí, pero mencionada como posible mejora).

## Resultado esperado

El resultado correcto para el límite de 1000 es:
233168

## Conceptos aplicados

- Bucles y condiciones
- Operadores lógicos
- Comprensiones de listas
- Pensamiento lógico
