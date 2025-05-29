
class RegistroAdocao:
    def registrar(self, adotante, pet, entrega_info):
        return f"Adoção registrada para {adotante.nome} com o pet {pet.nome} em {entrega_info['timestamp']}."
