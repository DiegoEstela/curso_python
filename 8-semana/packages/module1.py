class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}'
