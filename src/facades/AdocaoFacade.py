from datetime import datetime

class AdocaoFacade:
    def __init__(self, validador_documentos, validador_fotos, registro_adocao):
        """
        Constrói a fachada com os serviços necessários.
            validador_documentos: serviço para validar CPF/comprovante
            validador_fotos: serviço que verifica as fotos do pet
            registro_adocao: serviço que salva a adoção
        """
        self.validador_documentos = validador_documentos
        self.validador_fotos = validador_fotos
        self.registro_adocao = registro_adocao

    def processarAdocao(self, adotante, pet,documentos, foto_entrega):
        """  
             Organiza o processo de adoção completo
        """
        if not self.validador_documentos.validar(documentos):
            return "Documentação inválida."
            
        # Etapa 2: Verificar fotos do pet (mínimo de 3 fotos)
        if not self.validador_fotos.validar(pet.fotos):
            return "Fotos do pet estão incompletas ou inválidas."
            
        # Etapa 3: Confirmar entrega com foto + timestamp
        if len(foto_entrega) < 1:
            return "É necessário anexar uma foto da entrega do pet."
            
        foto_com_data = {
            "foto": foto_entrega[0],
            "timestamp": datetime.now().isoformat()
        }
        # Etapa 4: Registrar adoção
        resultado = self.registro_adocao.registrar(adotante, pet, foto_com_data)
        return resultado