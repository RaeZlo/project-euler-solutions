# **Problem 027 - Quadratic Primes**
## **Enunciado**
Se descubrió que la expresión cuadrática:

    *n² + an + b*,
donde |a| < 1000 y |b| ≤ 1000, produce una gran cantidad de números primos para valores consecutivos de *n*, comenzando con *n = 0*.
Por ejemplo, *n² + n + 41* produce 40 números primos para los valores *n = 0* hasta *39*. Sin embargo, al usar *n = 40*, el resultado ya no es primo.

¿Encuentra los coeficientes *a* y *b* para la expresión cuadrática que produce la mayor cantidad de números primos consecutivos empezando desde *n = 0*? ¿Cuál es el producto *a · b*?

👉 [Enlace al problema original](https://projecteuler.net/problem=27)

## **Enfoque**
La idea principal es probar todas las combinaciones posibles de coeficientes *a* y *b* dentro de los rangos permitidos, y contar cuántos primos consecutivos genera la fórmula cuadrática *n² + a·n + b* comenzando desde *n = 0*.

Se usa una función `is_prime()` para verificar si un número es primo, utilizando el método clásico hasta la raíz cuadrada.
Durante el recorrido:

* Se evalúa la fórmula en un bucle `while` mientras el resultado siga siendo primo.
* Se guarda el producto *a · b* solo si la secuencia de primos consecutivos generados es mayor a la máxima previamente encontrada.

Este enfoque funciona bien gracias a que:

* La verificación de primalidad es eficiente para los valores del problema.
* Se recorren sistemáticamente los coeficientes en el rango definido.
* La condición `while` permite evitar cálculos innecesarios si ya no se generan primos.

## **Resultado esperado**
El producto correcto de los coeficientes *a* y *b* que generan la mayor cantidad de números primos consecutivos es: **31875000**

## **Conceptos aplicados**
* Álgebra y propiedades de expresiones cuadráticas.
* Verificación de números primos con raíz cuadrada.
* Búsqueda exhaustiva con condiciones de corte.
* Tipado estático y funciones bien definidas.
* Buenas prácticas:

  * Separación de funciones (`is_prime` y `find_quadratic_coefficients_with_max_primes`)
  * Uso de variables descriptivas.
  * Código autocontenible y legible.
