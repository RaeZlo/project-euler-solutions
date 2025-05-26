# Problem 012 - Highly Divisible Triangular Number
## Enunciado
Los números triangulares se generan al sumar los números naturales secuenciales.
Por ejemplo, los primeros 7 números triangulares son:

> 1, 3, 6, 10, 15, 21, 28, ...

El séptimo número triangular es 28. Tiene los siguientes divisores:
1, 2, 4, 7, 14, 28 → en total, **6 divisores**.

¿Cuál es el primer número triangular que tiene **más de 500 divisores**?

👉 [Enlace al problema original](https://projecteuler.net/problem=12)

### Enfoque
La idea es recorrer los números triangulares utilizando la fórmula:

> T<sub>n</sub> = n × (n + 1) / 2

Para cada número triangular generado, se calcula la cantidad de divisores utilizando una función optimizada basada en recorrer hasta la raíz cuadrada del número.

El algoritmo se detiene tan pronto como se encuentra un número triangular con **más de 500 divisores**.

Este enfoque es eficiente porque:
* La generación del número triangular es directa usando una fórmula cerrada.
* El conteo de divisores aprovecha la simetría en pares de divisores: si `i` divide a `n`, entonces `n // i` también lo hace.
* Se evita guardar o recalcular secuencias innecesarias.

### Resultado esperado
El primer número triangular con más de 500 divisores es: **76576500**

### Conceptos aplicados
* Bucles `while` (para generar números triangulares hasta cumplir la condición)
* Bucles `for` (para contar divisores hasta la raíz cuadrada de un número)
* Condicionales `if`
* Aritmética (números triangulares, divisores, raíz cuadrada)
* Pensamiento lógico e iterativo
* Eficiencia en el conteo de divisores
