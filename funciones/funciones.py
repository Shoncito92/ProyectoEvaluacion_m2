def ingreso_y_descomp_num(n):

    #n = int                  #Aqui el numero ingresado se le asigna num_a y entra en formato INT

    print("sus digitos son: ", n)     #me muestra los digitos que ya ingrese
    n = int(n)
    if n >= 1000000:                  #si el numero ingresado supera las 6 cifras (999999) entra en un if
        print("has superado el limite de 6 digitos, intentalo otra vez. :(")
        exit()
    else:                                 #si el if no se cumple debe transformar num_a a STR
        s = str(n)
        # print("aqui se convirtio a string:",  type(str_num_a))
        print(list(s))            #En la linea oculta 13 comprueba que la variable num_a la transforme a
                                          #string en una nueva variable llamada STR_NUM_A
        return s







def crear_tablero():
    tablero = ["   *-+-* ",  #HEAD
                "   | 0 | ", #nivel 8
                "   | 0 | ", #nivel 7
                "   | 0 | ", #nivel 6
                "   | 0 | ", #nivel 5
                "   | 0 | ", #nivel 4
                "   | 0 | ", #nivel 3
                "   | 0 | ", #nivel 2
                "   | 0 | ", #nivel 1
                "   +-*-+ "] #FOOT

    sis_enum_decimal = '-|100.000|-|10.000|-|1.000|---|100|-----|10|-----|1|'
    for x in tablero:
        print(x * 6)
    print(sis_enum_decimal)


def agregar_punto_a_num():
    pass

def llenar_tablero():
    pass