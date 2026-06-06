def formatar_moeda(valor: float) -> str:
    return f"R$ {valor:.2f}"


def titulo(texto: str) -> str:
    return (
        "\n"
        + "=" * 40
        + f"\n{texto.upper()}\n"
        + "=" * 40
    )