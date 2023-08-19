cantidad_iteraciones = int(
    input("Ingresa cuantos valores vas a querer sumar para calcular la media: "))

lista = []

for iteracion in range(cantidad_iteraciones):
    lista.append(int(input("Ingrese un numero para sumar: ")))

media = sum(lista) / cantidad_iteraciones

print("la media es", media)
