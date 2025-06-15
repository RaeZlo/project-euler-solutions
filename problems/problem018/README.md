# Problem 018 - Maximum Path Sum I
## Enunciado
Partiendo desde la cima del siguiente triángulo y moviéndose hacia abajo solo a números adyacentes, encuentre el total máximo desde la cima hasta la base:

```
      3
     7 4
    2 4 6
   8 5 9 3
```

En este ejemplo, el camino 3 → 7 → 4 → 9 da un total de 23.
👉 [Enlace al problema original](https://projecteuler.net/problem=18)

El triángulo real utilizado en el problema es mucho más grande, por lo que una solución por fuerza bruta no es viable.

## Enfoque
La estrategia se basa en programación dinámica, recorriendo el triángulo desde abajo hacia arriba (en lugar de arriba hacia abajo), acumulando los máximos parciales:

* Se parte de la **penúltima fila**, sumando a cada número el **máximo de los dos posibles descendientes directos** de la fila inferior.
* De esta forma, cada número se transforma en el **máximo total alcanzable** desde ese punto hasta la base.
* El proceso se repite fila por fila hacia arriba, hasta llegar a la cima, donde estará el resultado final.

Este enfoque es eficiente porque:
* **Evita la exploración de todos los caminos posibles** (que serían exponenciales).
* Cada número se procesa **una sola vez**.
* Se aprovecha la **estructura del problema** para acumular resultados de forma ascendente.

## Resultado esperado
Para el triángulo original del problema, el total máximo desde la cima hasta la base es: **1074**

## Conceptos aplicados
* Programación dinámica (bottom-up)
* Iteración inversa con `reversed()` o índices descendentes
* Manipulación de listas anidadas
* Operaciones matemáticas básicas (`max`, `+`)
* Principios de optimización por subproblemas
