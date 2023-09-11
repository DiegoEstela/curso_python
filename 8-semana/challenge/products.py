class Televisor:

    paleta_de_colores = ['blanco', 'negro', 'rojo', 'azul', 'gris']

    valores_consumos = {
        'A': 100,
        'B': 80,
        'C': 60,
        'D': 50,
        'E': 30,
        'F': 10
    }

    def __init__(
        self, precio_base=100, color='blanco', consumo='F', peso=5
    ):
        self.precio_base = precio_base
        self.color = self.__validar_color(color)
        self.consumo = self.__validar_consumo(consumo)
        self.peso = peso

    def __validar_consumo(self, consumo):
        if consumo not in self.valores_consumos:
            return 'F'
        return consumo

    def __validar_color(self, color):
        if color.lower() not in self.paleta_de_colores:
            return 'blanco'
        return color

    def precio_final(self):

        precio = self.valores_consumos.get(self.consumo) + self.precio_base
        if 0 <= self.peso <= 19:
            precio += 10
        elif 20 <= self.peso <= 49:
            precio += 50
        elif 50 <= self.peso <= 79:
            precio += 80
        else:
            precio += 100

        return precio


televisores = [
    Televisor(250, 'rojo', 'E', 10),
    Televisor(143, 'negro', 'C', 13),
    Televisor(54, 'gris', 'A', 7),
    Televisor(300, 'violeta', 'B', 23)
]

precio_total = 0
for televisor in televisores:
    precio_total += televisor.precio_final()

print('El precio de el listado de televisores es', precio_total)
