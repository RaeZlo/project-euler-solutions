# Problem 014 - Longest Collatz Sequence
## Enunciado
La secuencia de Collatz se genera a partir de un número entero positivo `n` siguiendo estas reglas:

* Si `n` es par, el siguiente número es `n / 2`.
* Si `n` es impar, el siguiente número es `3n + 1`.

La secuencia termina al llegar al número 1.

Por ejemplo, comenzando con 13, se genera la siguiente secuencia:

```
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

Esta secuencia tiene 10 términos. Aunque aún no está demostrado, se cree que todas las secuencias terminan en 1.

**¿Cuál es el número inicial menor que un millón que genera la secuencia de Collatz más larga?**

👉 [Enlace al problema original](https://projecteuler.net/problem=14)

## Enfoque
Para resolver este problema, se recorre cada número desde 2 hasta el límite indicado (en este caso, 1 millón), generando su secuencia de Collatz y calculando su longitud.

Para optimizar el cálculo, se implementó **memoización**: un diccionario guarda la longitud ya calculada de secuencias previas, evitando repetir cálculos innecesarios. Cuando una secuencia alcanza un número ya calculado, se reutiliza el resultado directamente.

Este enfoque es eficiente porque:

* **Evita cálculos redundantes** usando memoización.
* **Reduce drásticamente el tiempo de ejecución** al reutilizar resultados previos.
* Usa estructuras simples como bucles y diccionarios para maximizar claridad y rendimiento.

## Resultado esperado
El número inicial menor que 1 millón que genera la secuencia de Collatz más larga es: **837799**

## Conceptos aplicados
* Bucles `while`
* Estructuras condicionales (`if`)
* División entera (`//`)
* Aritmética modular (`%`)
* Diccionarios para almacenamiento en caché
* **Memoización** para mejorar eficiencia
* Pensamiento algorítmico y análisis de secuencias numéricas

## Aprendizaje personal
Gracias a este ejercicio aprendí el uso de **memoización** para optimizar funciones recursivas o iterativas que repiten cálculos. Esta técnica es especialmente útil en problemas donde los subresultados se repiten, y su aplicación marcó una diferencia significativa en el rendimiento de la solución.
