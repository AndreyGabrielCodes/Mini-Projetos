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
letras_palavra_atual = []

import random

def main():
    global letras_restantes
    global vida
    print('JOGO DA FORCA')
    input('ENTER para iniciar o jogo')
    palavra_atual = sortear_palavra()
    while(letras_restantes != 0 or vida > 1):
        rodada(palavra_atual)
        break


def rodada(palavra):
    global vida
    for l in letras_palavra_atual:
        print(l, end=' ')
    

def verifica_letras(palavra_sorteada):
    print

def sortear_palavra():
    global palavras_jogadas
    global letras_palavra_atual
    palavra_escolhida = random.choice(lista_palavras)
    for i in lista_palavras:
        if i == palavra_escolhida:
            palavra_escolhida = random.choice(lista_palavras)
            break
    for l in palavra_escolhida:
        letras_palavra_atual.append(l)        
    return palavra_escolhida


main()