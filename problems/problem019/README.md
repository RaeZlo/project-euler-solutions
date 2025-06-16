# Problem 019 - Counting Sundays
## Enunciado
Se nos informa que:

* El 1 de enero de 1900 fue un lunes.
* Abril, junio, septiembre y noviembre tienen 30 días.
* Todos los demás tienen 31, excepto febrero, que tiene 28 (29 en años bisiestos).
* Un año es bisiesto si es divisible por 4, excepto los múltiplos de 100 que **no** lo son, **salvo** que también sean divisibles por 400.

**¿Cuántos domingos cayeron en el primer día del mes durante el siglo XX (del 1 de enero de 1901 al 31 de diciembre del 2000)?**

👉 [Enlace al problema original](https://projecteuler.net/problem=19)

## Enfoque
La idea principal es simular manualmente el avance del calendario desde el 1 de enero de 1901 hasta el 31 de diciembre de 2000, manteniendo un contador para el **día de la semana del primer día de cada mes**.
Cada vez que ese día sea un **domingo**, se incrementa un contador.

Este enfoque es eficiente porque:

* No se utilizan librerías externas como `datetime`, lo cual entrena el pensamiento lógico y matemático.
* Se calcula el número de días de cada mes teniendo en cuenta si el año es bisiesto.
* Se actualiza el día de la semana de forma acumulativa y modular (ciclo de 7 días).

## Resultado esperado
La cantidad de domingos que cayeron en el primer día del mes entre 1901 y 2000 es: **171**

## Conceptos aplicados
* Lógica de años bisiestos
* Simulación de calendario
* Operador módulo `%` para rotación de días de la semana
* Bucles anidados (`for`)
* Contadores (`+=`)
* Representación numérica de días de la semana (0 = lunes, 6 = domingo)
