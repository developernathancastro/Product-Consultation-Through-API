import pyodbc

class ConectorBancodeDados:

    def __init__(self, driver, server, database):
        self.driver = driver
        self.server = server
        self.database = database
        self.conexao = None
        self.cursor = None

    def conectar(self):
        string_conexao = f"Driver={self.driver}; Server={self.server}; Database={self.database}"
        self.conexao = pyodbc.connect(string_conexao)
        self.cursor = self.conexao.cursor()

    def executar_consulta(self, consulta):
        self.cursor.execute(consulta)
        return self.cursor.fetchall()

    def fechar_conexao(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()








