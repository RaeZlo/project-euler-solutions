# Problem 016 - Power Digit Sum
## Enunciado
2¹⁵ = 32768 y la suma de sus dígitos es 3 + 2 + 7 + 6 + 8 = 26.
¿Cuál es la suma de los dígitos del número 2¹⁰⁰⁰?

👉 [Enlace al problema original](https://projecteuler.net/problem=16)

## Enfoque
La idea es calcular el número resultante de elevar una base a un exponente (`base ** exponent`) y luego sumar todos sus dígitos. Dado que Python permite trabajar con enteros de gran tamaño, no hay pérdida de precisión al elevar 2 a la milésima potencia.

Se realiza lo siguiente:

* Se calcula el número resultante de la potencia.
* Se toma el valor absoluto para evitar errores si el número fuera negativo.
* Se convierte el número en una cadena para iterar sobre cada dígito.
* Se convierte cada carácter de la cadena en entero y se suman.

Este enfoque es directo y eficiente:

* Se evita construir estructuras auxiliares.
* Se aprovechan funciones built-in (`sum`, `str`, `int`).
* Se aplica validación de tipos para asegurar robustez del código.

## Resultado esperado
El resultado correcto para `2^1000` es: **1366**

## Conceptos aplicados
* Tipado estático (`base: int`, `exponent: int`)
* Validación de entradas (`isinstance`)
* Funciones built-in (`abs`, `sum`, `str`, `int`)
* Buenas prácticas:
  * Separación de lógica en función clara
  * Control de errores mediante validaciones
* Pensamiento algorítmico aplicado a operaciones numéricas
