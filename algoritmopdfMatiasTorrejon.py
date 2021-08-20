import random
import numpy as np
from random import sample
import sys

#tabla 1
i = 6#numero de individuos
j = 5#numero de tamanio binario
x = np.array([[1, 4, 5, 12,8],
    [-5, 8, 9, 0,9],
    [-6, 7, 11, 19,8],
    [1, 4, 5, 12,7],
    [-5, 8, 9, 0,6],
    [-6, 7, 11, 19,4]])

xdec=[ ]
xdec2=[ ]
azar=[ ]
#pareja= sample([x for x in range(0,6)],6)
#while
option = 1
valido = 0
iteracion = 0
while valido == 0:
    optionVal = 0
    valido = 1
    while optionVal == 0:
        option    = input("Desea continuar con la implementación del AG: 1.Si. 2.No ")
        option = int(option)
        optionVal = 1
        if option < 1 or option > 2:
            print("Escoga una opción correcta por favor.")
            optionVal = 0
        
        print (option)
    if option == 2:
        sys.exit()
    azar=list(range(6))
    random.shuffle(azar)
    print(azar)
    uno= [ ]
    dos= [ ]
    m = 5
    for n in range(3):
   
        uno.append(azar[n])
        dos.append(azar[m])
        m = m-1

    
    for n in range(i): #Genera el arreglo en binario
        position=4
        resultdec=0
        for m in range(j):
            if (iteracion == 0):
                x[n][m] = random.randrange(2)
            #print("", x[n][m]) 
            resultdec=x[n][m]*2**position + resultdec
            #print("resultdec,position",resultdec,position)
            position = position-1
        xdec.append(resultdec)
        xdec2.append(resultdec**2)


    print ("Tabla1. Selección\n",x)    # (2)x 
    print ("X decimal",xdec) # (3)x en decimal
    print ("F(x)",xdec2)# (4) f(x)
    print("parejas(el primero con el primero ...)",uno,dos)# (5)pareja aleatoria
    #Para comprobar
    #z= int('11000', 2)
    #print(z)
    winnerTorneo = []
    individuoWin = []
    individuoLoser = []
    for n in range(3): 
        #print("kafjasjkfjk")
        winnerTorneo.append(max(xdec[uno[n]] , xdec[dos[n]]))
    
        if winnerTorneo[n] == xdec[uno[n]]:
            #print("gano el de lista uno")
            individuoWin.append(uno[n])
            individuoLoser.append(dos[n])
        else:
            #print("gano el de lista dos")
            individuoWin.append(dos[n])
            individuoLoser.append(uno[n])
    #print (winnerTorneo)    
    print ("Individuos que fueron seleccionados",individuoWin)
    print ("Individuos perdedores a olvidar",individuoLoser)       
    #tabla2.Cruce
    tablaWin = np.array([[1, 4, 5, 12,8],
        [-5, 8, 9, 0,9],
        [-6, 7, 11, 19,8],
        [1, 4, 5, 12,7],
        [-5, 8, 9, 0,6],
        [-6, 7, 11, 19,4]])
    position = 0
    for n in range(i): #Genera el arreglo en binario
        if n == 2:
            position = 1

        if n == 4:
            position = 2
        #print (n)
        for m in range(j):
            tablaWin[n][m] = x[individuoWin[position]][m] 
         
    x= tablaWin
    print ("tabla2.Cruce:\n",tablaWin)
    #print (x)
    padre = []
    madre = []
    m = 5
    for n in range(3):
   
        padre.append(azar[n])
        madre.append(azar[m])
        m = m-1
    numeroCruce = []
    for n in range(3):
        numeroCruce.append(random.randrange(1,5)) #generar numero aleatorio entre 1 y 4
    print("numero aleatorio cruce",numeroCruce) 
    listaHijos = [ ]

    #print(x)
    hijoPadre = np.array([[1, 4, 5, 12,8],
        [-5, 8, 9, 0,9],
        [-6, 7, 11, 19,8]])
    hijoMadre = np.array([[1, 4, 5, 12,8],
        [-5, 8, 9, 0,9],
        [-6, 7, 11, 19,8]])
    print("parejas(el primero con el primero ...)",padre,madre)# (5)pareja aleatoria

    positionF = 0 
    for n in range(3):
    
        if numeroCruce[n] == 1:
            hijoPadre[n][0]= x[padre[n]][0]
            hijoPadre[n][1]= x[madre[n]][1]
            hijoPadre[n][2]= x[madre[n]][2]
            hijoPadre[n][3]= x[madre[n]][3]
            hijoPadre[n][4]= x[madre[n]][4]

            hijoMadre[n][0]= x[madre[n]][0]
            hijoMadre[n][1]= x[padre[n]][1]
            hijoMadre[n][2]= x[padre[n]][2]
            hijoMadre[n][3]= x[padre[n]][3]
            hijoMadre[n][4]= x[padre[n]][4]
    
        if numeroCruce[n] == 2:
            hijoPadre[n][0]= x[padre[n]][0]
            hijoPadre[n][1]= x[padre[n]][1]
            hijoPadre[n][2]= x[madre[n]][2]
            hijoPadre[n][3]= x[madre[n]][3]
            hijoPadre[n][4]= x[madre[n]][4]

            hijoMadre[n][0]= x[madre[n]][0]
            hijoMadre[n][1]= x[madre[n]][1]
            hijoMadre[n][2]= x[padre[n]][2]
            hijoMadre[n][3]= x[padre[n]][3]
            hijoMadre[n][4]= x[padre[n]][4]
        if numeroCruce[n] == 3:
            hijoPadre[n][0]= x[padre[n]][0]
            hijoPadre[n][1]= x[padre[n]][1]
            hijoPadre[n][2]= x[padre[n]][2]
            hijoPadre[n][3]= x[madre[n]][3]
            hijoPadre[n][4]= x[madre[n]][4]

            hijoMadre[n][0]= x[madre[n]][0]
            hijoMadre[n][1]= x[madre[n]][1]
            hijoMadre[n][2]= x[madre[n]][2]
            hijoMadre[n][3]= x[padre[n]][3]
            hijoMadre[n][4]= x[padre[n]][4]
        
        if numeroCruce[n] == 4:
            hijoPadre[n][0]= x[padre[n]][0]
            hijoPadre[n][1]= x[padre[n]][1]
            hijoPadre[n][2]= x[padre[n]][2]
            hijoPadre[n][3]= x[padre[n]][3]
            hijoPadre[n][4]= x[madre[n]][4]

            hijoMadre[n][0]= x[madre[n]][0]
            hijoMadre[n][1]= x[madre[n]][1]
            hijoMadre[n][2]= x[madre[n]][2]
            hijoMadre[n][3]= x[madre[n]][3]
            hijoMadre[n][4]= x[padre[n]][4]
        
    #print (hijoPadre)
    #print (hijoMadre)
    #tabla3.poblacion tras el cruce
    l = 0
    for n in range(3):
        x[l] = hijoPadre[n]
        x[l+1] = hijoMadre[n]
        l = l+2
    


    
    print("Tabla 3.Matriz después del cruce\n",x) #Matriz después del cruce
    xdec = []
    xdec2 = []
    for n in range(6):
        position = 4
        resultdec=0
        for m in range(5):
            resultdec=x[n][m]*2**position + resultdec
            #print("resultdec,position",resultdec,position)
            position = position-1
        xdec.append(resultdec)
        xdec2.append(resultdec**2)
    print (xdec)
    print (xdec2)
    valido=0
    iteracion = iteracion + 1 
    print ("Iteración N°:",iteracion)