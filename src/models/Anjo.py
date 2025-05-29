# src/models/Anjo.py

from src.models.User import User

class Anjo(User):
    def __init__(self, nome, endereco, telefone, cpf=""):
        super().__init__(nome, endereco, telefone)
        self.tipo = "Salvador"
        self.cpf = cpf
        self.pets_resgatados = []

    def get_tipo(self) -> str:
         return self.tipo

    def informacoes(self) -> str:
        info = super().informacoes()
        return f"""
        {info}Tipo: {self.tipo}
        CPF: {self.cpf}
"""

    def adicionar_pet_resgatado(self, pet):
        self.pets_resgatados.append(pet)

    def listar_pets_resgatados(self) -> str:
        if not self.pets_resgatados:
            return "Nenhum pet resgatado ainda."
        return "\n".join([str(pet) for pet in self.pets_resgatados])
