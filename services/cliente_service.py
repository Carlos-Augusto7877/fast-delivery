from modelos.cliente import Cliente


class ClienteService:

    def __init__(self):
        self._clientes = []

    def cadastrar( self, nome: str, cpf: str, telefone: str, endereco: str) -> Cliente:

        cliente = Cliente(
            nome,
            cpf,
            telefone,
            endereco
        )

        self._clientes.append(cliente)

        return cliente

    def listar(self) -> list[Cliente]:
        return self._clientes

    def buscar_por_cpf(self, cpf: str) -> Cliente | None:

        for cliente in self._clientes:
            if cliente.cpf == cpf:
                return cliente

        return None