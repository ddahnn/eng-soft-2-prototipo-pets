from abc import ABC, abstractmethod

class Pet(  ):
    _listaPets = []
    _id= 0
    def __init__(self, nome, idade, humor, raca, sexo, vacinado: bool, castrado: bool):
        """ Construtor da classe Pet """
        Pet._id =+ 1
        self._id = Pet._id
        self._nome = nome
        self._idade = idade
        self._humor = humor
        self._raca = raca
        self._sexo = sexo
        self._vacinado = vacinado
        self._castrado = castrado

    @property
    def nome(self):
        return self._nome   
    
    @nome.setter    
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @property
    def humor(self):
        return self._humor
    
    @humor.setter
    def humor(self, humor):
        self._humor = humor

    @property  
    def raca(self):
        return self._raca
    
    @raca.setter
    def raca(self, raca):
        self._raca = raca

    @property
    def sexo(self):
        return self._sexo
    
    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo
    
    @property
    def vacinado(self):
        return self._vacinado
    
    @vacinado.setter
    def vacinado(self, vacinado):
        self._vacinado = vacinado

    @property
    def castrado(self):
        return self._castrado
    
    @castrado.setter
    def castrado(self, castrado):
        self._castrado = castrado


    def getInfo(self):
        return f"""
-------------INFORMAÇÕES DO PET-------------
            Nome: {self._nome},
            Idade: {self._idade}, 
            Humor: {self._humor}, 
            Raça: {self._raca}, 
            Sexo: {self._sexo},
            Vacinado: {self._vacinado},
            Castrado: {self._castrado}
            """