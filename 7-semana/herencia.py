class Animal:
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print(f"Soy un animal del tipo {type(self).__name__}")


class Perro(Animal):

    def __init__(self, especie, edad, duenio):
        super().__init__(especie, edad)
        self.duenio = duenio

    def hablar(self):
        print("guau guau")

    def moverse(self):
        print("Camina en 4 patas")


class Vaca(Animal):

    def hablar(self):
        print("muuu")

    def moverse(self):
        print("Camina en 4 patas")


perro1 = Perro("Mamifero", 2)

perro1.describeme()


vaca1 = Vaca("Mamifero", 12)
