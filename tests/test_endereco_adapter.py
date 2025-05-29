import unittest
from src.adapters.EnderecoAdapter import EnderecoAdapter

class TestEnderecoAdapter(unittest.TestCase):

    def test_endereco_completo(self):
        dados = {"cidade": "Belo Horizonte", "estado": "MG"}
        adapter = EnderecoAdapter(dados)
        self.assertEqual(adapter.obter_endereco_formatado(), "Belo Horizonte - MG")

    def test_endereco_sem_estado(self):
        dados = {"cidade": "São Paulo"}
        adapter = EnderecoAdapter(dados)
        self.assertEqual(adapter.obter_endereco_formatado(), "São Paulo - ")

    def test_endereco_sem_cidade(self):
        dados = {"estado": "SP"}
        adapter = EnderecoAdapter(dados)
        self.assertEqual(adapter.obter_endereco_formatado(), " - SP")

    def test_endereco_vazio(self):
        dados = {}
        adapter = EnderecoAdapter(dados)
        self.assertEqual(adapter.obter_endereco_formatado(), " - ")

if __name__ == "__main__":
    unittest.main()
