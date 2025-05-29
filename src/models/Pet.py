class Pet:
    def __init__( self, nome, especie, idade, sexo, localizacao, fotos, raca=None, vacinas=None, castracao=None, temperamento=None ):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.sexo = sexo
        self.localizacao = localizacao
        self.fotos = fotos  
        self.raca = raca
        self.vacinas = vacinas
        self.castracao = castracao
        self.temperamento = temperamento

    def __str__(self):
        return f""" 
            Nome: {self.nome} | Espécie: {self.especie} | Idade: {self.idade} | 
            Sexo: {self.sexo} | Localização: {self.localizacao} | 
            Raça: {self.raca or 'SRD'} | Castração: {self.castracao or 'N/I'}
         """