
def operacion(opcion):
    while True:
        try:
            numero_1 = int(input("Inserta un número: "))
            numero_2 = int(input("Segundo número: "))
        except:
            print("Valor no válido")
            continue
        
        if opcion == 1:
            resultado = numero_1 + numero_2
        elif opcion == 2:
            resultado = numero_1 - numero_2
        elif opcion == 3:
            resultado = numero_1 * numero_2
        elif opcion == 4:
            resultado = numero_1 / numero_2
        
        print(resultado)
        break

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Elige una opción: "))
operacion(opcion)


        


        








        
       

            

    




