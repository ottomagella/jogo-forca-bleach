import random

# ---- FUNÇÕES ----

# ---- FUNÇÃO DE INICIALIZAÇÃO DO JOGO ----
# Cria o estado inicial do jogo (tentativas, palavra e controles)
def iniciar_jogo():
    """
        Inicializa e retorna o estado inicial de uma partida do Jogo da Força.

        Seleciona aleatoriamente uma palavra secreta da lista predefinida,
        cria a representação oculta da palavra e define o número de tentativas.

        Returns:
            tuple: Uma tupla contendo:
                - tentativas (int): Número de tentativas disponíveis (6).
                - letras_digitadas (set): Conjunto vazio para registrar letras usadas.
                - palavra_secreta (str): Palavra sorteada aleatoriamente, em maiúsculo.
                - palavra_oculta (list[str]): Lista de '_' com o mesmo comprimento da palavra secreta.
    """
    tentativas = 6
    letras_digitadas = set()

    print("\n--- FORCA ---")

    palavra_aleatoria = ["AIZEN", "ICHIGO", "URAHARA", "ORIHIME", "ZANGETSU", "BYAKUYA", "RUKIA", "RENJI", "HOLLOW", "BANKAI", "SEIREITEI"] #Personagens de Bleach
    palavra_secreta = random.choice(palavra_aleatoria)
    palavra_oculta = ["_"] * len(palavra_secreta) # Cria a palavra oculta com "_" no tamanho da palavra secreta

    return tentativas, letras_digitadas, palavra_secreta, palavra_oculta

# ---- FUNÇÃO DE PROCESSAMENTO DA TENTATIVA ----
# Responsável por validar a letra e atualizar o estado do jogo
def processar_tentativa(palavra_secreta, palavra_oculta, letras_digitadas, tentativas, letra):
    """
        Processa uma tentativa do jogador, atualizando o estado do jogo.

        Normaliza a letra para maiúsculo e verifica três casos em ordem:
        letra já utilizada, letra inexistente na palavra ou letra correta.
        Nos dois primeiros casos desconta uma tentativa;
        no terceiro revela as ocorrências da letra na palavra oculta.

        Args:
            palavra_secreta (str): A palavra que o jogador deve adivinhar.
            palavra_oculta (list[str]): Estado atual da palavra, com '_' nos lugares não revelados.
            letras_digitadas (set): Conjunto de letras já utilizadas pelo jogador.
            tentativas (int): Número de tentativas restantes.
            letra (str): Letra digitada pelo jogador (maiúscula ou minúscula).

        Returns:
            tuple: Uma tupla contendo:
                - palavra_oculta (list[str]): Estado atualizado da palavra oculta.
                - letras_digitadas (set): Conjunto atualizado com a nova letra (se aplicável).
                - tentativas (int): Número de tentativas restantes após a jogada.
    """

    letra = letra.upper() # padroniza para evitar erro de maiúscula/minúscula

    if letra in letras_digitadas: # Verifica se a letra já foi usada
        tentativas -= 1
        print("Letra já utilizada XD")
    elif letra not in palavra_secreta: # Verifica se a letra não existe na palavra
        letras_digitadas.add(letra)
        tentativas -= 1
        print("A letra não existe!")
    else: # Caso a letra esteja correta, substitui "_" pela letra correta na posição correspondente
        letras_digitadas.add(letra)
        for i, letra_palavra in enumerate(palavra_secreta):
            if letra_palavra == letra:
                palavra_oculta[i] = letra

    return palavra_oculta, letras_digitadas, tentativas

# ---- JOGO ----

while True:
    print("-- JOGO DA FORCA BLEACH --")
    print("Escolha uma opção \n 1- JOGAR \n 2- REGRAS \n 3- SAIR")

    try:
        opcao = int(input("Escolha: "))
    except ValueError:
        print("Opção inválida\n")
        continue

# ---- MENU ----
# Criado para que o sistema não abra diretamente no jogo e sim de a oportunidade do jogador se preparar

    if opcao == 1: #o jogo começa

        tentativas, letras_digitadas, palavra_secreta, palavra_oculta = iniciar_jogo()

        while tentativas > 0:
            print(" ".join(palavra_oculta))
            letra = input("Digite uma letra: ")

            palavra_oculta, letras_digitadas, tentativas = processar_tentativa(palavra_secreta, palavra_oculta,letras_digitadas,tentativas,letra)

            print(f"\nTentativas restantes: {tentativas}")
            print("Letras usadas:", ",".join(letras_digitadas), "\n")

            if "_" not in palavra_oculta: # Verifica vitória
                print("--- VOCÊ VENCEU! ---\n")
                break

            if tentativas == 0: # Verifica derrota
                print("A palavra era: ",palavra_secreta)
                print("-- GAME OVER! ---\n")
                break

    elif opcao == 2:
        print("\n--- REGRAS ---")
        print("1- Você possuí 6 tentativas \n2- Você perde quando suas tentativas zeram \n3- Você vence quando adivinha toda a palavra \n4- Letras erradas ou já utilizadas fazem você perder uma tentativa\n")


    elif opcao == 3:
        print("-- SAIR DO SISTEMA --")
        print("Obrigado por jogar! :)")
        break
    else:
        print("Opção inválida")