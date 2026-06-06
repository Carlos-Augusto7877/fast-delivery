class EntregaService:

    @staticmethod
    def calcular_frete_pedido(pedido) -> float:
        return pedido.calcular_frete()