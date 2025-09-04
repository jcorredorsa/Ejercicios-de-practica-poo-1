def ej1():   
     print("Hola, ya se imprimir frases")
def ej2():   
     print("273")
def ej3():   
     suma=1234+532
     print(suma)
def ej4():
    resta=1234-532
    print(resta)  
def ej5():
     numero=int(input("Ingrese un numero: "))
     suma=int(((numero + 1) + (numero + 100)) * 100 / 2) 
     print(suma)
def ej6():
    euros = float(input("Ingrese la cantidad en euros: "))
    tasa_cambio = 1.08  
    dolares = euros * tasa_cambio
    print(f"{euros} euros equivalen a {dolares:.2f} dólares.")
def ej7():
    altura = float(input("Ingrese la altura del rectángulo: "))
    anchura = float(input("Ingrese la anchura del rectángulo: "))
    area = altura * anchura
    print(f"El área del rectángulo es: {area:.2f}")
def ej8():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num1 > num2:
        print(f"El mayor es: {num1}")
        print(f"El menor es: {num2}")
    elif num2 > num1:
        print(f"El mayor es: {num2}")
        print(f"El menor es: {num1}")
    else:
        print("Ambos números son iguales.")
def ej9():
    numero = int(input("Ingrese un número entero: "))
    for i in range(1, numero):
        if i % 2 != 0:
            print(i)
def ej10():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    
    def ej10(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    resultado = ej10(num1, num2)
    print(f"El máximo común divisor de {num1} y {num2} es: {resultado}")


#ej1()
#ej2()
#ej3()
#ej4()
#ej5()
#ej6()
#ej7()
#ej8()
#ej9()
#ej10()
