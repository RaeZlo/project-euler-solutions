# Problem 025 - 1000-digit Fibonacci number

## Enunciado
La sucesión de Fibonacci se define por la siguiente relación de recurrencia:
**F₁ = 1**, **F₂ = 1**, y **Fₙ = Fₙ₋₁ + Fₙ₋₂** para **n > 2**.

Al continuar esta secuencia, se encuentra que **el primer término de la sucesión de Fibonacci que contiene 1000 dígitos es el término número 4782**.

> ¿Cuál es el índice del primer número de Fibonacci que tiene al menos `n` dígitos?

👉 [Enlace al problema original](https://projecteuler.net/problem=25)

## Enfoque
La estrategia consiste en generar los términos de la sucesión de Fibonacci de forma iterativa, hasta que uno de ellos alcance la cantidad deseada de dígitos. Para ello:

* Se inicializa la secuencia con los dos primeros términos: 1 y 1.
* Se mantiene un contador (`index`) que representa la posición del término actual.
* En cada iteración se calcula el siguiente número de Fibonacci sumando los dos anteriores.
* Se evalúa la cantidad de dígitos convirtiendo el número a cadena (`str()`) y usando `len()`.
* Se detiene la ejecución cuando se encuentra el primer término con al menos `n` dígitos.

Este enfoque evita el almacenamiento de toda la secuencia y calcula solo lo necesario.

## Resultado esperado
Para `n = 1000`, el índice del primer número de Fibonacci con al menos 1000 dígitos es: **4782**

## Conceptos aplicados
* Generación iterativa de la sucesión de Fibonacci.
* Conversión de enteros a strings (`str()`).
* Conteo de dígitos mediante `len()`.
* Uso de variables auxiliares (`previous`, `current`) para mantener el estado.
* Validación de entrada (`n <= 1`).
* Tipado de parámetros y valores de retorno.
