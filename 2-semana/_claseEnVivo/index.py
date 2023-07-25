""" Utilizando todo lo que sabes sobre cadenas, listas y sus métodos internos, transforma este texto:  
gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista

Transforma el texto en:  
Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies -le corrigió Troop.
- Strawberry menea la cabeza como disgustado… -agrega el comentarista. """

texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"

lista = texto.split('&')

lista[0] += '..'

lista2 = []

for oracion in lista:
    lista2.append(oracion[0].upper() + oracion[1:])

texto2 = '.\n- '.join(lista2)

texto2 += '.'

print(texto2)
