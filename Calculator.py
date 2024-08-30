"Lets gonna make a very simple calculator only two numbers"
numeroUno = int(input("Ingresa el primer numero"))
numeroDos = int(input("Ingresa el segundo numero"))

eleccion = 0
while eleccion != 7:
    print("Seleciona la operacion que quieres realizar tus numeros son: ", numeroUno, " y ", numeroDos )
    print("1.- Suma")
    print("2.- Resta")       
    print("3.- Division")
    print("4.- Multiplicacion")
    print("5.- Modulo")
    print("7.- Cambiar los numeros!")
    print("6.- Salir")


    eleccion = int(input())
    
    if eleccion == 1:
        print("Resultado: ", numeroUno + numeroDos)
    if eleccion == 2:
        print("Resulado: ", numeroUno - numeroDos)
    if eleccion == 3:
        print("Resultado: ", numeroUno * numeroDos)
    if eleccion == 4:
        print("Resultado: ", numeroUno / numeroDos)
    if eleccion == 5:
        print("Resultado: ",numeroUno % numeroDos)
    if eleccion == 6:
        numeroUno = int(input("Ingresa el nuevo valor del numero 1: "))
        numeroDos = int(input("Ingresa el nuevo valor del numero 2: "))
    if eleccion == 7:
        print("Gracias por usar mi calculadora sencilla!")
        print("Hasta la vista!")
        eleccion ==7



    