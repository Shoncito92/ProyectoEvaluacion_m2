import funciones

print("Hola, bienvenido al abaco virtualmix-3d")
print("Ingrese abajo un numero =< 6 digitos")
n = input("A q u i ! : ")
diccionario = {'unidad':"", 'decena': "", 'centena':"", 'unidad_de_mil':"", 'decena_de_mil':"", 'centena_de_mil':""}
funciones.crear_tablero()


if __name__ == '__main__':
    while False:  #Aqui hago pruebas con funciones
        funciones.ingreso_y_descomp_num(n)
        funciones.crear_tablero()




#Utilice un diccionario que almacene las unidades, decenas, centenas,
#unidades de mil, unidades de diez mil y unidades de cien mil.

#cada intento debe ser almacenado en una lista,
#tal lista debe contener todos los intentos de usuario.

#Si el usuario desea dejar de ejecutar el programa en cualquier instante,
#permitale terminar escribiendo ‘salir’.

#Previo a ‘salir’ muestre en pantalla todos los intentos de la lista, por

#ejemplo:
#841.231
# 10.231
#    123
#903.267
#   etc.

#No olvide ubicar el punto separador de miles para mostrar la cifra más
#claramente.

#Haga su código legible y facilmente ejecutable, dando las instrucciones de
#su uso.

#Separe las distintas partes en funciones propiamente nombradas y de una
#extension razonable.

#Escriba todos los comentarios que estime convenientes.

#No solo se evaluará que el programa haga lo requerido, también se
#evaluará el orden del código. Códigos poco legibles no se evaluarán
#positivamente.