from src.builders.PetBuilder import PetBuilder

class  PetAdapter:
    """
    Adapter para transformar dados externos em uma instância válida de Pet usando o PetBuilder.
    """
        
    @staticmethod
    def adaptar(dados_externos: dict):
        """
        Converte dados recebidos de um sistema externo para o formato interno.
        
        :param dados_externos: dicionário no formato de entrada externa
        :return: objeto Pet
        """
        return (
            PetBuilder()
            .set_nome(dados_externos["nomeAnimal"])
            .set_especie(dados_externos["tipo"])
            .set_idade(dados_externos["idadeAnos"])
            .set_sexo("Macho" if dados_externos["sexo"] == "M" else "Fêmea")
            .set_localizacao(dados_externos["local"])
            .set_fotos(dados_externos["imagens"])
            .build()
        )