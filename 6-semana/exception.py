try:
    n = float(input("ingrese un numero: "))
    5/n
except TypeError:
    print("no se pudo dividir el numero por un string")
except ValueError:
    print("debe introducir una cadena compuesta por numeros")
except ZeroDivisionError:
    print("ingrese un numero distinto de 0")
except Exception as e:
    print("ha ocurrido un error no previsto", type(e).__name__)
