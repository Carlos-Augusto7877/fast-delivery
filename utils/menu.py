# menu.py

from .validador import escolher_opcao
from .formatador import titulo


def menu_principal():

    print(titulo("Fast Delivery"))

    return escolher_opcao([
        "Clientes",
        "Entregadores",
        "Pedidos",
        "Sair"
    ])


def menu_clientes():

    print(titulo("Clientes"))

    return escolher_opcao([
        "Cadastrar cliente",
        "Listar clientes",
        "Voltar"
    ])
    
def menu_entregadores():
    print(titulo("Entregadores"))
    
    return escolher_opcao([
        "Cadastrar Entregador",
        "Listar Entregadores",
        "voltar"
    ])
    
def menu_pedidos():
    print(titulo("Pedidos"))
    
    return escolher_opcao([
        "Criar Pedido",
        "Listar Pedidos",
        "Atualizar Status",
        "Voltar"
    ])