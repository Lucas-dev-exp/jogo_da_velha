import math

# Função recursiva do algoritmo minimax
def minimax(estado, profundidade, maximizador):
    # Caso base: se o jogo terminou ou atingiu a profundidade máxima, retorna utilidade do estado
    if estado.jogo_terminado() or profundidade == 0:
        return estado.utilidade()

    if maximizador:
        # Jogador maximizador (IA) tenta obter o maior valor possível
        melhor_valor = -math.inf
        for movimento in estado.movimentos_validos():
            novo_estado = estado.aplicar_movimento(movimento)
            valor = minimax(novo_estado, profundidade - 1, False)
            melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        # Jogador minimizador (humano) tenta obter o menor valor possível
        melhor_valor = math.inf
        for movimento in estado.movimentos_validos():
            novo_estado = estado.aplicar_movimento(movimento)
            valor = minimax(novo_estado, profundidade - 1, True)
            melhor_valor = min(melhor_valor, valor)
        return melhor_valor

# Função que determina a melhor jogada para a IA usando o minimax
def melhor_jogada(estado, profundidade):
    melhor_valor = -math.inf  # Inicializa o melhor valor como o menor possível
    melhor_movimento = None   # Inicializa a melhor jogada como None
    for movimento in estado.movimentos_validos():
        novo_estado = estado.aplicar_movimento(movimento)
        valor = minimax(novo_estado, profundidade - 1, False)
        if valor > melhor_valor:
            melhor_valor = valor
            melhor_movimento = movimento
    return melhor_movimento  # Retorna o índice da melhor jogada encontrada