# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:32:27 2026

@author: Hudson
"""

import random
print("Bem vindo ao Jogo de Pedra, Papel e Tesoura!")
compScore = 0
userScore = 0
while True:
  move = input("O que você quer jogar? pedra, papel ou tesoura?")
  print("Você escolheu", move)
  allMoves = ["pedra", "papel", "tesoura"]
  compMove = random.choice(allMoves)
  print("O PC escolheu", compMove)
  if move.lower() == compMove:
    print("EMPATE!")
  elif move.lower() == 'pedra':
    if compMove == 'tesoura':
      print("You won! Você ganhou!")
      userScore += 1
    else:
        print("You lost! Você perdeu!")
        compScore += 1
  elif move.lower() == 'papel':
    if compMove == 'pedra':
      print("You won! Você ganhou!")
      userScore += 1
    else:
        print("You lost! Você perdeu!")
        compScore += 1
  elif move.lower() == 'tesoura':
    if compMove == 'papel':
      print("You won! Você ganhou!")
      userScore += 1
    else:
        print("You lost! Você perdeu!")
        compScore += 1
  print("Placar")
  print(f"Voce {userScore}")
  print(f"PC {compScore}")
  continue2 = input("Quer continuar? s ou n")
  if continue2.lower() == 'n':
    break
