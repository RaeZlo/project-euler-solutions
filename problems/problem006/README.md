## Problem 006 - Sum Square Difference
### Enunciado
La suma de los cuadrados de los primeros diez números naturales es:
1² + 2² + ... + 10² = 385

El cuadrado de la suma de los primeros diez números naturales es:

(1 + 2 + ... + 10)² = 55² = 3025

Por lo tanto, la diferencia entre el cuadrado de la suma y la suma de los cuadrados es:
3025 − 385 = 2640

Encontrá la diferencia entre el cuadrado de la suma y la suma de los cuadrados de los primeros `n` números naturales.

👉 [Enlace al problema original](https://projecteuler.net/problem=6)


### Enfoque
La idea es calcular por separado:

- La **suma de los cuadrados**: se eleva cada número al cuadrado y luego se suman.
- El **cuadrado de la suma**: se suman los números normalmente y luego se eleva ese total al cuadrado.

Finalmente, se calcula la diferencia entre estos dos valores.

Este enfoque es claro y directo porque:

- Aprovecha **comprensiones de listas** para hacer los cálculos de forma concisa.
- Utiliza funciones integradas de Python como `sum()` y operaciones básicas.
- Es adecuado para valores de `n` moderados (hasta miles), aunque no es el más eficiente posible.

### Resultado esperado
El resultado correcto para `n = 100` es: **25164150**


### Conceptos aplicados
- Comprensiones de listas
- Funciones integradas (`sum`)
- Operaciones aritméticas (potencias y sumas)
- Pensamiento matemático
- Análisis de diferencia entre expresiones algebraicas
