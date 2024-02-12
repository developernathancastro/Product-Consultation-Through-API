class ConexaoAPI():
    def verificar_token(self, token_recebido, token):
        self.token_valido = token.lower()
        self.token_usuario = token_recebido.lower()
        if self.token_valido == self.token_usuario:
            return True
        else:
            return False
