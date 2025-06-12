class EstrategiaRecompensa:
    def calcular_pontos(self, dados):
        raise NotImplementedError

class AdocaoEstrategia(EstrategiaRecompensa):
    def calcular_pontos(self, dados):
        return 100

class VendaEstrategia(EstrategiaRecompensa):
    def calcular_pontos(self, dados):
        return dados.get('valor', 0) * 0.1

class SistemaRecompensas:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def set_estrategia(self, estrategia):
        self.estrategia = estrategia

    def processar(self, dados):
        return self.estrategia.calcular_pontos(dados)
