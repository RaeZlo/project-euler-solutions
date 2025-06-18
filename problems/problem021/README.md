# Problem 021 - Amicable Numbers
## Enunciado
Permutamos que **d(n)** representa la suma de los divisores propios de `n` (los números menores que `n` que lo dividen exactamente). Si `d(a) = b` y `d(b) = a`, donde `a ≠ b`, entonces `a` y `b` son un **par de números amigos**.

Por ejemplo:

* Los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110. Por tanto, `d(220) = 284`.
* Los divisores propios de 284 son 1, 2, 4, 71 y 142. Por tanto, `d(284) = 220`.

👉 [Enlace al problema original](https://projecteuler.net/problem=21)

**Pregunta:**
Calcula la suma de todos los números amigos menores a **10.000**.

## Enfoque
Se define una función auxiliar `divisors_sum()` que calcula la suma de los divisores propios de un número, iterando hasta su raíz cuadrada y aprovechando la propiedad de que si `i` divide a `n`, entonces `n // i` también lo hace.
Luego, se itera desde 1 hasta 9999, y para cada número `a` se calcula su par `b = d(a)`, y se verifica si `d(b) == a` y `a ≠ b`. Si es así, `a` es parte de un par de números amigos y se suma al total.

Este enfoque es eficiente porque:

* Solo se calcula hasta la raíz cuadrada de cada número al buscar divisores.
* Se evitan duplicados al verificar que `a ≠ b`.
* No se necesita almacenar todos los pares encontrados.

## Resultado esperado
La suma de todos los números amigos menores que 10.000 es: **31626**

## Conceptos aplicados
* Funciones auxiliares reutilizables
* Cálculo eficiente de divisores usando raíz cuadrada
* Aritmética modular (`%`)
* Comparaciones lógicas y condicionales (`if`)
* Pensamiento algorítmico aplicado a teoría de números
* Tipado explícito y funciones bien definidas
* Recorrido secuencial (`for`) con condiciones precisas
