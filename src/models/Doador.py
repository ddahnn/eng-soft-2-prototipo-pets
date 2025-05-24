from src.models.Usuario import Usuario



class Doador(Usuario):
    def __init__(self, nome, dtNasc, endereco, telefone, email, cpf: str):
        """ Classe Doador que herda de Usuario """
        super().__init__(nome, dtNasc, endereco, telefone, email)
        self._doador = True
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def _tipo(self):
        return "Doador" 
    
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
        return f'{info}CPF: {self._cpf} Tipo: '
    


    def cadastrarPet(self, pet):
        """ Método para cadastrar um pet """
        print('Pet cadastrado com sucesso!')
    
        