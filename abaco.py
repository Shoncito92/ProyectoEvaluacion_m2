

espacio = "   "
lista_numeros = []
v1 = []
v2 = []
v3 = []
v4 = []
v5 = []
v6 = []
diccionario = {'unidad':"", 'decena': "", 'centena':"", 'unidad_de_mil':"", 'decena_de_mil':"", 'centena_de_mil':""}
salir = 0

for i in range(10):
    v1.append("|  |")
for i in range(10):
    v2.append("|  |")
for i in range(10):
    v3.append("|  |")
for i in range(10):
    v4.append("|  |")
for i in range(10):
    v5.append("|  |")
for i in range(10):
    v6.append("|  |")

def consultar_numero():
    global numero_ingresado
    global salir
    numero_ingresado = input("Ingrese un numero: ")
    lista_numeros.append(numero_ingresado)
    if numero_ingresado == "salir":
        salir = 1
    return salir 

def descoponer_numero():
    global unidad
    global decena
    global centena
    global unidad_de_mil
    global decena_de_mil
    global centena_de_mil
    
    if   int(numero_ingresado) > 0 :
        diccionario['unidad'] = numero_ingresado[-1]
    else :
        print("El numero ingresado no es válido.")
        diccionario['unidad'] = 0

    if   int(numero_ingresado) >= 10 :
        diccionario['decena'] = numero_ingresado[-2]
    else :
        diccionario['decena'] = 0
    if   int(numero_ingresado) >= 100 :
        diccionario['centena'] = numero_ingresado[-3]  
    else :
         diccionario['centena'] = 0
    if   int(numero_ingresado) >= 1000 :
        diccionario['unidad_de_mil'] = numero_ingresado[-4]
    else :
        diccionario['unidad_de_mil'] = 0
    if   int(numero_ingresado) >= 10000 :
        diccionario['decena_de_mil'] = numero_ingresado[-5]
    else :
        diccionario['decena_de_mil'] = 0
    if   int(numero_ingresado) >= 100000 :
        diccionario['centena_de_mil'] = numero_ingresado[-6]
    else :
        diccionario['centena_de_mil'] = 0



def rellenar_abaco():
    
    #reinicia valores del abaco
    for i in range (10):
        v1[i] = "|  |"
    for i in range (10):
        v2[i] = "|  |"
    for i in range (10):
        v3[i] = "|  |"
    for i in range (10):
        v4[i] = "|  |"
    for i in range (10):
        v5[i] = "|  |"
    for i in range (10):
        v6[i] = "|  |"
    
    #rellena valores del abaco
    for i in range (int(diccionario['unidad'])+1):
        v1[i] = "XXXX"
    for i in range (int(diccionario['decena'])+1):
        v2[i] = "XXXX"
    for i in range (int(diccionario['centena'])+1):
        v3[i] = "XXXX"
    for i in range (int(diccionario['unidad_de_mil'])+1):
        v4[i] = "XXXX"
    for i in range (int(diccionario['decena_de_mil'])+1):
        v5[i] = "XXXX"
    for i in range (int(diccionario['centena_de_mil'])+1):
        v6[i] = "XXXX"
    abaco = ("\n" + espacio + v6[9] + espacio + v5[9] + espacio + v4[9] + espacio + v3[9] + espacio + v2[9] + espacio + v1[9] + "\n" +
    espacio + v6[8] + espacio + v5[8] + espacio + v4[8] + espacio + v3[8] + espacio + v2[8] + espacio + v1[8] + "\n" +
    espacio + v6[7] + espacio + v5[7] + espacio + v4[7] + espacio + v3[7] + espacio + v2[7] + espacio + v1[7] + "\n" +
    espacio + v6[6] + espacio + v5[6] + espacio + v4[6] + espacio + v3[6] + espacio + v2[6] + espacio + v1[6] + "\n" +
    espacio + v6[5] + espacio + v5[5] + espacio + v4[5] + espacio + v3[5] + espacio + v2[5] + espacio + v1[5] + "\n" +
    espacio + v6[4] + espacio + v5[4] + espacio + v4[4] + espacio + v3[4] + espacio + v2[4] + espacio + v1[4] + "\n" +
    espacio + v6[3] + espacio + v5[3] + espacio + v4[3] + espacio + v3[3] + espacio + v2[3] + espacio + v1[3] + "\n" +
    espacio + v6[2] + espacio + v5[2] + espacio + v4[2] + espacio + v3[2] + espacio + v2[2] + espacio + v1[2] + "\n" +
    espacio + v6[1] + espacio + v5[1] + espacio + v4[1] + espacio + v3[1] + espacio + v2[1] + espacio + v1[1] + "\n" + 
    " ___________________________________________ " + "\n" + "|___________________________________________|" + "\n" +
    "100.000  10.000  1.000   100    10      1")
    print(abaco)

def numeros_ingresados():
    lista_numeros.remove("salir")
    print("Los numeros ingrsados son:")
    for i in range (0,len(lista_numeros)):
        print(f'{int(lista_numeros[i]):,.0f}')
    

while True:
    consultar_numero()
    if salir == 1:
        break
    descoponer_numero()
    rellenar_abaco()
numeros_ingresados()