class EnderecoAdapter:
    def __init__(self, dados_externos):
        self.dados_externos = dados_externos

    def obter_endereco_formatado(self):
        cidade = self.dados_externos.get("cidade", "")
        estado = self.dados_externos.get("estado", "")
        return f"{cidade} - {estado}"