""" condition = True
while condition:
    numero_ingresado = int(input("ingresa un numero impar: "))
    if numero_ingresado % 2 == 1:
        condition = False
    else:
        print("Debes ingresar un numero impar para poder escapar!")
print("muy bien ya saliste")
 """

num1 = int(input("Ingrese primer numero a operar: "))
num2 = int(input("Ingrese segundo numero a operar: "))

print("""
menu:
1. Sumar
2. Restar
3. Multiplicar
4. Salir
""")

option = input("Ingrese opcion del menu que desea ejecutar: ")

if option == '1':
    print(f'la suma de {num1} y {num2} es: {num1 + num2}')
elif option == '2':
    print(f'la resta de {num1} y {num2} es: {num1 - num2}')
elif option == '3':
    print(f'la multiplicacion de {num1} y {num2} es: {num1 * num2}')
elif option == '4':
    pass
else:
    print("Ingrese una opcion correcta!")
