def somar(n1: int, n2: int) -> int:
    """
    Função para fazer a soma de dois números.

    Args:
        n1 (int): Recebe o primeiro número.
        n2 (int): Recebe o segundo número.

    Returns:
        Retorna a soma dos números.
    """

    return n1 + n2


def subtrair(n1: int, n2: int) -> int:
    """
    Função para fazer a subtração de dois números.

    Args:
        n1 (int): Recebe o primeiro número.
        n2 (int): Recebe o segundo número.

    Returns:
        Retorna a subtração dos números.
    """

    return n1 - n2


def multiplicar(n1: int, n2: int) -> int:
    """
    Função para fazer a multiplicação de dois números.

    Args:
        n1 (int): Recebe o primeiro número.
        n2 (int): Recebe o segundo número.

    Returns:
        Retorna a multiplicação dos números.
    """

    return n1 * n2


def dividir(n1: int, n2: int) -> float:
    """
    Função para fazer a divisão de dois números.

    Args:
        n1 (int): Recebe o primeiro número.
        n2 (int): Recebe o segundo número.

    Returns:
        Retorna a divisão dos números.
    """

    return n1 / n2


def porcentagem(numero: float, prct: float) -> float:
    """
    Função para mostrar a porcentagem de um determinado número.

    Args:
        numero (float):
            Recebe o número a ser feito a porcentagem.
        prct (float):
            Recebe a porcentagem a ser calculado.

    Returns:
        float:
            Retorna a porcentagem do número fornecido.
    """

    prct = prct / 100
    return numero * prct
