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
```python
class DatabaseConnection:
    _instance = None

    @staticmethod
    def get_instance():
        if DatabaseConnection._instance is None:
            DatabaseConnection()
        return DatabaseConnection._instance

    def __init__(self):
        if DatabaseConnection._instance is not None:
            raise Exception("Esta classe é Singleton!")
        else:
            # Aqui entraria a conexão com o banco (mockada)
            self.connection = "Conexão estabelecida"
            DatabaseConnection._instance = self
