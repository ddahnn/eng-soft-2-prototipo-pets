from src.models.Pet import Pet

class PetBuilder:
    def __init__(self):
        # Define valores padrão (temporários)
        self.nome = None
        self.especie = None
        self.idade = None
        self.sexo = None
        self.localizacao = None
        self.fotos = []

        self.raca = None
        self.vacinas = None
        self.castracao = None
        self.temperamento = None


    def set_nome(self, nome):
        self.nome = nome
        return self

    def set_especie(self, especie):
        self.especie = especie
        return self

    def set_idade(self, idade):
        self.idade = idade
        return self

    def set_sexo(self, sexo):
        self.sexo = sexo
        return self

    def set_localizacao(self, cidade_estado):
        self.localizacao = cidade_estado
        return self

    def set_fotos(self, fotos):
        if len(fotos) < 3:
            raise ValueError("É obrigatório enviar no mínimo 3 fotos.")
        self.fotos = fotos
        return self

    def set_raca(self, raca):
        self.raca = raca
        return self

    def set_vacinas(self, vacinas):
        self.vacinas = vacinas
        return self

    def set_castracao(self, castracao):
        self.castracao = castracao
        return self

    def set_temperamento(self, temperamento):
        self.temperamento = temperamento
        return self

    def build(self):
        obrigatorios = [self.nome, self.especie, self.idade, self.sexo, self.localizacao, self.fotos]
        if any(campo is None for campo in obrigatorios):
            raise ValueError("Campos obrigatórios não foram preenchidos.")

        return Pet(
            nome=self.nome,
            especie=self.especie,
            idade=self.idade,
            sexo=self.sexo,
            localizacao=self.localizacao,
            fotos=self.fotos,
            raca=self.raca,
            vacinas=self.vacinas,
            castracao=self.castracao,
        )
