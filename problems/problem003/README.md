# Problem 003 - Largest Prime Factor

## Enunciado
El número 13195 tiene como factores primos a 5, 7, 13 y 29.
¿Cuál es el mayor factor primo del número **600851475143**?

👉 [Enlace al problema original](https://projecteuler.net/problem=3)


## Enfoque
La idea es **dividir iterativamente el número objetivo** por sus factores primos más pequeños, comenzando desde 2.
Cada vez que se encuentra un factor, se divide el número tantas veces como sea divisible, reduciendo así el problema a un número más pequeño.

Este enfoque es eficiente porque:

- Solo se itera hasta la raíz cuadrada del número.
- Se eliminan múltiples ocurrencias de un mismo factor sin repetir cálculos innecesarios.
- Se omiten los números pares mayores a 2 para optimizar el recorrido.

## Resultado esperado
El mayor factor primo de **600851475143** es: **6857**

## Conceptos aplicados
- Bucles `while`
- Condicionales (`if`)
- División entera (`//`)
- Aritmética modular (`%`)
- Optimización mediante salto de pares
- Pensamiento matemático (factores primos y raíz cuadrada)
