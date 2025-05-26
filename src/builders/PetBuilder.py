from src.models.Pet import Pet  

class PetBuilder:
    def __init__(self):
        self._nome = None
        self._idade = None
        self._especie = "Desconhecida"
        self._sexo = None
        self._castrado = False
        self._vacinas = []

    def set_nome(self, nome):
        self._nome = nome
        return self

    def set_idade(self, idade):
        self._idade = idade
        return self

    def set_especie(self, especie):
        self._especie = especie
        return self

    def set_sexo(self, sexo):
        self._sexo = sexo
        return self

    def set_castrado(self, castrado):
        self._castrado = castrado
        return self

    def build(self):
        if not all([self._nome, self._idade, self._sexo, self._castrado is not None]):
            raise ValueError("Todos os campos obrigatórios devem ser preenchidos.")
        pet = Pet(self._nome, self._idade, self._especie, self._sexo, self._castrado)

        if self._especie:
            pet.raca = self._especie
        if self._sexo:
            pet.sexo = self._sexo
        if self._vacinas:
            for vacina in self._vacinas:
                pet.adicionar_vacinas(vacina)


        return Pet(pet._nome, pet._idade, pet._especie, pet._sexo, pet._castrado)
    def adicionar_vacina(self, vacina):
        """ Método para adicionar vacinas ao pet """
        if vacina not in self._vacinas:
            self._vacinas.append(vacina)
        else:
            print(f"A vacina {vacina} já está cadastrada.")
        return self
    



builder = PetBuilder()
pet = (builder
       .set_nome("Rex")
       .set_idade(3)
       .set_especie("Cachorro")
       .set_sexo("Macho")
       .set_castrado(True)
       .adicionar_vacina("Antirrábica")
       .build())

print(pet.getInfo())
