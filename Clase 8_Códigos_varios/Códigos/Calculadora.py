def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b !=0:
        return a/b
    else:
        return "no se puede dividir por 0"

def calculadora():
    print ("elige una operacion:")
    print ("1.sumar")
    print ("2.resta")
    print ("3.multiplicar")
    print ("4.dividir")
    opcion=int(input("Elige una opcion (1/2/3/4):"))
    num1=float(input("Elige un numero:"))
    num2=float(input("Elige un numero:"))


    if opcion==1:
        print(suma(num1,num2))
    elif opcion==2:
        print(resta(num1,num2))
    elif opcion==3:
        print(multiplicar(num1,num2))
    elif opcion==4:
        print(dividir(num1,num2))
    else:
        print("opcion no es valida")

calculadora()