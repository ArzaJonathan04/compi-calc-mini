# Compilador Mini-Calc

## Integrantes
- Jonathan
- Danilo
- Andrea
- Victor
- Beatriz
- Magali

Manual de uso – Compilador Mini-Calc
Este manual explica cómo obtener el proyecto compi-calc-mini desde GitHub, abrirlo en Visual Studio Code y ejecutar el compilador (lexer y parser) sobre archivos .calc.
Requisitos previos
•Una cuenta de GitHub no es necesaria: el repositorio es público.
•Git instalado (solo si se elige clonar; descargar el ZIP no lo necesita).
•Visual Studio Code.
•Python en su última versión estable. El proyecto usa Python nativo, sin librerías externas.
Paso 1. Obtener el repositorio
Hay dos formas. Con cualquiera de ellas se obtiene la misma carpeta de proyecto.
Opción A: clonar con Git
1.Abrir el repositorio en GitHub.
2.Pulsar el botón verde Code, pestaña Local, opción HTTPS, y copiar la URL con el icono de copiar.
3.Abrir una terminal en la carpeta donde se quiere guardar el proyecto y ejecutar:
git clone <URL copiada>
Opción B: descargar el ZIP
1.En el mismo menú Code, elegir Download ZIP.
2.Extraer el archivo ZIP. Se crea una carpeta como compi-calc-mini-main.
La carpeta del proyecto contiene Documentacion, src, tests y README.md.
Paso 2. Importar el proyecto a Visual Studio Code
1.Abrir Visual Studio Code.
2.Ir al menú File y elegir Open Folder… (atajo Ctrl+K Ctrl+O).
3.Seleccionar la carpeta del proyecto (compi-calc-mini o compi-calc-mini-main) y confirmar.
4.En el panel Explorer debe verse src/mini_calc.py y la carpeta tests.
Es importante abrir la carpeta raíz del proyecto y no solo el archivo mini_calc.py, porque los comandos usan rutas relativas como src/mini_calc.py y tests/valido.calc.
Paso 3. Instalar Python (última versión) y configurarlo en VS Code
1.Descargar la última versión estable desde python.org e instalarla. En Windows, marcar la casilla "Add Python to PATH" en el instalador.
2.Verificar la instalación desde la terminal:
python --version
3.En VS Code, instalar la extensión Python (de Microsoft) desde el panel de extensiones.
4.Seleccionar el intérprete: Ctrl+Shift+P, escribir Python: Select Interpreter y elegir la versión recién instalada.
Paso 4. Iniciar la terminal de Python
1.En VS Code, abrir el menú Terminal y elegir New Terminal (atajo Ctrl+Ñ o Ctrl+`).
2.Comprobar que el prompt muestra la carpeta raíz del proyecto, por ejemplo:
PS D:\compi-calc-mini-main\compi-calc-mini-main>
3.Si el comando python no se reconoce, probar con py. Si tampoco funciona, reinstalar Python marcando "Add Python to PATH" y reiniciar VS Code.
Paso 5. Ejecutar el código
El formato general es:
python src/mini_calc.py <ruta del archivo .calc>
Ejemplo con un programa válido:
python src/mini_calc.py tests/valido.calc
La ejecución muestra primero los tokens, con el formato <TIPO, "lexema", línea, columna>, y luego el resultado del análisis sintáctico:
<ID, "x", 1, 1>
<OP_ASSIGN, "=", 1, 3>
<NUM, "10", 1, 5>
...
=== INICIO DE ANÁLISIS SINTÁCTICO ===
El análisis sintáctico finalizó exitosamente sin errores.
Ejemplo con un error léxico:
python src/mini_calc.py tests/error_lexico.calc

=== INICIO DE ANÁLISIS LÉXICO ===
Error [Línea 1, Columna 10]: Carácter no válido '$'.
Cuando hay un error léxico, el análisis sintáctico no llega a iniciarse.
Archivos de prueba disponibles
La carpeta tests incluye:
•valido.calc y ejemplo.calc: programas correctos.
•err_caracter, err_expresion, err_identificador, err_operador, err_parentesis, err_punto_coma, error_lexico y error_sintactico: casos con errores.
•resultados_esperados.md: salidas esperadas para comparar.
Ejecutar un programa propio
1.Crear un archivo nuevo con extensión .calc dentro de tests, por ejemplo mi_programa.calc.
2.Escribir sentencias de Mini-Calc. Las variables son de una sola letra minúscula y cada sentencia termina en ;:
x = 10 + 5 * 2;
y = (x - 4) / 2;
print y;
3.Ejecutar:
python src/mini_calc.py tests/mi_programa.calc
Solución de problemas
Problema	Causa probable	Solución
python no se reconoce como comando	Python no está en el PATH	Reinstalar marcando "Add Python to PATH" o usar py
No se encuentra src/mini_calc.py	La terminal no está en la carpeta raíz	Abrir la carpeta raíz con File > Open Folder o usar cd hasta ella
El archivo .calc no existe	Ruta mal escrita	Revisar el nombre y la carpeta (tests/...)
Aparece un error léxico	Carácter fuera del lenguaje (mayúsculas, $, @)	Corregir en el archivo la línea y columna indicadas
