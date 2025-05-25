# 🃏 Simulador de Baralho de Cartas em Python

Este é um script Python simples que simula a criação e distribuição de cartas de um baralho. Ele permite ao usuário especificar o número de baralhos, a inclusão de coringas, se o baralho deve ser embaralhado, o número de jogadores e quantas cartas cada jogador deve receber.

#### ✨ Recursos

* Geração de um ou múltiplos baralhos padrão (52 cartas).
* Opção de incluir 2 coringas por cópia de baralho.
* Capacidade de embaralhar o baralho resultante.
* Distribuição de um número específico de cartas para múltiplos jogadores.
* Interface interativa via linha de comando para definir os parâmetros da simulação.
* Exibição do baralho inicial (antes da distribuição), das mãos dos jogadores e do baralho restante após a distribuição.
* Tratamento básico de erros para entradas do usuário.

#### 📋 Pré-requisitos

* Python 3.6 ou superior (devido ao uso de f-strings e anotações de tipo).
* Nenhuma biblioteca externa é necessária além das que vêm com o Python padrão (como `random`).

#### 🚀 Como Usar

1.  **Clone o repositório ou baixe o arquivo `app.py`**.

    Se você clonar:
    ```bash
    git clone https://github.com/Gabriel-Rosatto-Dantas/BARALHO-DE-CARTAS
    cd BARALHO-DE-CARTAS
    ```
2.  **Execute o script** a partir do seu terminal:
    ```bash
    python app.py
    ```

3.  **Siga as instruções no terminal:** O script solicitará interativamente:
    * Número de cópias do baralho.
    * Se deseja incluir coringas.
    * Se deseja embaralhar o baralho.
    * Número de jogadores.
    * Número de cartas para cada jogador.

#### 🎲 Exemplo de Interação

Ao executar o script, você verá prompts como:

=== Simulador de Baralho de Cartas ===
Quantas cópias de baralho deseja usar (ex: 1)? 1
Deseja incluir coringas (2 por cópia de baralho)? (s/n): s
Deseja embaralhar o baralho? (s/n): s
Quantos jogadores irão jogar (ex: 2)? 2
Quantas cartas cada um dos 2 jogadores deve receber (ex: 5)? 3

--- Baralho Inicial (antes de dar as cartas) ---
Baralho (54 cartas):
K♣, JOKER1, 7♥, 5♠, Q♦, A♠, 8♥, 9♣, 3♦, 10♣, 4♠, 6♣, 2♥, J♥, ... (etc.)

--- Baralho Restante (após dar as cartas) ---
Baralho (48 cartas):
8♥, 9♣, 3♦, 10♣, 4♠, 6♣, 2♥, J♥, K♥, 7♠, 8♦, 10♦, ... (etc.)

Mão dos jogadores:
Jogador 1 (3 cartas): K♣, 7♥, Q♦
Jogador 2 (3 cartas): JOKER1, 5♠, A♠

=== Fim da Simulação ===
