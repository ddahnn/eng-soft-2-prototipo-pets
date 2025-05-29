from src.models.User import User

class Admin(User):
    def __init__(self, nome, endereco, telefone, email_admin=""):
        super().__init__(nome, endereco, telefone)
        self.tipo = "Administrador"
        self.email_admin = email_admin

    def get_tipo(self) -> str:
        return self.tipo

    def informacoes(self) -> str:
        info = super().informacoes()
        return info+f"""Tipo: {self.tipo}
        E-mail Institucional: {self.email_admin}"""


    def validar_documento(self, usuario):
        return f"Documentos do usuário {usuario.nome} validados com sucesso."

    def banir_usuario(self, usuario):
        return f"Usuário {usuario.nome} foi banido da plataforma."
