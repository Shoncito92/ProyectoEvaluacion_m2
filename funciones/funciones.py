def ingreso_y_descomp_num():
    num_a = str(input())
    num_a = list(num_a)
    print(num_a)
    return num_a

def crear_tablero():
    tablero = ["   *--* ", "   |  | ", "   |  | ",
                          "   |  | ", "   |  | ", "   |  | ",
                          "   |  | ", "   +--+ "]

    sis_enum_decimal = ' 100.000  10.000  1.000    100      10      1'
    for x in tablero:
        print(x * 6)
    print(sis_enum_decimal)


def agregar_punto_a_num():
    pass

def llenar_tablero():
    pass