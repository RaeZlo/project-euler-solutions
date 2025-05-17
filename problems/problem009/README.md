## Problem 009 - Special Pythagorean Triplet
### Enunciado
Un triplete pitagórico es un conjunto de tres números naturales, `a < b < c`, para los cuales se cumple que:

a² + b² = c²

Existe exactamente un triplete pitagórico para el cual:
a + b + c = 1000

Encontrá el producto `abc`.

👉 [Enlace al problema original](https://projecteuler.net/problem=9)

### Enfoque
La idea es iterar sobre los valores posibles de `a` y `b`, y calcular `c` como `c = total - a - b`, de modo que siempre se cumpla `a + b + c = total`.

Luego, simplemente se comprueba si `(a² + b²) == c²` para verificar si el triplete es pitagórico.

Este enfoque es efectivo porque:

* Se garantiza que `a < b < c` al controlar los rangos de los bucles.
* Se evita recalcular `a + b + c` en cada iteración, derivando `c` directamente.
* El rango de búsqueda es limitado (hasta `total`) y puede mejorarse aún más limitando a `a < total / 3` y `b < (total - a) / 2`.

### Resultado esperado
El producto del triplete pitagórico especial para el cual `a + b + c = 1000` es: 31875000

### Conceptos aplicados
* Bucles `for` anidados
* Condicionales (`if`)
* Operaciones aritméticas (`**`, `+`, `==`)
* Asignación derivada (`c = total - a - b`)
* Pensamiento lógico-matemático (tripletes pitagóricos, suma fija)
