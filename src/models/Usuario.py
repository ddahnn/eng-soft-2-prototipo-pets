from abc import ABC, abstractmethod

class Usuario(ABC):
    def  __init__(self, nome, dtNasc, endereco, telefone, email):

        """ Construimos a classe abstrada Pessoa, é uma super classe para, 'Cliente' , 'Funcionario', vendedor, 'adotante'"""

        self._nome = nome
        self._dtNasc = dtNasc
        self._endereco = endereco
        self.telefone = telefone
        self.email = email

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def dtNasc(self):
        return self._dtNasc
    
    @dtNasc.setter
    def dtNasc(self, dtNasc):
        self._dtNasc = dtNasc

    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    
    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email

    def getInfo(self):
        return f"""
            -------------INFORMAÇÕES DO USUÁRIO-------------
            Nome: {self._nome},
            Data de Nascimento: {self._dtNasc}, 
            Endereço: {self._endereco}, 
            Telefone: {self._telefone}, 
            Email: {self._email},
            """


    @abstractmethod
    def cadastrarPet(self, pet):
        pass

