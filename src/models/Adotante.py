from src.models.User import User

class Adotante(User):
    def __init__(self, nome, endereco, telefone, cpf=""):
        super().__init__(nome, endereco, telefone)
        self.tipo =  "Adotante"
        self.cpf = cpf

    def get_tipo(self):
        return self.tipo

    def informacoes(self) -> str:
        info = super().informacoes()
        return info+ f"""CPF: {self.cpf},
        Tipo: {self.tipo}"""