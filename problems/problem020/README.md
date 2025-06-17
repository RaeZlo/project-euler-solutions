# Problem 020 - Factorial Digit Sum
## Enunciado
n! significa n × (n − 1) × ... × 3 × 2 × 1

Por ejemplo, 10! = 3628800 y la suma de sus dígitos es 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

¿Cuál es la suma de los dígitos del número 100!?

👉 [Enlace al problema original](https://projecteuler.net/problem=20)

## Enfoque
El objetivo es calcular el factorial de un número `n` y luego obtener la suma de los dígitos del resultado. Para esto:

1. Se implementa una función recursiva `custom_factorial()` para obtener `n!`.
2. Se convierte el resultado en cadena para iterar sobre cada dígito.
3. Se suman los dígitos uno a uno utilizando una comprensión de lista.

Antes de realizar el cálculo, la función valida:

- Que el valor ingresado sea un entero (`int`).
- Que no sea un número negativo, ya que el factorial no está definido para estos casos.

Este enfoque es claro y didáctico, especialmente útil para practicar recursividad y validación de entradas.

## Resultado esperado
La suma de los dígitos de 100! es: **648**

## Conceptos aplicados
- Funciones recursivas (`custom_factorial`)
- Validación de tipos y valores (`isinstance`, `if n < 0`)
- Conversión de números a cadenas (`str()`)
- Comprensión de listas
- Iteración sobre cadenas
- Manejo de errores con excepciones personalizadas
