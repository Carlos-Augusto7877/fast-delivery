from modelos.entrega import (
    EntregaComum,
    EntregaExpressa,
    EntregaPremium
)

from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from services.entregadores_service import EntregadorService

from utils.menu import (
    menu_principal,
    menu_clientes,
    menu_entregadores,
    menu_pedidos
)

from utils.validador import (
    ler_float,
    mostrar_lista
)


cliente_service = ClienteService()
pedido_service = PedidoService()
entregador_service = EntregadorService()


def gerenciar_clientes():

    while True:

        opcao = menu_clientes()

        match opcao:

            case 1:
                print("\nCadastro de Cliente: ")
                
                nome = input("Nome: ")
                cpf = input("CPF: ")
                telefone = input("Telefone: ")
                endereco = input("Endereço: ")

                cliente_service.cadastrar(
                    nome,
                    cpf,
                    telefone,
                    endereco
                )

                print("Cliente cadastrado.")

            case 2:
                print("\nListagem de clientes: ")
                mostrar_lista(
                    cliente_service.listar()
                )

            case 3:
                break


def gerenciar_pedidos():

    while True:

        opcao = menu_pedidos()

        match opcao:

            case 1:
                print("\nCriar pedido: ")
                cpf = input(
                    "CPF do cliente: "
                )

                cliente = (
                    cliente_service
                    .buscar_por_cpf(cpf)
                )

                if cliente is None:
                    print(
                        "Cliente não encontrado."
                    )
                    continue

                peso = ler_float(
                    "Peso (kg): "
                )

                distancia = ler_float(
                    "Distância (km): "
                )

                print("\nTipo de entrega")
                print("1 - Comum")
                print("2 - Expressa")
                print("3 - Premium")

                tipo = int(
                    input("Escolha: ")
                )

                match tipo:

                    case 1:
                        entrega = EntregaComum()

                    case 2:
                        entrega = EntregaExpressa()

                    case 3:
                        entrega = EntregaPremium()

                    case _:
                        print(
                            "Tipo inválido."
                        )
                        continue

                pedido = pedido_service.criar(
                    cliente,
                    peso,
                    distancia,
                    entrega
                )

                print(f"\nPedido criado: ")
                print(pedido)

            case 2:
                print("\nListagem de pedidos:")
                mostrar_lista(
                    pedido_service.listar()
                )

            case 3:

                print("\nAtualização de status do pedido: ")
                codigo = int(
                    input(
                        "Código do pedido: "
                    )
                )

                novo_status = input(
                    "Novo status: "
                )

                sucesso = (
                    pedido_service
                    .atualizar_status(
                        codigo,
                        novo_status
                    )
                )

                if sucesso:
                    print(
                        "\nStatus atualizado."
                    )
                else:
                    print(
                        "\nPedido não encontrado."
                    )

            case 4:
                break


def gerenciar_entregadores():
    while True:

        opcao = menu_entregadores()

        match opcao:

            case 1:
                print("\nCadastro de Entregador: ")
                
                nome = input("Nome: ")
                cpf = input("CPF: ")
                veiculo = input("Veículo: ")
                cnh = input("CNH: ")
                
                entregador_service.cadastrar(
                    nome,
                    cpf,
                    veiculo,
                    cnh
                )
                
                print("Entregador Cadastrado.\n")

            case 2:
                print("\nListagem de entregadores: \n")
                mostrar_lista(entregador_service.listar())
                print("")
                
            case 3:
                break


def main():

    while True:

        opcao = menu_principal()

        match opcao:

            case 1:
                gerenciar_clientes()

            case 2:
                gerenciar_entregadores()

            case 3:
                gerenciar_pedidos()

            case 4:
                print("Encerrando...")
                break


if __name__ == "__main__":
    main()