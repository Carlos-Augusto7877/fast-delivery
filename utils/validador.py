def ler_int(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro.")
            
def ler_float(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um número válido.")
            
def mostrar_lista(itens):
    print("")
    if not itens:
        print("Nenhum registro encontrado.")
        return

    for indice, item in enumerate(itens, start=1):
        print(f"{indice}. {item}")
        

def escolher_opcao(opcoes: list[str]) -> int:

    mostrar_lista(opcoes)
    
    while True:

        escolha = ler_int("Escolha: ")

        if 1 <= escolha <= len(opcoes):
            return escolha

        print("Opção inválida.")