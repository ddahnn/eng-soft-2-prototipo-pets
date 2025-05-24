

class DatabaseConnection:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("[singleton] Criando nova instancia de conexao com o banco de dados")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self.connection = "Conecxão com o banco de dados"
        print("[singleton] Inicializando a conexão com o banco de dados")
    
    
    
    def get_connection(self):
        return self.connection
        