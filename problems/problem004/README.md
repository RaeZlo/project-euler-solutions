# Problem 004 - Largest Palindrome Product

## Enunciado
Un número palindrómico se lee igual de izquierda a derecha que de derecha a izquierda.  
El palíndromo más grande hecho del producto de dos números de 2 cifras es:  
`9009 = 91 × 99`  
¿Cuál es el palíndromo más grande que se puede obtener del producto de dos números de 3 cifras?

👉 [Enlace al problema original](https://projecteuler.net/problem=4)

## Enfoque
La estrategia consiste en probar todos los productos posibles entre números de 3 cifras (desde 999 hasta 100) y verificar si el resultado es un número palindrómico.  
Para optimizar el recorrido:

- Se itera desde 999 hacia 100, tanto en el primer como en el segundo factor.
- Se evita recalcular combinaciones repetidas (ej. `123 × 456` y `456 × 123`).
- Se sale anticipadamente del segundo bucle si el producto actual ya no puede superar al máximo palíndromo encontrado hasta el momento.
- Se encapsula la verificación de palíndromos en una función auxiliar para mejorar la claridad y reutilización.

## Resultado esperado
El mayor palíndromo producto de dos números de 3 cifras es:  
**906609 = 913 × 993**

## Conceptos aplicados
- Conversión de enteros a cadenas
- Reversión de strings (`s[::-1]`)
- Comparación y actualización de valores máximos
- Estructura de bucles `for` anidados
- Optimización por corte anticipado (`break`)
- Encapsulamiento en funciones reutilizables
- Tipado y documentación con `docstrings`
