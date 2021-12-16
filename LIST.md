

# Issues


 - Proyecto sin separación de capas
 - Falta de Serializadores
 - Manejo de errores
 - Snake case faltante para las propiedades del objeto
 - Falta de tests unitarios
 - Creación de variables sin sentido



## Proyecto sin separación de capas

Como ventajas de la separación por capas se encuentra el aislamiento de resposabilidades, que conllevan a un mejor mantenimiento y desarrollo.
También la escalabilidad del proyecto se ve beneficiada por la estructura.
En el caso de la app proporcionada, todo se encuentra en el mismo archivo:
esto complica la lectura, la escalabilidad, el mantenimiento y desarrollo.
Es muy probable que si la aplicación falla, será tedioso encontrar los errores, aún
si es un proyecto chico.

## Falta de Serializadores

La falta de serializadores en el ingreso de datos permite que se generen errores en la base de datos, y que uno o más errores lleven a resultados que no son predecibles si la aplicación es productiva.
Al aplicar un serializador con los campos y tipos esperados se puede recoger el error antes de que la información sea intercambiada por una o más piezas del proyecto.


## Manejo de errores

El manejo de errores permite el control esperado de futuros errores que sabemos que pueden ocasionarse. Esto ayuda tanto para identificar el tipo esperado, como para retornar una respuesta personalizada en cuanto el error ocurra.

## Snake case faltante para las propiedades del objeto

Si bien puede presentarse el caso del camelCase, para variables de javascript, la definición del nombre de propiedades, clases, métodos, son claves que se utilizarán a lo largo del proyecto. No tener denifinida una convención para la escritura y definición de ellos puede ocacionar problemas críticos productivos. Y si bien, por ej. en Python, no son obligatorios los ';', la mala definición del nombre de atributos puede ocacionar un problema crítico inrastreable, que sería peor que un ';'.

## Falta de tests unitarios

Si bien la aplicación puede funcionar sin que existan tests unitarios, estos ayudan a la salud de la aplicación. La certeza de que los casos de uso para los que la aplicación fue diseñada se sigan cumpliendo. También ayudan a reconocer que la aplicación diseñada tiene una complejidad fácil o dificil de testear.

## Creación de variables sin sentido

Si bien esta aplicación no está hecha en C, tampoco es correcto crear o reasignar variables que finalmente no tenían un tratamiento distinto al asignado. Para solucionar esto pueden agregarse linters al proyecto, y mantener la sintaxis homologada para el resto del personal del equipo.


## Definición y documentación de métodos

Si bien es probable que la explicación de algunos métodos sea innecesaria, existen algunos casos en que puede dejar una documentación mínima del método, clase, o incluso la resolución de alguna línea de código, para la claridad del equipo.
