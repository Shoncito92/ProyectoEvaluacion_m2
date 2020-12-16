#Haga un programa que muestre una cantidad ingresada por el usuario en forma de abaco en pantalla:
def ingreso_y_descomp_num():
    num_a = str(input("Ingrese un numero: "))
    num_a = list(num_a)
    print(num_a)
    return num_a

def crear_tablero():
    centena_de_millar = ["   *--* ", "   |  | ", "   |  | ",
                          "   |  | ", "   |  | ", "   |  | ",
                          "   |  | ", "   +--+ "]

    decena_de_millar = ["   +--+ ", "   |  | ", "   |  | ",
                          "   |  | ", "   |  | ", "   |  | ",
                          "   |  | ", "   *--* "]

    sis_enum_decimal = ' 100.000  10.000  1.000    100      10      1'


    for x in centena_de_millar:
        print(x)
    for y in decena_de_millar:
        print(y)
    print(sis_enum_decimal)




def agregar_punto_a_num():
    pass


def llenar_tablero():

    pass


if __name__ == '__main__':
        while True:
            ingreso_y_descomp_num()
            crear_tablero()
            agregar_punto_a_num()
            llenar_tablero()

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