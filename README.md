# Plataforma PetHub - Padrões de Projeto (1ª Entrega)

## 📌 Objetivo da Entrega

Esta entrega tem como objetivo implementar os principais **padrões criacionais** de projeto dentro do sistema **Plataforma de E-commerce e Rede Social para Adoção de Pets**, iniciando o projeto com uma base sólida, flexível e testável.

---

## 🧱 Padrões de Projeto Utilizados

### 1. Singleton

**Descrição:**  
Garante que uma única instância de uma classe seja criada durante a execução do sistema. 
 
**Aplicação:**  
Foi utilizado para gerenciar a conexão com o banco de dados, garantindo que apenas uma instância de conexão exista no sistema.

**Trecho de código:**
# classe que representa uma conexão com banco de dados simulada (mockada)
class DatabaseConnection:
    # atributo de classe que armazenará a única instância criada (padrão Singleton)
    _instance = None

    @staticmethod
    def get_instance():
        '''
        Método estático que retorna a instância única da classe.
        Se ainda não existir, cria uma nova instância chamando o construtor.
        '''
        if DatabaseConnection._instance is None:
            DatabaseConnection()  # cria a instância
        return DatabaseConnection._instance  # retorna a instância única

    def __init__(self):
        '''
        Construtor da classe. Se já houver uma instância, impede a criação de outra.
        Caso contrário, define a "conexão" e salva a instância na variável de classe.
        '''
        # verifica se já existe uma instância criada
        if DatabaseConnection._instance is not None:
            raise Exception("Esta classe é Singleton!")  # impede múltiplas instâncias
        else:
            # simula a criação da conexão (aqui seria uma conexão real com banco de dados)
            self.connection = "Conexão estabelecida"
            # armazena a instância criada no atributo de classe
            DatabaseConnection._instance = self


2. Factory Method

Descrição:
O padrão Factory Method define uma interface para criar objetos, mas permite que as subclasses alterem o tipo de objetos que serão criados. Isso promove o princípio aberto/fechado: o código é aberto para extensão, mas fechado para modificação.

Aplicação no Projeto:
Foi utilizado para criar os diferentes perfis de usuários da plataforma: Adotante, Vendedor, Anjo (Resgatador) e Admin.
A classe UserFactory centraliza e encapsula a lógica de criação, evitando repetição e facilitando testes e manutenções futuras.

Vantagens no contexto do projeto:

    Evita if/else espalhados para instanciar usuários.

    Facilita a adição de novos perfis no futuro.

    Padroniza a criação dos objetos e aumenta a legibilidade.

    # Trecho da UserFactory
class UserFactory:
    @staticmethod
    def criar_usuario(tipo, nome, endereco, telefone, **kwargs):
        if tipo.lower() == "adotante":
            return Adotante(nome, endereco, telefone, cpf=kwargs.get("cpf", ""))
        elif tipo.lower() == "vendedor":
            return Vendedor(nome, endereco, telefone, cnpj=kwargs.get("cnpj", ""))
        elif tipo.lower() in ["resgatador", "anjo"]:
            return Anjo(nome, endereco, telefone, cpf=kwargs.get("cpf", ""))
        elif tipo.lower() == "admin":
            return Admin(nome, endereco, telefone, email_admin=kwargs.get("email_admin", ""))
        else:
            raise ValueError(f"Tipo de usuário inválido: {tipo}")


usuario = UserFactory.criar_usuario(
    tipo="Adotante",
    nome="Maria da Silva",
    endereco="Rua X, 123",
    telefone="(11) 91234-5678",
    cpf="123.456.789-00"
)






3. Builder

Descrição:
O padrão Builder é utilizado para construir objetos complexos passo a passo, permitindo diferentes representações do mesmo objeto. Ele é ideal quando um objeto possui muitos atributos opcionais e regras de validação.

Aplicação no Projeto:
Foi utilizado para criar a entidade Pet, que possui atributos obrigatórios (nome, espécie, idade, sexo, localização, fotos) e opcionais (raça, vacinas, castração, temperamento).
O uso do Builder facilita a montagem flexível e segura desses objetos, com validações e leitura clara do código.

Vantagens no contexto do projeto:

    Criação clara e encadeada de objetos.

    Evita construtores grandes e difíceis de manter.

    Facilita a adição de novos campos no futuro.

    Permite validação dos campos obrigatórios no método .build().

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

# O código abaixo levantaria um erro pois faltam campos obrigatórios:
pet = PetBuilder().set_nome("Tobby").build()
# => ValueError: Campos obrigatórios não foram preenchidos.


## 🧩 3ª Entrega – Padrões Comportamentais

### 👁️ Observer
Padrão usado para notificar usuários automaticamente.
Trecho de código: `src/behavioral/observer.py`

### 🧠 Strategy
Padrão usado para mudar a lógica de cálculo de pontos.
Trecho de código: `src/behavioral/strategy.py`
