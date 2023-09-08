""" from collections import namedtuple

pez = namedtuple("Pez", ['nombre', 'especie', 'peso'])

pez1 = pez("Pedro", "payaso", 200)

print(pez) """


from collections import Counter

""" list = [1, 2, 3, 4, 12, 23, 5, 32, 1, 4, 34, 1]

print(Counter(list)) """

estudiasntes = "Diego Ezequiel Lucas Matias Ayelen Sabrina"

print(Counter(estudiasntes))

print(Counter(estudiasntes.split()))
