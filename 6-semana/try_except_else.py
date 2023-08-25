while (True):
    try:
        a = float(input("introduce un numero: "))
        b = float(input("introduce otro numero: "))
        print(a+b)
    except:
        print("Ocurrio un error.Tienes que introducir 2 numeros")
    else:
        print("La suma se realizo correctamente")
    break
