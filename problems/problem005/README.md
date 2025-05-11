## Problem 005 - Smallest Multiple

### Enunciado
2520 es el número más pequeño que puede dividirse exactamente por todos los números del 1 al 10.
¿Cuál es el número positivo más pequeño que es divisible por todos los números del 1 al 20?

👉 [Enlace al problema original](https://projecteuler.net/problem=5)

### Enfoque
La idea es encontrar el **mínimo común múltiplo (MCM)** entre todos los números del 1 al 20.
Para hacerlo de forma eficiente, se usa el hecho matemático de que:

```
mcm(a, b) = abs(a * b) // mcd(a, b)
```

Donde `mcd` es el máximo común divisor.
Aplicando esta fórmula de forma acumulativa usando `reduce()`, se obtiene el menor múltiplo común de todo el rango sin necesidad de comprobar divisores uno por uno.

Este enfoque es eficiente porque:

* Se evita la verificación manual de divisibilidad.
* Se usa el algoritmo de Euclides (`gcd`) para calcular el MCD de forma óptima.
* `reduce()` permite aplicar el MCM de forma sucesiva a toda la serie.

### Resultado esperado
El resultado correcto para el rango del 1 al 20 es: `232792560`

### Conceptos aplicados
* Funciones matemáticas (`gcd`, `abs`)
* Programación funcional (`reduce`)
* Operadores aritméticos
* Tipado estático
* Buenas prácticas: separación de lógica, validación de entradas, documentación
* Pensamiento algorítmico aplicado a matemáticas
