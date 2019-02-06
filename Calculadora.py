def modificarRegistro(creditos, notas, asignaturas):
    print("Introduzca el nombre de la asignatura")
    asignaturas.append(input())
    print("Introduzca el número de créditos")
    creditos.append(int(input()))
    print("Introduzca la nota")
    notas.append(float(input()))

def añadirRegistro(creditos, notas, asignaturas):
    print("Introduzca el nombre de la asignatura")
    asignaturas.append(input())
    print("Introduzca el número de créditos")
    creditos.append(int(input()))
    print("Introduzca la nota")
    notas.append(float(input()))
    print("Si no desea contrinuar pulse n, si no pulse cualquier otra tecla")
    if input() == "n":
        return False
    else:
        return True

def imprimirResultado(creditos, notas, asignaturas):
    i = 0
    acumulado = 0
    num_creditos = 0
    print("Estos son los valores introducidos: ")
    while i < len(asignaturas):
        print("Asignatura: " + asignaturas[i] + "\tNota: " + str(notas[i]) + "\tCreditos: " + str(creditos[i]) + "\tRegistro: " + str(i))
        acumulado += (notas[i] * creditos[i])
        num_creditos += creditos[i]
        i = i + 1
    print("Media ponderada = " + str(acumulado / num_creditos))
    print("Creditos = " + str(num_creditos))

def borrarRegistro(creditos, notas, asignaturas, registro):
    asignaturas.pop(registro)
    creditos.pop(registro)
    notas.pop(registro)


creditos = []
notas = []
asignaturas = []
continuar = True
fin = False
print("Si se equivoca al introducir un registro continue hasta el final, cuando termine podrá modificarlo")
while continuar:
    continuar = añadirRegistro(creditos, notas, asignaturas)
imprimirResultado(creditos, notas, asignaturas)
while fin != True:
    print("Si desea modificar algún registro pulse m , si desea insertar alguno nuevo pulse i, si desea ver los registros guardados pulse v, si desea eliminar alguno pulse d, si no pulse otra tecla")
    opcion = input()
    if opcion == "i":
        continuar = True
        while continuar:
            continuar = añadirRegistro(creditos, notas, asignaturas)
    elif opcion == "m":
        print("Indique el número de registro que desea modificar")
        registro = int(input())
        print("Introduzca el nombre de la asignatura")
        asignaturas[registro] = input()
        print("Introduzca el número de créditos")
        creditos[registro] = int(input())
        print("Introduzca la nota")
        notas[registro] = float(input())
    elif opcion == "v":
        imprimirResultado(creditos, notas, asignaturas)
    elif opcion == "d":
        print("Indique el número de registro que desea eliminar")
        registro = int(input())
        borrarRegistro(creditos, notas, asignaturas, registro)
    else:
        imprimirResultado(creditos, notas, asignaturas)
        fin = True




        

