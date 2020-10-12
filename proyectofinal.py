#Este script tiene como fin poner a prueba los conocimientos del usuario
#con ejercicios de operaciones con números random
# o el uso de una calculadora según la operación que sea seleccionada.
import random,time
def suma (a,b):
    return(a+b)
def resta (a,b):
    return (a-b)
def multiplicacion (a,b):
    return (a*b)
def division (a,b):
    return(a/b)
def potencia (a,b):
    return (a**b)
def raiz(a,b):
    return (a**1/b)
def cuadro():
    print('Llevas 4 errores, para pasar, tendrás que resolver el siguiente acertijo.')
    time.sleep(3)
    #Cuadrado mágico
    cm=[[4,9,2],[3,5,7],[8,1,6]]
    cmr=[[0,0,0],[0,0,0],[0,0,0]]
    e=0
    print('''En el cuadrado mágico puedes sumar toda la fila, columna
    o diagonal y siempre te dará el mismo resultado, en este
    caso debe dar 15, escribe el tuyo de izquierda a derecha:\nHint: solo se usan los números del 1 al 9 una sola vez cada uno.''')
    for i in range(len(cmr)):
        for j in range(len(cmr[i])):
            n=int(input())
            cmr[i][j]=n
    for i in range(len(cmr)):
        for j in range(len(cmr[i])):
            if(cmr[i][j]!=cm[i][j]):
                e+=1
    if(e==0):
        print('Correcto')
        print('\n',cmr[0],'\n',cmr[1],'\n',cmr[2])
    else:
        print('Tuviste',e,'error(es), escribiste: ')
        print('\n',cmr[0],'\n',cmr[1],'\n',cmr[2])
        print('Lo correcto es:')
        print('\n',cm[0],'\n',cm[1],'\n',cm[2])
    return '1'
x=input("¿Qué operación quiere realizar?\n-suma\n-resta\n-multiplicación\n-división\n-potencia\n-raiz \n")
y=input("¿Calculadora o ejercicios? ")
points = []
tiempo = 0
if(y=="calculadora" or y=="Calculadora" or y=="CALCULADORA"):
    if(x=='suma' or x=='Suma' or x=='SUMA'):
        a=float(input("Ingrese el primer numero "))
        b=float(input("Ingrese el segundo numero "))
        print(suma(a,b))
    else:
            if(x=='resta' or x=='Resta' or x=='RESTA'):
                a=float(input("Ingrese el primer numero "))
                b=float(input("Ingrese el segundo numero "))
                print(resta(a,b))
            else:
                if(x=='multiplicacion' or x=='Multiplicacion' or x=='MULTIPLICACION'):
                    a=float(input("Ingrese el primer numero "))
                    b=float(input("Ingrese el segundo numero "))
                    print(multiplicacion(a,b))
                else:
                    if(x=='division' or x=='Division' or x=='DIVISION'):
                        a=float(input("Ingrese el dividendo "))
                        b=float(input("Ingrese el divisor "))
                        print(division(a,b))
                    else:
                        if(x=='potencia' or x=='Potencia' or x=='POTENCIA'):
                            a=float(input("Ingrese el numero que desea elevar "))
                            b=float(input("Ingrese el exponente "))
                            print(potencia(a,b))
                        else:
                            if(x=='raiz' or x=='Raiz' or x=='RAIZ'):
                                a=float(input("Ingrese el numero del que desea saber la raiz "))
                                b=float(input("Ingrese el indice "))
                                print(raiz(a,b))
else:
    if(y=='ejercicios' or y=='Ejercicios' or y=='EJERCICIOS'):
        if(x=='suma' or x=='Suma' or x=='SUMA'):
            while True:
                a = random.randint(0,99)
                b = random.randint(0,99)
                print("¿Cuánto es ",a," + ",b,"?\n¡Tienes 10 segundos!")
                start = time.time()
                time.clock()
                r = int(input())
                tiempo = time.time() - start
                if r == a + b:
                    if tiempo >= 10:
                        print("tardaste mucho!, inténtalo de nuevo")
                        points.append('1')
                        continue
                    else:
                        seguir = input("correcto!\n¿Quieres seguir haciendo ejercicios? ")
                        if seguir == "si":
                            continue
                        else:
                            print("Tuviste ",len(points)," error(es).\n ¡Hasta luego!")
                            break
                elif r != a + b:
                    if tiempo >= 10:
                        print("tardaste mucho!, inténtalo de nuevo")
                        points.append('1')
                        if len(points) % 4 == 0:
                            cuadro()
                            continue
                        else:
                            continue
                    else:
                        print("incorrecto, inténtalo de nuevo")
                        points.append('1')
                        if len(points) % 4 == 0:
                            cuadro()
                            continue
                        else:
                            continue
        else:
            if(x=='resta' or x=='Resta' or x=='RESTA'):
                while True:
                    a = random.randint(0,99)
                    b = random.randint(0,99)
                    print("¿Cuánto es ",a," - ",b,"?\n¡Tienes 10 segundos!")
                    start = time.time()
                    time.clock()
                    r = int(input())
                    tiempo = time.time() - start
                    if r == a - b:
                        if tiempo >= 10:
                            print("tardaste mucho!, inténtalo de nuevo")
                            points.append('1')
                            continue
                        else:
                            seguir = input("correcto!\n¿Quieres seguir haciendo ejercicios? ")
                            if seguir == "si":
                                continue
                            else:
                                print("Tuviste ",len(points)," error(es).\n ¡Hasta luego!")
                                break
                    elif r != a - b:
                        if tiempo >= 10:
                            print("tardaste mucho!, inténtalo de nuevo")
                            points.append('1')
                            if len(points) % 4 == 0:
                                cuadro()
                                continue
                            else:
                                continue
                        else:
                            print("incorrecto, inténtalo de nuevo")
                            points.append('1')
                            if len(points) % 4 == 0:
                                cuadro()
                                continue
                            else:
                                continue
            else:
                if(x=='multiplicacion' or x=='Multiplicacion' or x=='MULTIPLICACION'):
                    while True:
                        a = random.randint(0,99)
                        b = random.randint(0,10)
                        print("¿Cuánto es ",a," * ",b,"?\n¡Tienes 15 segundos!")
                        start = time.time()
                        time.clock()
                        r = int(input())
                        tiempo = time.time() - start
                        if r == a * b:
                            if tiempo >= 15:
                                print("tardaste mucho!, inténtalo de nuevo")
                                points.append('1')
                                continue
                            else:
                                seguir = input("correcto!\n¿Quieres seguir haciendo ejercicios? ")
                                if seguir == "si":
                                    continue
                                else:
                                    print("Tuviste ",len(points)," error(es).\n ¡Hasta luego!")
                                    break
                        elif r != a - b:
                            if tiempo >= 10:
                                print("tardaste mucho!, inténtalo de nuevo")
                                points.append('1')
                                if len(points) % 4 == 0:
                                    cuadro()
                                    continue
                                else:
                                    continue
                            else:
                                print("incorrecto, inténtalo de nuevo")
                                points.append('1')
                                if len(points) % 4 == 0:
                                    cuadro()
                                    continue
                                else:
                                    continue
                else:
                    if(x=='division' or x=='Division' or x=='DIVISION'):
                         while True:
                            a = random.randint(0,99)
                            b = random.randint(0,10)
                            print("¿Cuánto es ",a," / ",b,"?\n¡Tienes 15 segundos!")
                            start = time.time()
                            time.clock()
                            r = int(input())
                            tiempo = time.time() - start
                            if r == a / b:
                                if tiempo >= 15:
                                    print("tardaste mucho!, inténtalo de nuevo")
                                    points.append('1')
                                    continue
                                else:
                                    seguir = input("correcto!\n¿Quieres seguir haciendo ejercicios? ")
                                    if seguir == "si":
                                        continue
                                    else:
                                        print("Tuviste ",len(points)," error(es).\n ¡Hasta luego!")
                                        break
                            elif r != a / b:
                                if tiempo >= 10:
                                    print("tardaste mucho!, inténtalo de nuevo")
                                    points.append('1')
                                    if len(points) % 4 == 0:
                                        cuadro()
                                        continue
                                    else:
                                        continue
                                else:
                                    print("incorrecto, inténtalo de nuevo")
                                    points.append('1')
                                    if len(points) % 4 == 0:
                                        cuadro()
                                        continue
                                    else:
                                        continue
                    else:
                        if(x=='potencia' or x=='Potencia' or x=='POTENCIA'):
                            while True:
                                b = random.randint(1,3)
                                if b == 2:
                                    a = random.randint(0,20)
                                    exp = "cuadrado"
                                elif b == 1:
                                    a = random.randint(0,20)
                                    exp = "uno"
                                else:
                                    a= random.randint(0,10)
                                    exp = "cubo"
                                    print("¿Cuánto es ",a," al ",exp,"?\n¡Tienes 15 segundos!")
                                    start = time.time()
                                    time.clock()
                                    r = int(input())
                                    tiempo = time.time() - start
                                    if r == a ** b:
                                        if tiempo >= 15:
                                            print("tardaste mucho!, inténtalo de nuevo")
                                            points.append('1')
                                            continue
                                        else:
                                            seguir = input("correcto!\n¿Quieres seguir haciendo ejercicios? ")
                                            if seguir == "si":
                                                continue
                                            else:
                                                print("Tuviste ",len(points)," error(es).\n ¡Hasta luego!")
                                                break
                                    elif r != a ** b:
                                        if tiempo >= 10:
                                            print("tardaste mucho!, inténtalo de nuevo")
                                            points.append('1')
                                            if len(points) % 4 == 0:
                                                cuadro()
                                                continue
                                            else:
                                                continue
                                        else:
                                            print("incorrecto, inténtalo de nuevo")
                                            points.append('1')
                                            if len(points) % 4 == 0:
                                                cuadro()
                                                continue
                                            else:
                                                continue
                        else:
                            if(x=='raiz' or x=='Raiz' or x=='RAIZ'):
                                while True:
                                    a = random.randint(1,20)
                                    print("¿Cuál es la raíz cuadrada de ",a**2,"?\n¡Tienes 20 segundos!")
                                    start = time.time()
                                    time.clock()
                                    r = int(input())
                                    tiempo = time.time() - start
                                    if r == a:
                                        if tiempo >= 20:
                                            print("tardaste mucho!, inténtalo de nuevo")
                                            points.append('1')
                                            continue
                                        else:
                                            seguir = input("correcto!\n¿Quieres seguir haciendo ejercicios? ")
                                            if seguir == "si":
                                                continue
                                            else:
                                                print("Tuviste ",len(points)," error(es).\n ¡Hasta luego!")
                                                break
                                    elif r != a:
                                        if tiempo >= 10:
                                            print("tardaste mucho!, inténtalo de nuevo")
                                            points.append('1')
                                            if len(points) % 4 == 0:
                                                cuadro()
                                                continue
                                            else:
                                                continue
                                        else:
                                            print("incorrecto, inténtalo de nuevo")
                                            points.append('1')
                                            if len(points) % 4 == 0:
                                                cuadro()
                                                continue
                                            else:
                                                continue
    else:
        print("Operacion inexistente")