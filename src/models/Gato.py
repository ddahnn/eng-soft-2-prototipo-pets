from src.models.Pet import Pet

class Gato(Pet):
    def __init__(self, nome, idade, sexo, castrado, especie="Gato"):
        super().__init__(nome, idade,  sexo,especie, castrado)
        self._especie = especie
        self._id = Pet._id
        Pet._id += 1