class EstadoJogo:
    def __init__(self, tabuleiro=None, jogador_atual='X'):
        # Inicializa o estado do jogo com o tabuleiro e o jogador atual
        self.tabuleiro = tabuleiro if tabuleiro else [' '] * 9
        self.jogador_atual = jogador_atual

    def movimentos_validos(self):
        # Retorna uma lista dos índices das casas vazias (movimentos possíveis)
        return [i for i, v in enumerate(self.tabuleiro) if v == ' ']

    def aplicar_movimento(self, index):
        # Retorna um novo EstadoJogo após aplicar o movimento na posição 'index'
        novo_tabuleiro = self.tabuleiro[:]
        novo_tabuleiro[index] = self.jogador_atual
        # Alterna o jogador para o próximo turno
        return EstadoJogo(novo_tabuleiro, 'O' if self.jogador_atual == 'X' else 'X')

    def vencedor(self):
        # Verifica todas as combinações vencedoras possíveis
        combinacoes = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for i,j,k in combinacoes:
            if self.tabuleiro[i] == self.tabuleiro[j] == self.tabuleiro[k] != ' ':
                return self.tabuleiro[i]  # Retorna 'X' ou 'O' se houver vencedor
        return None  # Retorna None se não houver vencedor

    def jogo_terminado(self):
        # Retorna True se houver vencedor ou se não houver mais casas vazias (empate)
        return self.vencedor() or ' ' not in self.tabuleiro

    def utilidade(self):
        # Retorna 10 se 'X' venceu, -10 se 'O' venceu, 0 caso contrário (empate ou jogo em andamento)
        if self.vencedor() == 'X':
            return 10
        elif self.vencedor() == 'O':
            return -10
        return 0