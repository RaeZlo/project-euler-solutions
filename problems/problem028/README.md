# Problem 028 - Number Spiral Diagonals
## Enunciado
Comenzando con el número 1 en el centro de una espiral y moviéndose en el sentido horario en un patrón en espiral cuadrado de tamaño `n x n`, se forma una cuadrícula como esta (para `n = 5`):

```
21 22 23 24 25  
20  7  8  9 10  
19  6  1  2 11  
18  5  4  3 12  
17 16 15 14 13  
```

La suma de los números en ambas diagonales de esta espiral es 101.

¿Cuál es la suma de los números en las diagonales de una espiral de `1001 x 1001`?

👉 [Enlace al problema original](https://projecteuler.net/problem=28)

## Enfoque
La espiral crece capa por capa, y cada capa aumenta el tamaño del lado en 2 unidades (por ejemplo, de 1x1 a 3x3, luego a 5x5, etc.).

En cada nueva capa:

* La esquina superior derecha siempre es el cuadrado del lado actual: `side_length ** 2`
* Las otras tres esquinas se obtienen restando múltiplos de `(side_length - 1)`

Por ejemplo, para un `side_length = 5`:

* Esquinas: 25, 21, 17, 13
* Suma: 25 + 21 + 17 + 13 = 76

Entonces, la suma de todas las esquinas en cada capa se puede generalizar como:

```
4 * (side_length ** 2) - 6 * (side_length - 1)
```

El algoritmo comienza desde el centro (`1`) y recorre todas las capas sumando las esquinas hasta alcanzar el tamaño dado.

El código también incluye una validación para asegurar que el tamaño sea un número impar positivo.

## Resultado esperado
El resultado correcto para una espiral de `1001 x 1001` es: **669171001**

## Conceptos aplicados
* Aritmética matemática y patrones numéricos
* Cálculo de progresiones diagonales en espirales
* Validación de entradas y control de errores
* Tipado estático
* Buenas prácticas: documentación, separación de lógica, legibilidad
* Pensamiento algorítmico aplicado a estructuras numéricas