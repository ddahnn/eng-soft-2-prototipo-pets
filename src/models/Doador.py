from src.models.Usuario import Usuario
from src.models.Pet import Pet

class Doador(Usuario):
    def __init__(self, nome, dtNasc, endereco, telefone, email, cpf: str):
        super().__init__(nome, dtNasc, endereco, telefone, email)
        self._cpf = None
        self.cpf = cpf
        self._doador = True

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("O CPF deve conter exatamente 11 dígitos numéricos.")
        self._cpf = cpf

    @property
    def tipo(self):
        return "Doador"

    def getInfo(self):
        info = super().getInfo()
        return f'{info}CPF: {self._cpf}\n            Tipo: {self.tipo}'

    def cadastrarPet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("O objeto deve ser uma instância da classe Pet.")
        if not all([pet.nome, pet.idade, pet.sexo, pet.castrado]):
            raise ValueError("Todos os campos obrigatórios do pet devem estar preenchidos.")
        for p in Pet._listaPets:
            if p._id == pet._id:
                raise ValueError("O pet já está cadastrado.")
        Pet._listaPets.append(pet)
        print(f"Pet {pet.nome} cadastrado com sucesso pelo doador {self.nome}.")
