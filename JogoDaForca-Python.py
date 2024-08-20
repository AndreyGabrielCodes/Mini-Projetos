lista_palavras = ['casa', 'apartamento', 'quarto', 'cozinha', 'sala', 'banheiro', 'janela', 'porta', 'sofa', 'cama', 'mesa', 'cadeira', 'armario', 'geladeira', 'fogao', 'televisao', 'computador','smartphone', 'aplicativo', 'internet', 'wifi', 'algoritmo', 'software', 'hardware', 'nuvem', 'pixel', 'bot','receita', 'ingrediente', 'cozinhar', 'assado', 'frito', 'doce', 'salgado', 'temperos', 'gourmet', 'chef','passaporte', 'mala', 'aviao', 'hotel', 'turismo', 'roteiro', 'paisagem', 'cultura', 'salsicao', 'aventura','futebol', 'basquete', 'volei', 'natacao', 'ginastica', 'atleta', 'torcida', 'estadio', 'olimpiadas', 'medalha']
letras_restantes = 0
vida = 7
cadastro_letras_palavra_atual = []
exibicao_letras_palavra_atual = []
nro_jogada = 0
letras_tentadas = []
retorno_jogada = 'Partida iniciada'
status_partida = 0
palavra_escolhida = ''
boneco = ['  [',' ]','\n /',' |',' \\','\n  /',' \\']

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
            exibe_boneco()
            exibe_palavra()
            print(f'\n\n| {retorno_jogada}')
            print(f'| Vida: {vida}')
            exibe_letras_tentadas()
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
    elif vida == 0:
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
        boneco.pop(-1)
        if letra not in letras_tentadas:
            letras_tentadas.append(letra)
        retorno_jogada = 'Letra não existente !'
        
def exibe_palavra():
    global nro_jogada
    if nro_jogada == 0:
        for i in range(0,len(cadastro_letras_palavra_atual),1):
            exibicao_letras_palavra_atual.append('_')
    for l in exibicao_letras_palavra_atual:
        print(l, ' ', end='')

def exibe_letras_tentadas():
    print('| Letras tentadas: ', end='')
    for i in letras_tentadas:
        print(i, end=' ')
    print('\n')
    
def exibe_boneco():
    global vida
    for b in boneco:
        print(b, end='')
    print('\n')

def sortear_palavra():
    global letras_palavra_atual
    global letras_restantes
    global palavra_escolhida
    palavra_escolhida = random.choice(lista_palavras).upper()
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
    vida = 7
    retorno_jogada = 'Partida iniciada'

main()