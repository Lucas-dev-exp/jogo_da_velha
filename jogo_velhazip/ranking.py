import json
import os

ARQUIVO_RANKING = "ranking.json"  # Nome do arquivo onde o ranking será salvo
ranking = {}  # Dicionário para armazenar o ranking em memória

# Função para carregar o ranking do arquivo JSON
def carregar_ranking():
    global ranking
    if os.path.exists(ARQUIVO_RANKING):
        with open(ARQUIVO_RANKING, "r") as f:
            ranking = json.load(f)  # Carrega o ranking do arquivo
    else:
        ranking = {}  # Se não existir, inicia um ranking vazio

# Função para salvar o ranking no arquivo JSON
def salvar_ranking():
    with open(ARQUIVO_RANKING, "w") as f:
        json.dump(ranking, f)  # Salva o ranking no arquivo

# Função para adicionar pontos ao ranking de um jogador
def adicionar_ranking(nome, pontos):
    carregar_ranking()  # Garante que o ranking está atualizado
    if nome in ranking:
        ranking[nome] += pontos  # Soma os pontos ao jogador existente
    else:
        ranking[nome] = pontos  # Adiciona novo jogador ao ranking
    salvar_ranking()  # Salva o ranking atualizado

# Função para exibir o ranking ordenado por pontuação
def mostrar_ranking():
    carregar_ranking()  # Garante que o ranking está atualizado
    print("\nRanking:")
    for nome, pontos in sorted(ranking.items(), key=lambda x: x[1], reverse=True):
        print(f"{nome}: {pontos}")  # Exibe nome e pontos de cada jogador