# -*- coding: utf-8 -*-
"""
Jogo de Pedra, Papel e Tesoura
Criado em Junho de 2026

@author: Hudson
"""

import random


def obter_entrada_valida():
    """
    Obtém uma entrada válida do usuário.
    Retorna a escolha em minúsculas.
    """
    movimentos_validos = ["pedra", "papel", "tesoura"]
    
    while True:
        entrada = input("O que você quer jogar? (pedra, papel ou tesoura): ").lower().strip()
        
        if entrada in movimentos_validos:
            return entrada
        else:
            print("❌ Entrada inválida! Digite: pedra, papel ou tesoura\n")


def obter_escolha_pc():
    """
    Gera uma escolha aleatória para o computador.
    """
    movimentos = ["pedra", "papel", "tesoura"]
    return random.choice(movimentos)


def determinar_vencedor(usuario, pc):
    """
    Compara as escolhas e determina o vencedor da rodada.
    Retorna: 1 (usuário vence), -1 (pc vence), 0 (empate)
    """
    if usuario == pc:
        return 0
    
    vitorias = {
        "pedra": "tesoura",
        "papel": "pedra",
        "tesoura": "papel"
    }
    
    if vitorias[usuario] == pc:
        return 1
    else:
        return -1


def exibir_resultado_rodada(usuario, pc, resultado):
    """
    Exibe o resultado da rodada atual.
    """
    print(f"Você escolheu: {usuario}")
    print(f"PC escolheu: {pc}")
    
    if resultado == 1:
        print("✅ Você ganhou esta rodada!\n")
    elif resultado == -1:
        print("❌ Você perdeu esta rodada!\n")
    else:
        print("🤝 Empate!\n")


def exibir_placar(usuario_pontos, pc_pontos, rodada_atual):
    """
    Exibe o placar atual do jogo.
    """
    print(f"{'='*40}")
    print(f"📊 PLACAR - Rodada {rodada_atual}")
    print(f"{'='*40}")
    print(f"Você:  {usuario_pontos} ponto(s)")
    print(f"PC:    {pc_pontos} ponto(s)")
    print(f"{'='*40}\n")


def exibir_resultado_final(usuario_pontos, pc_pontos, total_rodadas):
    """
    Exibe o resultado final do jogo.
    """
    print(f"\n{'='*40}")
    print(f"🏁 FIM DE JOGO")
    print(f"{'='*40}")
    print(f"Total de rodadas: {total_rodadas}")
    print(f"Você:  {usuario_pontos} ponto(s)")
    print(f"PC:    {pc_pontos} ponto(s)")
    
    if usuario_pontos > pc_pontos:
        print(f"\n🎉 Parabéns! Você venceu com {usuario_pontos - pc_pontos} ponto(s) de diferença!")
    elif pc_pontos > usuario_pontos:
        print(f"\n🤖 O PC venceu com {pc_pontos - usuario_pontos} ponto(s) de diferença!")
    else:
        print(f"\n🤝 Resultado final: EMPATE!")
    print(f"{'='*40}\n")


def escolher_modo_jogo():
    """
    Permite o usuário escolher o modo de jogo.
    Retorna o número de rodadas desejadas, ou 0 para modo infinito.
    """
    print("\n" + "="*40)
    print("🎮 BEM-VINDO AO JOGO DE PEDRA, PAPEL E TESOURA!")
    print("="*40 + "\n")
    
    print("Escolha o modo de jogo:")
    print("1 - Melhor de 3 (até 2 vitórias)")
    print("2 - Melhor de 5 (até 3 vitórias)")
    print("3 - Modo infinito (continue quantas vezes quiser)")
    
    while True:
        opcao = input("\nDigite sua escolha (1, 2 ou 3): ").strip()
        
        if opcao == "1":
            return 2
        elif opcao == "2":
            return 3
        elif opcao == "3":
            return 0
        else:
            print("❌ Opção inválida! Digite 1, 2 ou 3.\n")


def jogar():
    """
    Função principal do jogo.
    """
    limite_rodadas = escolher_modo_jogo()
    
    usuario_pontos = 0
    pc_pontos = 0
    rodada_atual = 1
    
    while True:
        print(f"\n{'='*40}")
        print(f"🎯 RODADA {rodada_atual}")
        print(f"{'='*40}\n")
        
        # Obtém entrada do usuário
        escolha_usuario = obter_entrada_valida()
        
        # PC faz sua escolha
        escolha_pc = obter_escolha_pc()
        
        # Determina vencedor
        resultado = determinar_vencedor(escolha_usuario, escolha_pc)
        
        # Exibe resultado da rodada
        exibir_resultado_rodada(escolha_usuario, escolha_pc, resultado)
        
        # Atualiza pontuação
        if resultado == 1:
            usuario_pontos += 1
        elif resultado == -1:
            pc_pontos += 1
        
        # Exibe placar
        exibir_placar(usuario_pontos, pc_pontos, rodada_atual)
        
        # Verifica se atingiu o limite (melhor de X)
        if limite_rodadas > 0:
            if usuario_pontos > limite_rodadas - 1 or pc_pontos > limite_rodadas - 1:
                exibir_resultado_final(usuario_pontos, pc_pontos, rodada_atual)
                break
        
        # Pergunta se quer continuar (apenas no modo infinito)
        if limite_rodadas == 0:
            continuar = input("Deseja jogar outra rodada? (s/n): ").lower().strip()
            if continuar != 's':
                exibir_resultado_final(usuario_pontos, pc_pontos, rodada_atual)
                break
        
        rodada_atual += 1


if __name__ == "__main__":
    jogar()
