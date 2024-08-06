class Usuario:
    def __init__(self,nome,email,senha):
        self.nome=nome
        self.email=email
        self.senha=senha
    def setNome(self):
        return(f"nome:{self.nome}")
    def setEmail(self):
        return(f"email:{self.email}")
    def setSenha(self):
        return(f"senha:{self.senha}")
    def arquivousuario(self):
        usuarios={
            "Nome":self.nome,
            "Email":self.email,
            "Senha":self.senha
        }

        
        return usuarios

