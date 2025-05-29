# tests/test_adocao_facade.py

import unittest
from src.facades.AdocaoFacade import AdocaoFacade

# Mocks dos serviços usados na fachada

class MockValidadorDocumentos:
    def validar(self, documentos):
        return all(doc in documentos for doc in ["rg", "cpf", "comprovante_residencia"])

class MockValidadorFotos:
    def validar(self, fotos):
        return fotos and len(fotos) >= 3

class MockRegistroAdocao:
    def registrar(self, adotante, pet, entrega_info):
        return f"Adoção registrada com sucesso para {adotante.nome} e {pet.nome}."


# Mocks de objetos
class MockAdotante:
    def __init__(self, nome):
        self.nome = nome

class MockPet:
    def __init__(self, nome, fotos):
        self.nome = nome
        self.fotos = fotos


class TestAdocaoFacade(unittest.TestCase):
    def setUp(self):
        self.facade = AdocaoFacade(
            MockValidadorDocumentos(),
            MockValidadorFotos(),
            MockRegistroAdocao()
        )

        self.adotante = MockAdotante("João")
        self.pet = MockPet("Rex", ["foto1.jpg", "foto2.jpg", "foto3.jpg"])
        self.documentos_validos = ["rg", "cpf", "comprovante_residencia"]

    def test_adocao_com_sucesso(self):
        resultado = self.facade.processarAdocao(
            self.adotante,
            self.pet,
            self.documentos_validos,
            foto_entrega=["entrega.jpg"]
        )
        self.assertIn("Adoção registrada com sucesso", resultado)

    def test_falta_documento(self):
        resultado = self.facade.processarAdocao(
            self.adotante,
            self.pet,
            documentos=["rg", "cpf"],  # faltando comprovante
            foto_entrega=["entrega.jpg"]
        )
        self.assertEqual(resultado, "Documentação inválida.")

    def test_fotos_do_pet_incompletas(self):
        pet_com_foto_unica = MockPet("Luna", ["foto1.jpg"])
        resultado = self.facade.processarAdocao(
            self.adotante,
            pet_com_foto_unica,
            self.documentos_validos,
            foto_entrega=["entrega.jpg"]
        )
        self.assertEqual(resultado, "Fotos do pet estão incompletas ou inválidas.")

    def test_sem_foto_de_entrega(self):
        resultado = self.facade.processarAdocao(
            self.adotante,
            self.pet,
            self.documentos_validos,
            foto_entrega=[]
        )
        self.assertEqual(resultado, "É necessário anexar uma foto da entrega do pet.")
