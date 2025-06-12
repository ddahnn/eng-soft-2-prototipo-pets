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


## 🧩 3ª Entrega – Padrões Comportamentais

### 👁️ Observer
Padrão usado para notificar usuários automaticamente.
Trecho de código: `src/behavioral/observer.py`

### 🧠 Strategy
Padrão usado para mudar a lógica de cálculo de pontos.
Trecho de código: `src/behavioral/strategy.py`
