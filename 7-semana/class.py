class Perro:
    especie = 'Mamifero'

    # El constructor
    def __init__(self, nombre, raza):
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("Este perro acaba de ladrar!")

    def caminar(self, pasos):
        print(f"Este perro acaba de caminar {pasos} pasos")


perro1 = Perro("Sammy", "Caniche")

perro1.ladrar()
perro1.caminar(10)
