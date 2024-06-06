from Lexico import Lexicon
from Sintactico import Sintax

file = "Codigos/Calificacion.txt"  #La ruta se tiene que cambiar para probar el primero es el nombre de la carpeta
                                  #Errores y el segundo es el .txt que se desea probar, ejemplo: Codigos/Primos.txt
lexico = Lexicon(file, print_result=True)
if not lexico.error_found:
    print("Análisis léxico completado exitosamente")
    sintaxis = Sintax(lexico.head, print_result=True)
    if not sintaxis.error_found:
        print("Análisis Sintactico completado exitosamente")
