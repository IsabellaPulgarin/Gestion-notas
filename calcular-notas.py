print("--------------------Bienvenido--------------------\n ")
#Menu con varios casos
while True :
    print("1.Verificar si aprobaste o reprobaste\n2.Calcula tu promedio\n3.Crear una lista de calificaciones\n4.Verifica tus calificaciones si son mayores a:\n5.Verifica si tu calificacion esta en la lista\n6.Salir de sistema")
    op=int(input())
    match op:
        #Caso1 verificar si aprueba o no con la nota que ingreso
        case 1:
            print("Ingresa una calificacion que quieres verificar de (0 a 100)")
            calificaion=float(input())
            if 0<=calificaion<=100:
                if calificaion>=60:
                    print("\n Aprobaste")
                else:
                    print("\n Reprobaste")
            else:
                print("\n Calificacion no valida") 
        case 2 :
            #Caso2 crear una lista con notas que ingreso el usuario y calcular un promedio
            while True:
                print("Digita tus notas separadas por comas(,)\nEjemplo: 40,30.2,50.5")
                notas=input()
                notas1=notas.split(",")
                prom=0.0
                lista1=[]
                
                try:
                    #Capturar un error en la lista que ingreso el usuario
                    for nota in notas1:
                        nota=float(nota)
                        if 0 <= nota <= 100:
                            lista1.append(nota)
                            prom += nota
                        else:
                            raise#Tirar el error
                    
                    prom = prom / len(lista1)
                    print(f"promedio: {prom}")
                    break
                except:
                    print("Nota no valida")
        case 3:
            #Caso3 crear un lista para interactuar con ella en las otras 2 opciones
            print("Ingresa varias calificaciones separadas por comas para crear la lista ")
            lista=input()
            lista=lista.split(",")
            print(lista)
        case 4:
            #Caso4 para validar si hay un numero mayor  que el usuario ingresa en la lista anterior 
            if "lista" in globals():
                print("Digita un numero ")
                num = float(input())
                def numayores():
                    num_mayores = []
                    for i in lista:
                        if float(i) > num:
                            found = False
                            for numayor in num_mayores:
                                if int(float(i)) == numayor[0]:
                                    numayor[1] += 1
                                    found = True
                                    break
                            if not found:
                                num_mayores.append([int(float(i)), 1])
                    for item in num_mayores:
                        print(f"La calificacion: {item[0]} es mayor, {item[1]} veces")
                    if not num_mayores:
                        print("No hay calificaciones mayores al numero ingresado")
                numayores()
            else:
                print("Debes ingresar la lista de calificaciones primero, en la opcion 3\n ")
            
        case 5:
            #Caso5 para validar si la calificacion ingresada esta en la lista anterior del caso3
            if "lista" in globals():
                print("Digita la calificacion que quieres verificar si esta en la lista")
                num2=float(input())
                for i in lista:
                    if num2 == float(i):
                        print(i)
                    else: print("No esta en la lista")
                    
            else:
                print("Debes ingresar la lista de calificaciones primero, en la opcion 3")
        case 6 :
            #Caso6 para salir del bucle
            break
        case _:
            #Para que el usuario solo ingrese el numero de opcion que existe 
            print("Funcion no valida")