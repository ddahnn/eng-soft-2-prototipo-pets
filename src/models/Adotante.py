from src.models.Usuario import Usuario 
from src.models.Pet import Pet


class Adotante (Usuario):
    def __init__(self, nome, dtNasc, endereco, telefone, email, cpf: str ):
        """ Classe Adotante que herda de Pessoa """
        super().__init__(nome, dtNasc, endereco, telefone, email)
        self._adotante = True
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) < 11:
            raise ValueError("O CPF deve ter 11 dígitos.")
        elif len(cpf) > 11:
            raise ValueError("O CPF deve ter 11 dígitos.")
        else:   
            self._cpf = cpf

    def getInfo(self):
        info = super().getInfo()
        return f'{info}CPF: {self._cpf}'
    
    def cadastrarPet(self, pet):
        """ Método para cadastrar um pet """
        pass