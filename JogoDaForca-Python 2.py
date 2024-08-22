lista_palavras = ['casa', 'apartamento', 'quarto', 'cozinha', 'sala', 'banheiro', 'janela', 'porta', 'sofa', 'cama', 'mesa', 'cadeira', 'armario', 'geladeira', 'fogao', 'televisao', 'computador','smartphone', 'aplicativo', 'internet', 'wifi', 'algoritmo', 'software', 'hardware', 'nuvem', 'pixel', 'bot','receita', 'ingrediente', 'cozinhar', 'assado', 'frito', 'doce', 'salgado', 'temperos', 'gourmet', 'chef','passaporte', 'mala', 'aviao', 'hotel', 'turismo', 'roteiro', 'paisagem', 'cultura', 'salsicao', 'aventura','futebol', 'basquete', 'volei', 'natacao', 'ginastica', 'atleta', 'torcida', 'estadio', 'olimpiadas', 'medalha']
boneco = ['  [',' ]','\n /',' |',' \\','\n  /',' \\']
obj_rodada = {'letras_restantes': 0, 'vida': 7, 'nro_jogada': 0, 'letras_tentadas': [], 'status_partida': 0, 'palavra_escolhida': '', 'retorno_jogada':'Partida iniciada'}
obj_palavra = {'cadastro_letras_palavra_atual':[],'exibicao_letras_palavra_atual':[]}

import random
from os import system

def main():
    while(True):
        modo = 0
        while(modo not in ('1','2')):
            system('cls')
            print('   JOGO DA FORCA\n       MODOS\n1 - Letra aleatória\n2 - Letra escolhida\n')
            modo = input('Deseja jogar em qual modo ? ')
            if modo == '1':
                palavra_rodada(1)
            elif modo == '2':
                palavra_rodada(2,input('Digite a palavra que deseja: ').upper())
        while(obj_rodada['status_partida'] == 0):
            system('cls')
            menu()
            print(obj_rodada['palavra_escolhida']) #teste
            rodada(input('Digite uma letra: ').upper())
            status_rodada()
        system('cls')
        reiniciar = 2
        while(reiniciar not in ('1','0')):
            system('cls')
            if obj_rodada['status_partida'] == 1:
                print('Parabens, Você ganhou ! - Palavra: ' + obj_rodada['palavra_escolhida'])
            else:
                print('Você perdeu ! - Palavra: ' + obj_rodada['palavra_escolhida'])
            reiniciar = input('\nDeseja iniciar uma nova partida? (1/0)')
        if reiniciar == '1':
            reseta_partida()
            continue
        else:
            break
            
def status_rodada():
    if obj_rodada['letras_restantes'] <= 0:
        obj_rodada['status_partida'] = 1
    elif obj_rodada['vida'] == 0:
        obj_rodada['status_partida'] = 2
    return obj_rodada['status_partida']

def rodada(letra):
    indices_letra = []
    letra_valida = False
    obj_rodada['nro_jogada'] += 1
    if letra == obj_rodada['palavra_escolhida']:
        obj_rodada['status_partida'] = 1
    elif len(letra) > 1 or (letra.isalpha()) == False:
        obj_rodada['retorno_jogada'] = 'Valor invalido !'
        letra_valida = True
    elif (letra.isalpha())== True:
        if letra in obj_rodada['letras_tentadas']:
            obj_rodada['retorno_jogada'] = 'Letra já existente !'
            letra_valida = True
        else:
            for l in obj_palavra['cadastro_letras_palavra_atual']:
                if l == letra:
                    obj_rodada['retorno_jogada'] = 'Letra inserida !'
                    obj_rodada['letras_tentadas'].append(letra)
                    nro_letras_iguais = 0
                    for i in obj_palavra['cadastro_letras_palavra_atual']:
                        if i == letra:
                            nro_letras_iguais += 1
                            indices_letra.append(obj_palavra['cadastro_letras_palavra_atual'].index(i))
                            indice_atual = obj_palavra['cadastro_letras_palavra_atual'].index(i)
                            obj_palavra['cadastro_letras_palavra_atual'].remove(letra)
                            obj_palavra['cadastro_letras_palavra_atual'].insert(indice_atual,'-')
                    if nro_letras_iguais > 1:
                        for i in obj_palavra['cadastro_letras_palavra_atual']:
                            if i == letra:
                                indices_letra.append(obj_palavra['cadastro_letras_palavra_atual'].index(i,indices_letra[0]))
                    print(indices_letra)
                    for i in indices_letra:
                        obj_palavra['exibicao_letras_palavra_atual'][i] = obj_palavra['exibicao_letras_palavra_atual'][i].replace('_',str(letra))
                        obj_rodada['letras_restantes'] -= 1
                    letra_valida = True
        if not letra_valida:
            obj_rodada['vida'] -= 1
            boneco.pop(-1)
            if letra not in obj_rodada['letras_tentadas']:
                obj_rodada['letras_tentadas'].append(letra)
            obj_rodada['retorno_jogada'] = 'Letra não existente !'

def menu():
    #boneco
    for b in boneco: 
        print(b, end='')
    print(' \n')
    #palavra
    if obj_rodada['nro_jogada'] == 0: 
        for i in range(0,len(obj_palavra['cadastro_letras_palavra_atual']),1):
            obj_palavra['exibicao_letras_palavra_atual'].append('_')
    for l in obj_palavra['exibicao_letras_palavra_atual']:
        print(l, ' ', end='')
    #retorno da jogada
    print(f'\n\n| ' + obj_rodada['retorno_jogada']) 
    #vida
    print(f'| Vida: ' + str(obj_rodada['vida']))
    #letras tentadas
    print('| Letras tentadas: ', end='') 
    for i in obj_rodada['letras_tentadas']:
        print(i, end=' ')
    print('\n')

def palavra_rodada(modo, palavra = ''):
    if modo == 1:
        obj_rodada['palavra_escolhida'] = random.choice(lista_palavras).upper()
        for i in lista_palavras:
            if i == obj_rodada['palavra_escolhida']:
                obj_rodada['palavra_escolhida'] = random.choice(lista_palavras).upper()
                break
    else:
        obj_rodada['palavra_escolhida'] = palavra
    obj_rodada['letras_restantes'] = len(obj_rodada['palavra_escolhida'])
    for l in obj_rodada['palavra_escolhida']:
        obj_palavra['cadastro_letras_palavra_atual'].append(l) 

def reseta_partida():
    global obj_rodada
    global obj_palavra
    obj_rodada = {'letras_restantes': 0, 'vida': 7, 'nro_jogada': 0, 'letras_tentadas': [], 'status_partida': 0, 'palavra_escolhida': '', 'retorno_jogada':'Partida iniciada'}
    obj_palavra = {'cadastro_letras_palavra_atual':[],'exibicao_letras_palavra_atual':[]}

main()