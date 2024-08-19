lista_palavras = ['CASA', 'SOL', 'LUA', 'MAO', 'RIO', 'AR', 'SOL', 'MAR', 'DIA','BOLSA', 
                  'LIVRO', 'CANETA', 'MESA', 'CADEIRA', 'JANELA', 'PORTA', 'FOGAO','GELADEIRA', 
                  'COMPUTADOR','PERSEVERANCA', 'DETERMINACAO', 'CONHECIMENTO', 'CRIATIVIDADE',
                  'INTELIGENCIA', 'ESPIRITUALIDADE', 'COMUNICACAO', 'RESPONSABILIDADE', 
                  'INDEPENDENCIA', 'LIBERDADE','CACHORRO', 'GATO', 'PASSARO', 'ELEFANTE', 
                  'TIGRE', 'LEAO', 'MACACO','ARROZ', 'FEIJAO', 'MACARRAO', 'PIZZA', 'BOLO', 
                  'TORTA', 'SORVETE','CABELO', 'OLHO', 'NARIZ', 'BOCA', 'MAO', 'PE', 'CORACAO']

letras_restantes = 0
vida = 6
palavras_jogadas = []
cadastro_letras_palavra_atual = []
exibicao_letras_palavra_atual = []
nro_jrodada = 0
letras_tentadas = []
retorno_jogada = 'Partida iniciada'

import random
from os import system

def main():
    global letras_restantes
    global vida
    global retorno_jogada
    system('cls')
    print('JOGO DA FORCA')
    input('ENTER para iniciar o jogo')
    sortear_palavra()
    while(letras_restantes != 0 or vida > 1):
        system('cls')
        exibe_palavra()
        print(f'\n\n| {retorno_jogada}\n')
        print(cadastro_letras_palavra_atual)
        rodada(input('Digite uma letra: ').upper())
        

def rodada(letra):
    global vida
    global nro_jrodada
    global retorno_jogada
    global letras_restantes
    indices_letra = []
    letra_valida = False
    nro_jrodada += 1
    for l in cadastro_letras_palavra_atual:
        if l == letra:
            if letra in letras_tentadas:
                retorno_jogada = 'Letra já existente !'
            else:
                retorno_jogada = 'Letra inserida !'
                letras_tentadas.append(letra)
                for i in cadastro_letras_palavra_atual:
                    if i == letra:
                        indices_letra.append(cadastro_letras_palavra_atual.index(letra))
                for i in indices_letra:
                    exibicao_letras_palavra_atual[i] = exibicao_letras_palavra_atual[i].replace('_',str(letra))
                    letras_restantes -= 1

            letra_valida = True

    if not letra_valida:
        vida -= 1

        
def exibe_palavra():
    global nro_jrodada
    if nro_jrodada == 0:
        for i in range(0,len(cadastro_letras_palavra_atual),1):
            exibicao_letras_palavra_atual.append('_')
    for l in exibicao_letras_palavra_atual:
        print(l, end='')

def sortear_palavra():
    global palavras_jogadas
    global letras_palavra_atual
    global letras_restantes
    palavra_escolhida = random.choice(lista_palavras)
    for i in lista_palavras:
        if i == palavra_escolhida:
            palavra_escolhida = random.choice(lista_palavras)
            break
    palavras_jogadas.append(palavra_escolhida)
    letras_restantes = len(palavra_escolhida)
    for l in palavra_escolhida:
        cadastro_letras_palavra_atual.append(l) 

main()