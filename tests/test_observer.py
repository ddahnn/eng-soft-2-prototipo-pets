from src.behavioral.observer import Usuario, Notificador

def test_notificacao():
    maria = Usuario("Maria")
    joao = Usuario("João")
    n = Notificador()
    n.adicionar(maria)
    n.adicionar(joao)
    n.notificar("Nova mensagem!")
