# Problem 002 - Even Fibonacci Numbers

## Enunciado  
Cada nuevo término de la secuencia de Fibonacci se genera sumando los dos anteriores.  
Los primeros términos son: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...  
Al considerar los términos de esta secuencia cuyos valores no exceden los cuatro millones,  
encontrá la suma de los términos que sean números pares.

👉 [Enlace al problema original](https://projecteuler.net/problem=2)

## Enfoque  
La idea es recorrer la secuencia de Fibonacci mientras los valores no superen el límite dado.  
A medida que se generan los términos, se va sumando solo aquellos que sean pares (`% 2 == 0`).

Este enfoque es eficiente porque:
- Solo se genera lo necesario (no se guarda toda la secuencia en memoria).
- Se evita cualquier lógica innecesaria de filtrado posterior.

## Resultado esperado  
El resultado correcto para el límite de 4.000.000 es: **4613732**

## Conceptos aplicados  
- Bucles `while`  
- Condicionales (`if`)  
- Aritmética modular  
- Pensamiento lógico  
- Eficiencia en generación de secuencias
