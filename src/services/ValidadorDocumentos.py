class ValidadorDocumentos:
    def validar(self, documentos):
        return all(doc in documentos for doc in ["rg", "cpf", "comprovante_residencia"])
