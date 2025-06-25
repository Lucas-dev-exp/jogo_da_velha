from estado_jogo import EstadoJogo
from minimax import melhor_jogada
from ranking import adicionar_ranking, mostrar_ranking

# Função para imprimir o tabuleiro de forma amigável
def imprimir_tabuleiro(tab):
    for i in range(0, 9, 3):
        linha = []
        for j in range(3):
            idx = i + j
            if tab[idx] == ' ':
                linha.append(str(idx))  # Mostra o índice se a posição estiver vazia
            else:
                linha.append(tab[idx])  # Mostra X ou O
        print(linha[0] + "|" + linha[1] + "|" + linha[2])
        if i < 6:
            print("-+-+-")  # Linha separadora

# Função principal para jogar uma partida
def jogar(nome_usuario):
    estado = EstadoJogo()  # Cria um novo estado de jogo
    nivel = input("Escolha o nível (fácil=1, médio=3, difícil=5): ")
    profundidade = int(nivel)  # Define a profundidade do algoritmo minimax

    while not estado.jogo_terminado():
        imprimir_tabuleiro(estado.tabuleiro)
        print()  # Linha em branco para separar os tabuleiros
        if estado.jogador_atual == 'X':
            # IA faz sua jogada usando o minimax
            movimento = melhor_jogada(estado, profundidade)
        else:
            # Jogador humano faz sua jogada
            movimento = int(input("Sua jogada (0-8): "))
            while estado.tabuleiro[movimento] != ' ':
                movimento = int(input("Posição inválida, tente novamente: "))

        estado = estado.aplicar_movimento(movimento)  # Atualiza o estado do jogo

    imprimir_tabuleiro(estado.tabuleiro)
    vencedor = estado.vencedor()  # Verifica quem venceu

    # Atualiza o ranking de acordo com o resultado
    if vencedor == 'X':
        print("IA venceu!")
        adicionar_ranking("IA", 10)
        adicionar_ranking(nome_usuario, 0)
    elif vencedor == 'O':
        print(f"{nome_usuario} venceu!")
        adicionar_ranking(nome_usuario, 10)
        adicionar_ranking("IA", 0)
    else:
        print("Empate!")
        adicionar_ranking(nome_usuario, 5)
        adicionar_ranking("IA", 5)

    mostrar_ranking()  # Exibe o ranking atualizado

# Menu principal do jogo
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1 - Jogar")
        print("2 - Consultar ranking")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            nome_usuario = input("Digite seu nome: ")
            while True:
                jogar(nome_usuario)
                resposta = input("Jogar novamente com o mesmo jogador? (s/n): ").strip().lower()
                if resposta != 's':
                    break
        elif opcao == '2':
            mostrar_ranking()  # Mostra o ranking sem jogar
        elif opcao == '3':
            print("Obrigado por jogar!")
            break  # Sai do loop e encerra o programa
        else:
            print("Opção inválida. Tente novamente.")