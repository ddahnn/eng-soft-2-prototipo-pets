from abc import ABC, abstractmethod

class Pet( ABC ):
    _listaPets = []
    _id= 0
    def __init__(self, nome, idade, especie, sexo,  castrado: bool):
        """ Construtor da classe Pet """
        Pet._id += 1
        self._id = Pet._id
        self._nome = nome
        self._idade = idade
        self._especie = especie
        self._sexo = sexo
        self._vacinas = []
        self._castrado = castrado

    def ver_lista_Vacinas(self):
        """ Método para verificar a lista de vacinas """
        if len(self._vacinas) == 0:
            print("Nenhuma vacina cadastrada.")
        else:
            print("Lista de vacinas:")
            for vacina in self._vacinas:
                print(vacina)

    

    def adicionar_vacinas(self, vacina):
        """ Método para adicionar vacinas """
        if vacina not in self._vacinas:
            self._vacinas.append(vacina)
        else:
            print(f"A vacina {vacina} já está cadastrada.")



    @property
    def nome(self):
        return self._nome   
    
    @property
    def idade(self):
        return self._idade
    
    @property
    def humor(self):
        return self._humor
    
    @property  
    def raca(self):
        return self._raca
    
    @property
    def sexo(self):
        return self._sexo
    
    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo
    
    @property
    def vacinado(self):
        return self._vacinado

    @property
    def castrado(self):
        return self._castrado
    # Setter
    @nome.setter    
    def nome(self, nome):
        self._nome = nome

    @castrado.setter
    def castrado(self, castrado):
        self._castrado = castrado

    @raca.setter
    def raca(self, raca):
        self._raca = raca

    @humor.setter
    def humor(self, humor):
        self._humor = humor

    @idade.setter
    def idade(self, idade):
        self._idade = idade
    @vacinado.setter
    def vacinado(self, vacinado):
        self._vacinado = vacinado

    def getInfo(self):
        return f"""
-------------INFORMAÇÕES DO PET-------------
            Nome: {self._nome},
            Idade: {self._idade}, 
            Especie: {self._especie}, 
            Sexo: {self._sexo},
            Vacinado: {self._vacinas},
            Castrado: {self._castrado}
            """