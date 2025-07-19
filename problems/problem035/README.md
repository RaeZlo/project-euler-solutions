# Problem 035 - Circular Primes
## Enunciado
El número 197 es un número primo notable, ya que todas sus rotaciones (197, 971 y 719) también son números primos.

Se dice que 197 es un **primo circular**.

¿Cuántos primos circulares hay por debajo de un millón?

👉 [Enlace al problema original](https://projecteuler.net/problem=35)

## Enfoque
Este problema se resuelve en varios pasos:

1. **Generación de primos:**
   Se utiliza una función `is_prime` para identificar los números primos menores que un límite (`limit`), generando así una lista inicial de primos mediante comprensión de listas.

2. **Generación de rotaciones:**
   Para cada número, se generan todas las rotaciones posibles de sus dígitos con la función `get_rotations`. Por ejemplo, 197 produce `[197, 971, 719]`.

3. **Verificación de circularidad:**
   Un número se considera circular si **todas sus rotaciones también están en la lista de primos**.

4. **Conteo de resultados:**
   Se recorre cada primo y, si cumple la condición de circularidad, se incrementa el contador.

Este enfoque es eficiente para el problema propuesto porque:

* Se convierte la lista de primos en un conjunto para acelerar las búsquedas (`O(1)` promedio por búsqueda).
* Evita revalidar números compuestos o rotaciones que ya no están en la lista.
* Aprovecha el hecho de que si una rotación no es prima, se puede descartar todo el grupo inmediatamente.

## Resultado esperado
El número de primos circulares por debajo de un millón es: **55**

## Conceptos aplicados
* Funciones puras (`is_prime`, `get_rotations`) para mejorar la modularidad.
* Optimización con estructuras eficientes (`set` para búsquedas rápidas).
* Manipulación de cadenas y enteros para generar rotaciones.
* Tipado estático (`->`) para mayor claridad y mantenibilidad del código.
* Separación clara de responsabilidades: detección de primos, generación de rotaciones, verificación de circularidad y conteo.
* Buenas prácticas como el uso de funciones pequeñas, expresivas y testeables.
