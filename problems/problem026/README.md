# Problem 026 - Recurring Cycles
## Enunciado
Una fracción decimal periódica es una fracción en la que un conjunto de dígitos se repite infinitamente.

Por ejemplo:

* 1/3 = 0.(3)
* 1/7 = 0.(142857)

Se puede ver que 1/7 tiene un ciclo de repetición de 6 dígitos.
Se pide encontrar, para todos los `d < 1000`, el valor de `d` tal que 1/d tenga el ciclo repetitivo más largo en su parte decimal.

👉 [Enlace al problema original](https://projecteuler.net/problem=26)

## Enfoque
La estrategia se basa en simular la división larga de `1 / d` y rastrear los restos (residuos) que van apareciendo. La clave es notar que:

* Cuando un resto se repite, el ciclo decimal también lo hace.
* Si el resto llega a cero, la división es exacta y no hay ciclo.

Por lo tanto, guardamos en un diccionario la posición de cada resto en el proceso.
Si volvemos a ver un resto ya registrado, podemos calcular la longitud del ciclo como la diferencia de posiciones.

Para encontrar qué denominador genera el ciclo más largo:

* Iteramos desde 2 hasta el límite (1000).
* Calculamos la longitud del ciclo para cada `d`.
* Guardamos el `d` que produzca el ciclo más largo.

## Resultado esperado
El valor correcto de `d` menor que 1000 con el ciclo más largo en 1/d es: **983**

## Conceptos aplicados
* Simulación de división larga
* Diccionarios para rastrear estado
* Pensamiento algorítmico basado en matemáticas
* Bucles y control de flujo
* Separación de lógica en funciones
