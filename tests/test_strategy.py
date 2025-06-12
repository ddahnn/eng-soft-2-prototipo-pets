from src.behavioral.strategy import AdocaoEstrategia, VendaEstrategia, SistemaRecompensas

def test_adocao():
    sistema = SistemaRecompensas(AdocaoEstrategia())
    assert sistema.processar({}) == 100

def test_venda():
    sistema = SistemaRecompensas(VendaEstrategia())
    assert sistema.processar({'valor': 200}) == 20.0
