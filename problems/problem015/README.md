# Problem 015 - Lattice Paths
## Enunciado
Partiendo desde la esquina superior izquierda de una cuadrícula de `20 x 20`, ¿cuántos caminos diferentes existen hasta la esquina inferior derecha, si solo se puede mover hacia **abajo** o hacia la **derecha**?

👉 [Enlace al problema original](https://projecteuler.net/problem=15)

## Enfoque
Este problema se puede modelar como un cálculo del **coeficiente binomial**. En una cuadrícula de `n x n`, el número total de movimientos necesarios es `2n` (n hacia la derecha y n hacia abajo). El problema se reduce a encontrar de cuántas maneras se pueden elegir `n` movimientos hacia la derecha (o hacia abajo) entre los `2n` totales:

$$
\text{Caminos posibles} = \binom{2n}{n} = \frac{(2n)!}{n! \cdot n!}
$$

Para calcular este valor eficientemente, se implementó una función que calcula el coeficiente binomial de forma iterativa, sin necesidad de calcular los factoriales completos, lo que mejora tanto la **eficiencia** como la **precisión**.

Este enfoque es eficiente porque:

* Utiliza una fórmula matemática directa sin recorrer todos los caminos posibles.
* Evita overflow o grandes operaciones de factorial innecesarias.
* Usa aritmética iterativa para optimizar memoria y velocidad.

## Resultado esperado
El número de caminos posibles en una cuadrícula de `20 x 20` es: **137846528820**

### Conceptos aplicados
* Bucles `for` para multiplicaciones controladas.
* Condicionales para verificar rangos válidos de `k`.
* División entera (`//`) para evitar valores decimales.
* Principios matemáticos (combinatoria y coeficientes binomiales).
* Tipado estático (`type hints`) y buenas prácticas de codificación.
* Validación básica de entrada.

##  Aprendizaje personal
Gracias a este ejercicio entendí cómo aplicar el concepto de **coeficiente binomial** para resolver problemas combinatorios de forma eficiente. También reforcé la importancia de escribir código claro y optimizado sin necesidad de usar bibliotecas externas, y cómo transformar una situación de la vida real (como recorrer una cuadrícula) en un problema puramente matemático.
