#Importamos nuestro menu para poder correr nuestro programa 
from utilidades.menu_consola import Menu_consola

#Ejecuta el programa y podemos ver el orden en el que se puede trabajar 
def main():
    menu = Menu_consola()
    menu.ejecutar()
#Inicia la ejecución del archivo 
main()
