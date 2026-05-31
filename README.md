# 🎮 Jogo da Forca

Jogo da Forca em Python com menu interativo, controle de tentativas e palavras temáticas de Bleach.

---

## 📋 Sobre o Projeto

Projeto desenvolvido em Python puro como exercício de lógica de programação. O jogador tenta adivinhar uma palavra secreta letra por letra, com até 6 tentativas antes do game over. As palavras são personagens e termos do anime **Bleach**.

---

## ⚙️ Funcionalidades

- Menu interativo com opções de jogar, ver regras e sair
- Sorteio aleatório de palavra secreta
- Controle de tentativas restantes
- Registro de letras já utilizadas
- Aceita letras maiúsculas e minúsculas
- Validação de entrada no menu (não quebra ao digitar letras)

---

## 🗡️ Palavras do Jogo

As palavras são temáticas de Bleach:

`AIZEN` · `ICHIGO` · `URAHARA` · `ORIHIME` · `ZANGETSU` · `BYAKUYA` · `RUKIA` · `RENJI` · `HOLLOW` · `BANKAI` · `SEIREITEI`

---

## ▶️ Como Executar

**Pré-requisito:** Python 3.x instalado.

```bash
python forca.py
```

---

## 🕹️ Como Jogar

1. No menu, digite `1` para iniciar uma partida
2. A palavra secreta aparece oculta como `_ _ _ _ _`
3. Digite uma letra por vez
4. Letras erradas ou repetidas custam uma tentativa
5. Adivinhe a palavra completa antes de zerar as 6 tentativas

---

## 📁 Estrutura do Projeto

```
forca/
│
├── forca.py        # Código principal
└── README.md       # Este arquivo
```

---

## 📜 Regras

- Você possui **6 tentativas**
- Perde quando as tentativas chegam a zero
- Vence quando adivinha todas as letras da palavra
- Letras erradas **ou** já utilizadas custam uma tentativa

---

## 🛠️ Tecnologias

- Python 3.x
- Módulo `random` (biblioteca padrão)
