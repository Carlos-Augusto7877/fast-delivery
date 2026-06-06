from modelos.pedido import Pedido


class PedidoService:

    def __init__(self):
        self._pedidos = []
        self._proximo_codigo = 1

    def criar(self, cliente, peso: float, distancia: float, tipo_entrega) -> Pedido:

        pedido = Pedido(    
            self._proximo_codigo,
            cliente,
            peso,
            distancia,
            tipo_entrega
        )

        self._pedidos.append(pedido)
        self._proximo_codigo += 1
        return pedido

    def listar(self) -> list[Pedido]:
        return self._pedidos

    def buscar_por_codigo(self, codigo: int) -> Pedido | None:
        for pedido in self._pedidos:
            if pedido.codigo == codigo:
                return pedido

        return None

    def atualizar_status(self, codigo: int, novo_status: str) -> bool:

        pedido = self.buscar_por_codigo(codigo)

        if pedido is None:
            return False

        pedido.status = novo_status

        return True