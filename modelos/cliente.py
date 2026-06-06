from .pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco):
        super().__init__(nome, cpf)
        self.telefone = telefone
        self.endereco = endereco
        
    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Telefone: {self.telefone}\n"
            f"Endereço: {self.endereco}"
        )