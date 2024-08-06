class Produto:
    def __init__(self,marca,expecificacao,modelo):
        self.marca=marca
        self.expecificacao=expecificacao
        self.modelo=modelo
    def setMarca(self):
        return(f"marca:{self.marca}")
    def setExpecificacao(self):
        return(f"expecificacao:{self.expecificacao}")
    def setModelo(self):
        return(f"modelo:{self.modelo}")
    def estoqueprodutos(self):
        produtos={
            "Marca":self.marca,
            "Expecificação":self.expecificacao,
            "Modelo":self.modelo
        }

    
        return produtos

