# Problem 024 - Lexicographic permutations
## Enunciado
Una permutación es un ordenamiento de objetos.
Por ejemplo, 3124 es una permutación posible de los dígitos 1, 2, 3 y 4.
Si todas las permutaciones se ordenan numéricamente, se dice que están en orden lexicográfico.

¿Cuál es la millonésima permutación lexicográfica de los dígitos del 0 al 9?

👉 [Enlace al problema original](https://projecteuler.net/problem=24)

## Enfoque
La estrategia no consiste en generar todas las permutaciones posibles, sino en **calcular directamente la permutación deseada** usando un enfoque matemático basado en el **factorial de las posiciones**:

1. Se observa que para `n` elementos hay `n!` permutaciones posibles.
2. Dado que las permutaciones lexicográficas están ordenadas, cada dígito ocupa una posición fija durante bloques de `k!` permutaciones.
3. A partir de eso, se puede determinar cuál debe ser el primer dígito, luego el segundo, y así sucesivamente, **sin tener que generar todas las permutaciones**.

Este enfoque es eficiente porque:

* Se evita el coste computacional de generar las `10! = 3.628.800` permutaciones.
* Se aplica aritmética de división y módulo para determinar índices directamente.
* Se trabaja con una copia ordenada de los dígitos disponibles, quitando los ya usados.

## Resultado esperado
La millonésima permutación lexicográfica de los dígitos del 0 al 9 es: **2783915460**

## Conceptos aplicados
* Factorial (`math.factorial`)
* Aritmética modular (`%`) y división entera (`//`)
* Indexación basada en cero
* Estructuras de datos: listas mutables (`list.pop()`)
* Pensamiento algorítmico (reducir combinatoria a pasos determinísticos)
* Validación de entradas con excepciones (`IndexError`)
* Orden lexicográfico y permutaciones
