from src.models.Adotante import Adotante
from src.models.Vendedor import Vendedor
from src.models.Anjo import Anjo
from src.models.Admin import Admin


class UserFac:
    @staticmethod
    def criar_usuario(tipo, nome, endereco, telefone, **kwargs):
        """
        Cria uma instância do tipo de usuário solicitado.
        :param tipo: Tipo do usuário (Adotante, Vendedor, Resgatador, Admin)
        :param nome: Nome do usuário
        :param endereco: Endereço do usuário
        :param telefone: Telefone de contato
        :param kwargs: Argumentos adicionais como cpf, cnpj, rg, email_admin
        :return: Instância de uma subclasse de User
"""     
        tipo = tipo.lower()


        if tipo == "adotante":
            return Adotante(nome, endereco, telefone, cpf=kwargs.get("cpf", ""))
        elif tipo == "vendedor":
            return Vendedor(nome, endereco, telefone, cnpj=kwargs.get("cnpj", ""))
        elif tipo == "resgatador" or tipo == "anjo":
            return Anjo(nome, endereco, telefone, cpf=kwargs.get("cpf", ""))
        elif tipo == "admin":
            return Admin(nome, endereco, telefone, email_admin=kwargs.get("email_admin", ""))
        else:
            raise ValueError(f"Tipo de usuário inválido: {tipo}")