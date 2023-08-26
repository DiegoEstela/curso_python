
class Vector:
    def __init__(self, data):
        self.data = data
        pass

    def __str__(self):
        return f"El valor de este vector es: {self.data}"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, pos):
        return self.data[pos]

    def __setitem__(self, pos, value):
        self.data[pos] = value

    def __iter__(self):
        for pos in range(0, len(self.data)):
            yield f"value[{pos}]: {self.data[pos]}"


vector = Vector([1, 2, 3, 4])

for i in vector:
    print(i)
