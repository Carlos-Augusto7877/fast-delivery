# services/entregador_service.py

from modelos.entregador import Entregador


class EntregadorService:

    def __init__(self):
        self._entregadores = []

    def cadastrar(
        self,
        nome: str,
        cpf: str,
        veiculo: str,
        cnh: str
    ) -> Entregador:

        entregador = Entregador(nome, cpf, veiculo, cnh)

        self._entregadores.append(
            entregador
        )

        return entregador

    def listar(self) -> list[Entregador]:
        return self._entregadores