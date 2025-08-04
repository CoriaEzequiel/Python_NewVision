'''

Es importante tener un buen manejo de errores para encontrar la solución.
Podemos anticipar errores causados por entrada de datos inválidos o inconsistencias predecibles.

-Errores sintácticos: SyntaxError, invalid syntax.
-Errores en tiempo de ejecución: Runtime Error.
-Errores semánticos.

Gestión de Excepciones: try / except
try: se coloca el código que espero que puede lanzar algún error.
except: se maneja el error, si ocurre un error dentro del bloque try, se deja de ejecutar el try 
        y se ejecuta lo que haya definido en el except


Excepciones:
Si una declaración o expresión es sintácticamente correcta
igual puede generar un error cuando se intente ejecutar.
 Los errores detectados durante la ejecución se llaman excepciones y no son incondicionalmente fatales.

 ZeroDivisionError.
 (valor asociado: cadena que indica tipo de operandos y la operación)
 "10 * (1/0)"
 "ZeroDivisionError:  division by zero"

 NameError: se genera cuando no se encuentra un nombre local o global. 
 (valor asociado: mensaje de error que incluye nombre que no se pudo encontrar)  
 "4+ spam*3"
 "NameError: name 'spam' is not defined."

 TypeError: se genera cuando una operación o función se aplica a un objeto de tipo inapropiado.  
 (valor asociado: cadena que proporciona detalles sobre la falta de coincidencia de tipos) 
 "'2' + 2 "
 "Type Error: can only concatenate str (not "init") to str"

  
  
'''

