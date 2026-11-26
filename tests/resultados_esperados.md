# Resultados esperados de las pruebas

Convención: línea y columna desde 1. Un tab cuenta como 1 columna.

| Archivo | Resultado esperado |
|---|---|
| `valido.calc` | Tokens correctos (línea 1: x=col 1, `=` col 3, 10 col 5, `+` col 8, 5 col 10, `*` col 12, 2 col 14, `;` col 15) y "El análisis sintáctico finalizó exitosamente sin errores." |
| `valido_extra.calc` | Análisis exitoso (espacios antes de `;`, línea en blanco, tab al inicio de la línea 5, paréntesis anidados) |
| `err_caracter.calc` | `Error [Línea 1, Columna 7]: Carácter no válido '$'` |
| `err_punto_coma.calc` | `Error [Línea 2, Columna 1]: Se esperaba ';' pero se encontró 'print'` |
| `err_parentesis.calc` | `Error [Línea 1, Columna 15]: Se esperaba ')' pero se encontró ';'` |
| `err_identificador.calc` | `Error [Línea 1, Columna 1]: Identificador no válido 'abc': solo se permite una letra` |
| `err_expresion.calc` | `Error [Línea 1, Columna 5]: Se esperaba una expresión pero se encontró ';'` |
| `err_operador.calc` | `Error [Línea 1, Columna 9]: Se esperaba una expresión pero se encontró '*'` |

En todos los casos de error, el programa se detiene y NO imprime "finalizó exitosamente".
