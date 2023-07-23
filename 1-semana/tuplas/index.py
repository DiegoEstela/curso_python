tupla = (8, 15, 4, 39, 5, 89, 87,  19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

# 1. Imprimir el último ítem de la tupla
ultimo_item = tupla[-1]
print("1. Último ítem:", ultimo_item)

# 2. Imprimir el número de ítems de la tupla
numero_items = len(tupla)
print("2. Número de ítems:", numero_items)

# 3. Imprimir la posición donde se encuentra el ítem 87 en la tupla
posicion_87 = tupla.index(87)
print("3. Posición del ítem 87:", posicion_87)

# 4. Crear una lista con los últimos tres ítems de la tupla y agregarle el 240
ultimos_tres_items = list(tupla[-3:])
ultimos_tres_items.append(240)
print("4. Últimos tres ítems con 240 añadido:", ultimos_tres_items)

# 5. Imprimir el ítem en la posición 8 de la tupla
item_posicion_8 = tupla[8]
print("5. Ítem en la posición 8:", item_posicion_8)

# 6. Contar el número de veces que el ítem 7 aparece en la tupla
conteo_item_7 = tupla.count(7)
print("6. Número de veces que el ítem 7 aparece:", conteo_item_7)