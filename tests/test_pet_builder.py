import unittest
from src.builders.PetBuilder import PetBuilder
from src.models.Pet import Pet

class TestPetBuilder(unittest.TestCase):

    def setUp(self):
        self.fotos_validas = ["foto1.jpg", "foto2.jpg", "foto3.jpg"]

    def test_criacao_pet_completa(self):
        pet = (
            PetBuilder()
            .set_nome("Tobby")
            .set_especie("Cachorro")
            .set_idade(2)
            .set_sexo("Macho")
            .set_localizacao("Rio de Janeiro - RJ")
            .set_fotos(self.fotos_validas)
            .set_raca("Poodle")
            .set_vacinas(["Raiva", "V10"])
            .set_castracao(True)
            .build()
        )

        self.assertEqual(pet.nome, "Tobby")
        self.assertEqual(pet.raca, "Poodle")
        self.assertTrue(pet.castracao)

    def test_erro_falta_fotos(self):
        with self.assertRaises(ValueError) as context:
            (
                PetBuilder()
                .set_nome("Luna")
                .set_especie("Gato")
                .set_idade(1)
                .set_sexo("Fêmea")
                .set_localizacao("São Paulo - SP")
                .set_fotos(["foto1.jpg"])  # Menos de 3 fotos
                .build()
            )
        self.assertIn("mínimo 3 fotos", str(context.exception))

    def test_erro_campos_obrigatorios(self):
        with self.assertRaises(ValueError) as context:
            (
                PetBuilder()
                .set_nome("Sansão")
                .build()  # Vários campos obrigatórios ausentes
            )
        self.assertIn("Campos obrigatórios não foram preenchidos", str(context.exception))

    def test_criacao_pet_sem_campos_opcionais(self):
        pet = (
            PetBuilder()
            .set_nome("Bidu")
            .set_especie("Cachorro")
            .set_idade(4)
            .set_sexo("Macho")
            .set_localizacao("Curitiba - PR")
            .set_fotos(self.fotos_validas)
            .build()
        )

        self.assertEqual(pet.nome, "Bidu")
        self.assertIsNone(pet.raca)
        self.assertIsNone(pet.castracao)
