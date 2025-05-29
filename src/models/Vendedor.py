from src.models.User import User

class Vendedor(User):
    def __init__(self, nome, endereco, telefone, cnpj =""):
        super().__init__(nome, endereco, telefone)
        self.tipo = "Vendedor"
        self.cnpj = cnpj
        self.estoque = []
    
    def get_tipo(self) -> str:
        return self.tipo
    
    def informacoes(self) -> str:
        info =  super().informacoes()
        return info+ f"""Tipo: {self.tipo}
        CNPJ: {self.cnpj}"""
    
    def adicionar_produto(self):
        pass

    def remover_produto(self):
        pass

    def ver_Estoque(self):
        for item in self.estoque:
            print(item)