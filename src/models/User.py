from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone


    @abstractmethod
    def get_tipo(self)-> str:
        pass

    def informacoes(self) -> str:
        return f"""
        *****   Dados Principais do usuario {self.nome}  ****
        Nome: {self.nome}
        Endereço: {self.endereco},
        Telefone: {self.telefone},
        """
    
