from .pessoa import Pessoa

class Entregador(Pessoa):
    def __init__(self, nome, cpf, veiculo, cnh):
        super().__init__(nome, cpf)
        self.veiculo = veiculo
        self.cnh = cnh
        
    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Veículo: {self.veiculo}\n"
        )