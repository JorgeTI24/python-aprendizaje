def sumar():
    while True:
        try:
           suma = int(input("Ingresa un número: "))
        except:
           print("Valor no válido")
           continue
        try:
            segundo_numero = int(input("+: "))
        except:
            print("Valor no válido")
            continue
        if suma > 0 or segundo_numero > 0:
            resultado = suma + segundo_numero
            print(resultado)
            break
        

def restar():
    while True:
        try:
           resta = int(input("Ingresa un número: "))
        except:
           print("Valor no válido")
           continue
        try:
            segundo_numero = int(input("-: "))
        except:
            print("Valor no válido")
            continue
        if resta > 0 or segundo_numero > 0:
            resultado = resta - segundo_numero
            print(resultado)
            break



def multiplicacion():
    while True:
        try:
           multiplicar = int(input("Ingresa un número: "))
        except:
           print("Valor no válido")
           continue
        try:
            segundo_numero = int(input("x: "))
        except:
            print("Valor no válido")
            continue
        if multiplicar > 0 or segundo_numero > 0:
            resultado = multiplicar * segundo_numero
            print(resultado)
            break

def division():
    while True:
        try:
           dividir = int(input("Ingresa un número: "))
        except:
           print("Valor no válido")
           continue
        try:
            segundo_numero = int(input("/: "))
        except:
            print("Valor no válido")
            continue
        if dividir > 0 or segundo_numero > 0:
            resultado = dividir / segundo_numero
            print(resultado)
            break

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opción: ")

if opcion == "1":
    sumar()
elif opcion == "2":
    restar()
elif opcion == "3":
    multiplicacion()
elif opcion == "4":
    division()








        
       

            

    




