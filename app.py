import random

NAIPES = ['♠', '♥', '♦', '♣']
VALORES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
CORINGAS = ('JOKER1', 'JOKER2') 

# Função para gerar um baralho novo
def gerar_baralho(copias=1, incluir_coringas=False, embaralhar=False):
    baralho_final = []
    for _ in range(copias):
        # Cria uma cópia base do baralho (52 cartas)
        uma_copia_deck = []
        for naipe in NAIPES:
            for valor in VALORES:
                uma_copia_deck.append(f'{valor}{naipe}')
        
        # Adiciona coringas a esta cópia do deck, se solicitado
        if incluir_coringas:
            uma_copia_deck.extend(CORINGAS) 
        
        baralho_final.extend(uma_copia_deck) 

    if embaralhar:
        random.shuffle(baralho_final)
    return baralho_final

# Função para mostrar o baralho
def mostrar_baralho(baralho):
    print(f'\nBaralho ({len(baralho)} cartas):') 
    if baralho: 
        print(', '.join(baralho))
    else:
        print("O baralho está vazio.")

# Função para distribuir cartas entre jogadores
def dar_as_cartas(baralho, num_jogadores, cartas_por_jogador):
    jogadores = {f'Jogador {i+1}': [] for i in range(num_jogadores)}
    cartas_a_dar_total = num_jogadores * cartas_por_jogador
    
    # Verifica se há cartas suficientes antes de começar a distribuir
    if len(baralho) < cartas_a_dar_total:
        print(f"Aviso: Não há cartas suficientes no baralho para dar {cartas_por_jogador} cartas a {num_jogadores} jogadores.")

    for _ in range(cartas_por_jogador): # Rodada de distribuição
        for jogador_id in jogadores: 
            if baralho: 
                jogadores[jogador_id].append(baralho.pop(0))
            else:
                print("O baralho acabou durante a distribuição.")
                return jogadores 
    return jogadores

# Função para mostrar as cartas dos jogadores
def mostrar_jogadores(jogadores):
    print('\nMão dos jogadores:')
    if not jogadores:
        print("Nenhum jogador para mostrar.")
        return
    for jogador, cartas in jogadores.items():
        print(f'{jogador} ({len(cartas)} cartas): {", ".join(cartas)}')

# Execução principal com interatividade
if __name__ == '__main__':
    print("=== Simulador de Baralho de Cartas ===")

    # Entradas do usuário com tratamento básico de erros
    while True:
        try:
            copias = int(input("Quantas cópias de baralho deseja usar (ex: 1)? "))
            if copias < 1:
                print("Por favor, insira um número positivo para cópias.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    incluir_coringas = input("Deseja incluir coringas (2 por cópia de baralho)? (s/n): ").strip().lower() == 's'
    embaralhar = input("Deseja embaralhar o baralho? (s/n): ").strip().lower() == 's'

    while True:
        try:
            num_jogadores = int(input("Quantos jogadores irão jogar (ex: 2)? "))
            if num_jogadores < 1:
                print("Por favor, insira um número positivo para jogadores.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
    
    while True:
        try:
            cartas_por_jogador = int(input(f"Quantas cartas cada um dos {num_jogadores} jogadores deve receber (ex: 5)? "))
            if cartas_por_jogador < 0: # 0 cartas é tecnicamente válido, mas talvez não desejável
                print("Por favor, insira um número não negativo para cartas por jogador.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    # Cálculo do total de cartas no baralho a ser gerado
    cartas_por_deck_base = len(VALORES) * len(NAIPES) # 52
    num_coringas_por_deck = len(CORINGAS) if incluir_coringas else 0 # 2 ou 0
    
    total_cartas_no_baralho_gerado = copias * (cartas_por_deck_base + num_coringas_por_deck)
    
    cartas_necessarias_para_distribuicao = num_jogadores * cartas_por_jogador

    if cartas_necessarias_para_distribuicao > total_cartas_no_baralho_gerado:
        print(f"Erro: Cartas insuficientes para a distribuição solicitada.")
        print(f"  Baralho teria {total_cartas_no_baralho_gerado} cartas.")
        print(f"  Necessário para distribuição: {cartas_necessarias_para_distribuicao} cartas.")
    else:
        # Geração e exibição do baralho
        baralho_principal = gerar_baralho(copias, incluir_coringas, embaralhar)
        print(f"\n--- Baralho Inicial (antes de dar as cartas) ---")
        mostrar_baralho(baralho_principal)

        # Distribuição de cartas
        maos_dos_jogadores = dar_as_cartas(baralho_principal, num_jogadores, cartas_por_jogador)

        # Exibir baralho restante
        print(f"\n--- Baralho Restante (após dar as cartas) ---")
        mostrar_baralho(baralho_principal)

        # Exibir mão dos jogadores
        mostrar_jogadores(maos_dos_jogadores)

    print("\n=== Fim da Simulação ===")
