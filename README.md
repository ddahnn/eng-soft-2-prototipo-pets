# Plataforma PetHub - Padrões de Projeto (1ª Entrega)

## 📌 Objetivo da Entrega

Esta entrega tem como objetivo implementar os principais **padrões criaçionais** de projeto dentro do sistema **Plataforma de E-commerce e Rede Social para Adoção de Pets**, iniciando o projeto com uma base sólida, flexível e testável.

---

## 🧱 Padrões de Projeto Utilizados

---

### 1. Singleton

**Descrição:**
Garante que uma única instância de uma classe seja criada durante a execução do sistema.

**Aplicação no Projeto:**
Utilizado para gerenciar a conexão com o banco de dados, garantindo que apenas uma instância de conexão exista no sistema.

**Trecho de código:**

```python
class DatabaseConnection:
    _instance = None  # Armazena a instância única

    @staticmethod
    def get_instance():
        '''
        Retorna a instância única da classe.
        '''
        if DatabaseConnection._instance is None:
            DatabaseConnection()
        return DatabaseConnection._instance

    def __init__(self):
        if DatabaseConnection._instance is not None:
            raise Exception("Esta classe é Singleton!")
        else:
            self.connection = "Conexão estabelecida"
            DatabaseConnection._instance = self
```

---

### 2. Factory Method

**Descrição:**
Define uma interface para criar objetos, permitindo que subclasses determinem o tipo de objeto a ser criado. Promove o **princípio aberto/fechado**.

**Aplicação no Projeto:**
Utilizado para criar diferentes perfis de usuários: `Adotante`, `Vendedor`, `Anjo` (Resgatante) e `Admin`. A classe `UserFactory` centraliza essa lógica.

**Vantagens no Projeto:**

* Evita estruturas `if/else` espalhadas.
* Facilita a manutenção e extensão.
* Padroniza e organiza a criação de objetos.

**Trecho de código:**

```python
class UserFactory:
    @staticmethod
    def criar_usuario(tipo, nome, endereco, telefone, **kwargs):
        if tipo.lower() == "adotante":
            return Adotante(nome, endereco, telefone, cpf=kwargs.get("cpf", ""))
        elif tipo.lower() == "vendedor":
            return Vendedor(nome, endereco, telefone, cnpj=kwargs.get("cnpj", ""))
        elif tipo.lower() in ["resgatador", "anjo"]:
            return Anjo(nome, endereco, telefone, rg=kwargs.get("rg", ""), cpf=kwargs.get("cpf", ""))
        elif tipo.lower() == "admin":
            return Admin(nome, endereco, telefone, email_admin=kwargs.get("email_admin", ""))
        else:
            raise ValueError(f"Tipo de usuário inválido: {tipo}")
```

**Exemplo de uso:**

```python
usuario = UserFactory.criar_usuario(
    tipo="Adotante",
    nome="Maria da Silva",
    endereco="Rua X, 123",
    telefone="(11) 91234-5678",
    cpf="123.456.789-00"
)
```

---

### 3. Builder

**Descrição:**
Constrói objetos complexos passo a passo. Ideal quando existem atributos obrigatórios e opcionais, com validações.

**Aplicação no Projeto:**
Utilizado na criação da entidade `Pet`, com campos obrigatórios (nome, espécie, idade, sexo, localização, fotos) e opcionais (raça, vacinas, castração, temperamento).

**Vantagens no Projeto:**

* Criação encadeada e clara.
* Valida campos obrigatórios.
* Evita construtores longos.

**Trecho de código:**

```python
pet = (
    PetBuilder()
    .set_nome("Rex")
    .set_especie("Cachorro")
    .set_idade(3)
    .set_sexo("Macho")
    .set_localizacao("São Paulo - SP")
    .set_fotos(["foto1.jpg", "foto2.jpg", "foto3.jpg"])
    .set_raca("SRD")
    .set_castracao(True)
    .set_temperamento("Brincalhão e dócil")
    .build()
)
```

**Validação de erro:**

```python
pet = PetBuilder().set_nome("Tobby").build()
# => ValueError: Campos obrigatórios não foram preenchidos.
```

---

### 4. Facade

**Descrição:**
Fornece uma interface unificada para um conjunto de interfaces em um subsistema, simplificando seu uso.

**Aplicação no Projeto:**
Utilizado para orquestrar o processo completo de adoção, centralizando etapas como validação de documentos, validação de fotos, confirmação de entrega e registro da adoção.

**Vantagens no Projeto:**

* Reduz o acoplamento entre os componentes.
* Facilita testes e reutilização.
* Encapsula a complexidade do processo.

**Trecho de código:**

```python
class AdocaoFacade:
    def __init__(self, validador_documentos, validador_fotos, registro_adocao):
        self.validador_documentos = validador_documentos
        self.validador_fotos = validador_fotos
        self.registro_adocao = registro_adocao

    def processar_adocao(self, adotante, pet, documentos, fotos_entrega):
        if not self.validador_documentos.validar(documentos):
            return "Documentação inválida."

        if not self.validador_fotos.validar(pet.fotos):
            return "Fotos do pet estão incompletas ou inválidas."

        if len(fotos_entrega) < 1:
            return "É necessário anexar uma foto da entrega do pet."

        foto_com_data = {
            "foto": fotos_entrega[0],
            "timestamp": datetime.now().isoformat()
        }

        return self.registro_adocao.registrar(adotante, pet, foto_com_data)
```

**Exemplo de uso:**

```python
facade = AdocaoFacade(ValidadorDocumentos(), ValidadorFotos(), RegistroAdocao())
resultado = facade.processar_adocao(adotante, pet, documentos, fotos_entrega)
print(resultado)
```

---

### 5. Adapter

**Descrição:**
Converte a interface de uma classe em outra que o cliente espera. É útil para integrar sistemas ou dados com formatos diferentes.

**Aplicação no Projeto:**
Foi utilizado para adaptar dados de localização vindos de uma API externa (em formato de dicionário) para o modelo interno de localização da plataforma (string "Cidade - Estado").

**Vantagens no Projeto:**

* Facilita a integração com APIs externas ou módulos legados.
* Permite reutilizar código sem alterações internas.
* Torna o sistema mais flexível e compatível.

**Trecho de código:**

```python
class EnderecoAdapter:
    def __init__(self, dados_externos):
        self.dados_externos = dados_externos

    def obter_endereco_formatado(self):
        cidade = self.dados_externos.get("cidade", "")
        estado = self.dados_externos.get("estado", "")
        return f"{cidade} - {estado}"
```

**Exemplo de uso:**

```python
dados_api = {"cidade": "Belo Horizonte", "estado": "MG"}
adapter = EnderecoAdapter(dados_api)
endereco_formatado = adapter.obter_endereco_formatado()
print(endereco_formatado)  # Belo Horizonte - MG
```

---
