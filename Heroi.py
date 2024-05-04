"""
1️ Desafio Classificador de nível de Herói

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões

## Objetivo

Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 5.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

#Ao final deve se exibir uma mensagem:
#"O Herói de nome **{nome}** está no nível de **{nivel}**"
"""

#Imports
import random

print(
    "Bem Vindo a Guilda dos Herois!\n"
    "Para definirmos o ranking dele aqui na guilda\n"
    "É necessario falar o nome e quanto de experiencia, ou xp, foi acumulado por este heroi!\n"
    "Entendido? Então vamos começar!\n"
      )
nome = input("Primeiro, diga o Nome do seu Heroi: ")
xp = float(input("Agora, fale quanto de XP este heroi acumulou: "))

def RakingHeroi(xp):
    if xp < 1000:
        return "Ferro"
    elif 1001 <= xp <= 2000:
        return "Bronze"
    elif 2001 <= xp <= 5000:
        return "Prata"
    elif 5001 <= xp <= 7000:
        return "Ouro"
    elif 7001 <= xp <= 8000:
        return "Platina"
    elif 8001 <= xp <= 9000:
        return "Ascendente"
    elif 9001 <= xp <= 10000:
        return "Imortal"
    else:
        return "Radiante"

print("Seu nome é ", nome,"e sua classe na guilda será ",RakingHeroi(xp))
yn = input("Você deseja ficar mais forte? Fale SIM ou NAO: ")
while yn == "SIM":
    pick = input(
        "Perfeito aonde deseja ir?\n"
        "Floresta, Caverna ou Masmorra? "  
          )
    if pick == "Floresta":
        xp = random.randint(1, 500)
        print(nome,"Voce ganhou ", xp,"de experiencia ao matar Lobos")
        yn = input("Você deseja continuar treinando? Diga SIM ou NAO: ")
    elif pick == "Caverna":
        xp = random.randint(500, 1000)
        print(nome,"Voce ganhou ", xp,"de experiencia ao matar Slimes")
        yn = input("Você deseja continuar treinando? Diga SIM ou NAO: ")
    elif pick == "Masmorra":
        xp = random.randint(1000, 1500)
        print(nome,"Voce ganhou ", xp,"de experiencia ao matar Esqueletos")
        yn = input("Você deseja continuar treinando? Diga SIM ou NAO: ")
    else:
        print("Não entendi, não me faça perder tempo!!")
if yn == "NAO":
    print(
        "Tudo bem, volte amanhã para pegar missões na guilda!!\n"
        "Ah sim, e você possui ",xp,"De experiencia e é um heroi rankin ",RakingHeroi(xp),"Continue assim e sempre de o seu melhor!!"
        )

else:
 print("Não entendi, não me faça perder tempo!!")