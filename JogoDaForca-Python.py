lista_palavras = ['CASA', 'SOL', 'LUA', 'MAO', 'RIO', 'AR', 'SOL', 'MAR', 'DIA', 'BOLSA', 'LIVRO', 'CANETA', 'MESA', 'CADEIRA', 'JANELA', 'PORTA', 'FOGAO','GELADEIRA', 'COMPUTADOR','PERSEVERANCA', 'DETERMINACAO', 'CONHECIMENTO', 'CRIATIVIDADE','INTELIGENCIA', 'ESPIRITUALIDADE', 'COMUNICACAO', 'RESPONSABILIDADE', 'INDEPENDENCIA', 'LIBERDADE','CACHORRO', 'GATO', 'PASSARO', 'ELEFANTE', 'TIGRE', 'LEAO', 'MACACO','ARROZ', 'FEIJAO', 'MACARRAO', 'PIZZA', 'BOLO', 'TORTA', 'SORVETE','CABELO', 'OLHO', 'NARIZ', 'BOCA', 'MAO', 'PE', 'CORACAO']

letras_restantes = 0
vida = 6
cadastro_letras_palavra_atual = []
exibicao_letras_palavra_atual = []
nro_jogada = 0
letras_tentadas = []
retorno_jogada = 'Partida iniciada'
status_partida = 0
palavra_escolhida = ''
boneco = ['[]','']

import random
from os import system

def main():
    global letras_restantes
    global vida
    global retorno_jogada
    global palavra_escolhida
    global status_partida
    system('cls')
    print('JOGO DA FORCA')
    input('ENTER para iniciar o jogo')
    while(True):
        sortear_palavra()
        while(status_partida == 0):
            system('cls')
            print(f'Vida: {vida}\n')
            exibe_palavra()
            print(f'\n\n| {retorno_jogada}\n')
            print(palavra_escolhida)
            rodada(input('Digite uma letra: ').upper())
            status_rodada()
        system('cls')
        if status_partida == 1:
            print(f'Parabens, Você ganhou ! - Palavra sorteada: {palavra_escolhida}')
        else:
            print(f'Você perdeu ! - Palavra sorteada: {palavra_escolhida}')
        reiniciar = int(input('\nDeseja iniciar uma nova partida? (1/0)'))
        if reiniciar == 1:
            reseta_partida()
            continue
        else:
            break
            
def status_rodada():
    global letras_restantes
    global vida
    global status_partida
    if letras_restantes <= 0:
        status_partida = 1
    elif vida <= 1:
        status_partida = 2
    return status_partida

def rodada(letra):
    global vida
    global nro_jogada
    global retorno_jogada
    global letras_restantes
    indices_letra = []
    letra_valida = False
    nro_jogada += 1
    if letra in letras_tentadas:
        retorno_jogada = 'Letra já existente !'
        letra_valida = True
    else:
        for l in cadastro_letras_palavra_atual:
            if l == letra:
                retorno_jogada = 'Letra inserida !'
                letras_tentadas.append(letra)
                nro_letras_iguais = 0
                for i in cadastro_letras_palavra_atual:
                    if i == letra:
                        nro_letras_iguais += 1
                        indices_letra.append(cadastro_letras_palavra_atual.index(i))
                        indice_atual = cadastro_letras_palavra_atual.index(i)
                        cadastro_letras_palavra_atual.remove(letra)
                        cadastro_letras_palavra_atual.insert(indice_atual,'-')
                if nro_letras_iguais > 1:
                    for i in cadastro_letras_palavra_atual:
                        if i == letra:
                            indices_letra.append(cadastro_letras_palavra_atual.index(i,indices_letra[0]))
                print(indices_letra)
                for i in indices_letra:
                    exibicao_letras_palavra_atual[i] = exibicao_letras_palavra_atual[i].replace('_',str(letra))
                    letras_restantes -= 1
                letra_valida = True

    if not letra_valida:
        vida -= 1
        letras_tentadas.append(letra)
        retorno_jogada = 'Letra não existente !'
        
def exibe_palavra():
    global nro_jogada
    if nro_jogada == 0:
        for i in range(0,len(cadastro_letras_palavra_atual),1):
            exibicao_letras_palavra_atual.append('_')
    for l in exibicao_letras_palavra_atual:
        print(l, ' ', end='')

def sortear_palavra():
    global letras_palavra_atual
    global letras_restantes
    global palavra_escolhida
    palavra_escolhida = random.choice(lista_palavras)
    for i in lista_palavras:
        if i == palavra_escolhida:
            palavra_escolhida = random.choice(lista_palavras)
            break
    letras_restantes = len(palavra_escolhida)
    for l in palavra_escolhida:
        cadastro_letras_palavra_atual.append(l) 

def reseta_partida():
    global vida
    global nro_jogada
    global retorno_jogada
    global status_partida
    status_partida = 0
    cadastro_letras_palavra_atual.clear()
    exibicao_letras_palavra_atual.clear()
    letras_tentadas.clear()
    nro_jogada = 0
    vida = 6
    retorno_jogada = 'Partida iniciada'

main()