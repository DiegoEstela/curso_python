class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona1 = Persona("Diego", 31)
print(type(persona1))
print(persona1.nombre)
