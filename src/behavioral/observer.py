class UsuarioObserver:
    def atualizar(self, mensagem):
        raise NotImplementedError

class Usuario(UsuarioObserver):
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, mensagem):
        print(f"[{self.nome}] Nova notificação: {mensagem}")

class Notificador:
    def __init__(self):
        self.observadores = []

    def adicionar(self, observador: UsuarioObserver):
        self.observadores.append(observador)

    def notificar(self, mensagem):
        for obs in self.observadores:
            obs.atualizar(mensagem)
