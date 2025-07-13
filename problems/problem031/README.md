# Problem 031 - Coin Sums
## Enunciado
En Inglaterra, la moneda se compone de libras (£) y peniques (p). Existen ocho monedas en circulación:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) y £2 (200p)

Se desea conocer **de cuántas formas distintas se puede hacer £2** usando cualquier cantidad de monedas.

👉 [Enlace al problema original](https://projecteuler.net/problem=31)

## Enfoque
El problema se resuelve usando **programación dinámica**, almacenando en una lista la cantidad de formas de formar cada valor entre 0 y el objetivo (`target`).

La idea es que, para cada moneda, se actualizan todas las combinaciones posibles que se pueden formar sumando esa moneda a las combinaciones previas.
Esto permite reutilizar los resultados parciales para formar valores mayores de manera eficiente.

El código incluye mejoras en claridad y robustez:

* Validación para evitar que el objetivo sea negativo.
* Eliminación de monedas duplicadas y ordenamiento para consistencia.
* Estructura modular que puede reutilizarse con diferentes objetivos y conjuntos de monedas.

## Resultado esperado
El número de formas de formar £2 (200p) con las monedas británicas es: **73682**

## Conceptos aplicados
* Programación dinámica (bottom-up)
* Inicialización de una tabla de soluciones (`ways`)
* Iteración optimizada por monedas y objetivos
* Eliminación de duplicados en listas (`set`)
* Validación de argumentos (`ValueError`)
* Estructura de bucles anidados
* Buenas prácticas de codificación con tipado, validación y modularidad
