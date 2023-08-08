nombre = input('Ingresa tu nombre: ')
edad = int(input('Ingresa tu edad: '))

resultado = nombre != '****' and 5 < edad < 20 and 4 <= len(
    nombre) < 8 and edad*3 > 35


print(resultado)
