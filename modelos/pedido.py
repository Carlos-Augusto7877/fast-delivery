from .cliente import Cliente
from .entrega import Entrega
from utils.formatador import formatar_moeda

class Pedido:
    
    STATUS_VALIDOS = {
        "Em preparação",
        "Saiu para entrega",
        "Entregue",
        "Cancelado"
    }
    
    def __init__(self, codigo, cliente: Cliente, peso, distancia, tipo_entrega: Entrega):
        if peso < 0 or distancia < 0:
            raise ValueError("Valor inválido")
        
        self.codigo = codigo
        self.cliente: Cliente = cliente
        self.peso = peso
        self.distancia = distancia
        self.tipo_entrega: Entrega = tipo_entrega
        self.__status = "Em preparação"
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, novo_status):
        
        if novo_status not in self.STATUS_VALIDOS:
            raise ValueError("Status inválido")
        
        self.__status = novo_status
    
    @property
    def valor_frete(self) -> float:
        return self.tipo_entrega.calcular_frete(self.distancia)    
    
    def __str__(self):
        return (
            f"Código: {self.codigo}\n"
            f"Cliente: {self.cliente.nome}\n"
            f"Peso: {self.peso} kg\n"
            f"Distância: {self.distancia} km\n"
            f"Status: {self.__status}\n"
            f"Frete: {formatar_moeda(self.valor_frete)}"
        )
        
