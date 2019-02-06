class Calculadora:
    
    creditos = []
    notas = []
    asignaturas = []
    continuar = True
    while continuar != False:
        print("Introduzca el nombre de la asignatura")
        asignaturas.append(input())
        print("Introduzca el número de créditos")
        creditos.append(int(input()))
        print("Introduzca la nota")
        notas.append(float(input()))
        print("Si no desea contrinuar pulse n, si no pulse cualquier otra tecla")
        if input() == "n":
            continuar = False
    i = 0
    acumulado = 0
    num_creditos = 0
    while i < len(asignaturas):
        print("Asignatura: "+asignaturas[i]+"\tNota: "+str(notas[i])+"\tCreditos: "+str(creditos[i]))
        acumulado += (notas[i]*creditos[i])
        num_creditos += creditos[i]
        i = i+1
    print("Media ponderada = " + str(acumulado/num_creditos))
    print("Creditos = " + str(num_creditos))
        

