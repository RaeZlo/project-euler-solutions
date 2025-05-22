# Problem 010 - Summation of primes
## Enunciado
La suma de los números primos por debajo de 10 es 2 + 3 + 5 + 7 = 17.

👉 ¿Cuál es la suma de todos los números primos menores que dos millones?

🔗 [Enlace al problema original en Project Euler](https://projecteuler.net/problem=10)

## Enfoque
Para resolver el problema, se implementó una función `is_prime(n)` que verifica si un número es primo mediante divisiones hasta su raíz cuadrada. Luego, se itera desde 0 hasta el número objetivo (`num`) y se acumulan los números que son primos en una suma total.

Este enfoque es funcional y correcto, aunque no el más eficiente para números muy grandes (como 2 millones), ya que revisa uno por uno si un número es primo.

Aun así, permite practicar conceptos clave como:

- Verificación eficiente de primos (sin comprobar pares mayores a 2).
- Reutilización de funciones.
- Acumulación condicional.
- Bucles y optimización básica.

## Resultado esperado
La suma de todos los números primos menores a 10 es: `17`  
La suma de todos los números primos menores a 2,000,000 es: `142913828922`

## Conceptos aplicados
- Condicionales (`if`)
- Bucles `for`
- Funciones personalizadas (`is_prime`)
- Tipado estático con anotaciones (`int`)
- Raíz cuadrada para reducir complejidad algorítmica
- Pensamiento algorítmico (verificación eficiente de números primos)

## Posibles mejoras
- Sustituir el algoritmo actual por la **Criba de Eratóstenes**, que permite obtener todos los primos menores que `n` con mejor rendimiento (`O(n log log n)`).
