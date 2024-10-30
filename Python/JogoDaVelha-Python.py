def valida_per(text_per, tipo, min=0, max=0):
    """
    Função para validar a entrada do usuário com tipo e intervalo definidos.

    - tipo: define se a entrada é texto (str) ou número (int ou float).
    - minimo e maximo: definem o intervalo para valores numéricos (opcional).
    """
    while True:
        try:
            if tipo in (int, float):
                resposta = float(input(text_per))
                if min <= resposta <= max:
                    return int(resposta)
                else:
                    system('cls')
                    menu()
                    print(f'*Linha ou coluna fora do intervalo existente!\n')
            elif tipo == str:
                resposta = input(text_per)
                if len(resposta) >= 1:
                    return resposta
                else:
                    system('cls')
                    print('*Tipo de valor inválido')
            elif tipo == 'menu':
                resposta = float(input(text_per))
                if min <= resposta <= max:
                    return int(resposta)
                else:
                    print(f'*Valor fora do intervalo: {min} a {max}')
            else:
                system('cls')
                menu()
                raise TypeError('*Tipo de valor inválido')
        except ValueError:
            print('*Tipo de valor inválido')              

def pc_turno():
    while(True):
        global pc_id_alea_comb_jog
        global pc_comb_atual
        #cadastro de preenchimento das posições da combinação escolhida pelo computador
        lista_ocupa_pos_comb_atual = [
            {'id':1,'id_pos':0,'ocupada':0},
            {'id':2,'id_pos':0,'ocupada':0},
            {'id':3,'id_pos':0,'ocupada':0}]
        #computador primeiro verifica se está proximo de completar uma combinação caso não esteja
        # verifica se o jogador está proximo de completar uma combinação e o bloqueia
        duas_pos_pc_comb = pc_comb()
        if not duas_pos_pc_comb:
            bloq = pc_bloq_jog()
            if (bloq == True):
                break
        #gera combinações possíveis
        pc_comb()
        lista_comb_possiveis.clear()
        for comb in lista_pc_comb:
            if (comb['valido'] == 1):
                lista_comb_possiveis.append(comb['id'])
        #caso todas as combinações estejam indisponíveis
        # altera para o computador jogador aleatoriamente
        if (lista_comb_possiveis == []):
            pc_comb_atual = 0
            #lista todas as posições disponíveis para o modo aleatório
            lista_pos_val_modo_alea.clear()
            for posicao in lista_todas_posicoes:
                if(posicao['simbolo'] == ' '):
                    lista_pos_val_modo_alea.append(posicao['id'])
            #escolhe aleatoriamente uma das posições e joga
            posicao_escolhida = 0
            posicao_escolhida = random.choice(lista_pos_val_modo_alea)
            for posicao in lista_todas_posicoes:
                if (posicao['id'] == posicao_escolhida):
                    posicao['simbolo'] = 'O'
            break
        else:
            #caso o computador já tenha escolhido uma combinação
            # não é aleatorizado uma nova
            if (pc_comb_atual == 0):
                pc_comb_atual = random.choice(lista_comb_possiveis)
        #estrutura de escolha da posição de jogada do computador
        if ((pc_comb_atual != 0)):
            #adiciona os ids das posicoes da combinação escolhida a uma lista de posicoes
            for comb in lista_pc_comb:
                if (comb['id'] == pc_comb_atual):
                    lista_pc_ids_comb_esc = (comb['pos_comb'])
            #adiciona os ids das posicoes a um cadastro de preenchimento delas
            id_pos = 0
            for pos in lista_ocupa_pos_comb_atual:
                if (pos['ocupada'] == 0):
                    pos['id_pos'] = lista_pc_ids_comb_esc[id_pos]
                id_pos +=1
            #Verifica se o id da posicao escolhida está ocupado por ele mesmo 
            # caso esteja o retira das posicoes para jogar da combinação escolhida
            for pos in lista_ocupa_pos_comb_atual:
                for posicao in lista_todas_posicoes:
                    if (pos['id_pos'] == posicao['id']):
                        if (posicao['simbolo'] == 'O'):
                            pos['ocupada'] = 1
            #verifica os ids a jogar possiveis e aleatoriza um para jogar
            lista_id_alea_comb_jog = []
            for pos in lista_ocupa_pos_comb_atual:
                if (pos['ocupada'] == 0):
                    lista_id_alea_comb_jog.append(pos['id_pos'])
            if (lista_id_alea_comb_jog != []):
                pc_id_alea_comb_jog = random.choice(lista_id_alea_comb_jog)
            #verifica se combinação escolhida ainda é válida
            comb_valida = ''
            for id_pos in lista_pc_ids_comb_esc:
                for posicao in lista_todas_posicoes:
                    if (posicao['id'] == id_pos):
                        comb_valida += posicao['simbolo']
            #caso a combinação não possua uma posicao ocupada por si próprio
            # troca para o modo aleatório
            if (comb_valida not in ('O  ',' O ','  O','O O','OO ',' OO','   ')):
                pc_comb_atual = 0
            else:
                #altera o status ocupada do id da combinação a jogar
                # depois parte para preencher
                for pos in lista_ocupa_pos_comb_atual:
                    if (pos['id_pos'] == pc_id_alea_comb_jog):
                        pos['ocupada'] = 1
                        for posicao in lista_todas_posicoes:
                            if (posicao['id'] == pc_id_alea_comb_jog):
                                posicao['simbolo'] = 'O'
                break

def pc_bloq_jog():
    global num_jog_comp
    bloq_feito = False
    num_jogadas_x = 0
    id_pri_pos_jog = 0
    id_ret_pri_pos = 0 #retorno para a primeira posição
    for pos in lista_todas_posicoes:
        if (pos['simbolo'] == 'X'):
            num_jogadas_x +=1
        if (num_jogadas_x == 1):
            id_pri_pos_jog = pos['id']
    #retorno de posições predefinidas a partir da posição inicial do jogador
    if (num_jogadas_x == 1 and num_jog_comp == 0):
        lista_pri_id_jog = [{'pos':[1,3,7,9],'ret':5},{'pos':[2],'ret':8},{'pos':[8],'ret':2},
                            {'pos':[4],'ret':6},{'pos':[6],'ret':4},{'pos':[5],'ret':7}]
        for ids in lista_pri_id_jog: #verifica na lista de retorno o id inicial
            if (id_pri_pos_jog in ids['pos']):
                id_ret_pri_pos = ids['ret']
        for pos in lista_todas_posicoes: #insere o retorno conforme a lista
            if(pos['id'] == id_ret_pri_pos):
                pos['simbolo'] = 'O'
        bloq_feito = True
    #bloqueia com base na criação de uma lista de pares de posições jogadas pelo jogador
    elif (num_jogadas_x >= 2):
        #cria uma lista com de todas as combinações possíveis com as posições ocupadas por X
        lista_todas_comb = []
        for pos in lista_todas_posicoes:
            if (pos['simbolo'] == 'X'):
                lista_duas_pos = []
                lista_duas_pos_invert = [] #inverte a lista, então [1,2] = [2,1]
                for i in range(1,10,1):
                    for j in lista_todas_posicoes: #retira os ids que não sejam iguais a X
                        if (j['id'] == i):
                            if (j['simbolo'] == 'X'):
                                if (pos['id'] != i):
                                    lista_duas_pos = [pos['id'],i]
                                    lista_duas_pos_invert = [i,pos['id']]
                                    #retira as combinações duplicadas
                                    if (lista_duas_pos not in lista_todas_comb):
                                        lista_todas_comb.append(lista_duas_pos)
                                    if (lista_duas_pos_invert not in lista_todas_comb):
                                        lista_todas_comb.append(lista_duas_pos_invert)
        if (len(lista_todas_comb) >= 1):
            #verifica se pares criados estão dentro da lista de retorno
            for comb in lista_todas_comb:
                if not (bloq_feito):
                    for id_ret in lista_retorno_pc_comb_jog:       
                        if((id_ret['id'] == comb) and (id_ret['bloq'] == 0)):
                            #quando encontra, insere o bloqueio
                            for pos in lista_todas_posicoes:
                                if(pos['id'] == id_ret['ret'] and pos['simbolo'] == ' '):
                                    pos['simbolo'] = 'O'
                                    id_ret['bloq'] = 1
                                    bloq_feito = True
    return bloq_feito

def pc_comb():
    #limpa combinações possíveis anteriores
    for comb in lista_pc_comb:
        comb['comb'] = ''
        comb['valido'] = 0
    #verifica cada "pos_comb" de "lista_pc_comb" e atribui o simbolo
    # de cada id de posicao de "lista_todas_posicoes"
    for comb in lista_pc_comb:
        pos_comb = comb['pos_comb']
        for posicao in lista_todas_posicoes:
            if(posicao['id'] in pos_comb):
                comb['comb'] += posicao['simbolo']
    #computador considera primeiro as combinações que já ocupou
    #verifica combinações em que o PC já tenha ocupado duas posicões
    comb_ocup_dois = False
    for comb in lista_pc_comb:
        if(comb['comb'] in ('O O','OO ',' OO')):
            comb['valido'] = 1
            comb_ocup_dois = True
    #verifica combinações em que o PC já tenha ocupado uma posicão
    comb_ocup_um = False
    if (comb_ocup_dois == False):
        for comb in lista_pc_comb:
            if(comb['comb'] in ('O  ',' O ','  O')):
                comb['valido'] = 1
                comb_ocup_um = True
    #verifica combinações em que o PC não tenha ocupado posicão
    if (comb_ocup_um == False and comb_ocup_dois == False):
        for comb in lista_pc_comb:
            if(comb['comb'] in ('   ')):
                comb['valido'] = 1
    return comb_ocup_dois

def status_partida():
    status = 0 #status: 0 - jogo acontecendo | 1 - empate | 2 - vitória
    comb_pos = [
        [1,2,3],[4,5,6],[7,8,9],#verifica linhas
        [1,4,7],[2,5,8],[3,6,9],#verifica colunas
        [1,5,9],[3,5,7],        #verifica diagonais
        [1,2,3,4,5,6,7,8,9]]    #verifica todas as posicoes
    #para cada combinação verifica os simbolos ocupados e após verifica status do jogo
    for ids_comb in comb_pos:
        comb_ocup = 0
        comb_feita = ''
        for posicao in lista_todas_posicoes:
            if(posicao['id'] in ids_comb and posicao['simbolo'] in ('X','O')):
                comb_feita += posicao['simbolo']
                comb_ocup += 1
        if (comb_feita in ('XXX','OOO')):
            if(comb_feita == 'XXX'):
                jogador_x[3] = 1
            else:
                jogador_o[3] = 1
            status = 2
            return status
        elif(comb_ocup == 9):
            status = 1
            return status
    return status 

def escolhe_posicao():
   #repete a escolha das posicoes caso a mesma esteja ocupada
   while(True):
        coluna_escolhida = valida_per(f'{ultima_jogada[0]}, escolha uma coluna: ',int,1,3)
        linha_escolhida = valida_per(f'{ultima_jogada[0]}, escolha uma linha: ',int,1,3)
        posicao_ocupada = ' '
        for posicao in lista_todas_posicoes:
            if ((posicao['linha'] == linha_escolhida) and (posicao['coluna'] == coluna_escolhida)):
                posicao_ocupada = posicao['simbolo']
        if (posicao_ocupada in ('X','O')):
            system('cls')
            menu()
            print('*Posição escolhida está ocupada! Tente novamente\n')
        else:
            for posicao in lista_todas_posicoes:
                if ((posicao['linha'] == linha_escolhida) and (posicao['coluna'] == coluna_escolhida)):
                    posicao['simbolo'] = ultima_jogada[1]
            break

def turno_atual(modo_jogo,inicio_partida):
    global jogador_x
    global jogador_o
    global ultima_jogada
    global num_jog_comp
    if (inicio_partida): #aleatoriza o jogador que inicia a partida
        jogadores = [jogador_x[1],jogador_o[1]]
        simbolos_jog = [jogador_x[2],jogador_o[2]]
        aleatorio = random.randint(0,1)
        ultima_jogada = [jogadores[aleatorio],simbolos_jog[aleatorio]]
    else: #faz a troca de vez entre cada jogador
        #modo jogador x jogador - altera o jogador conforme o ultimo que jogou
        if ((ultima_jogada[0] == jogador_x[1])):
            ultima_jogada = [jogador_o[1],jogador_o[2]]
            #modo jogador x computador - altera o jogador conforme modo
            if (modo_jogo == 1):
                escolhe_posicao()
            else:
                pc_turno()
                num_jog_comp += 1
        else:
            ultima_jogada = [jogador_x[1],jogador_x[2]]
            escolhe_posicao()

def reseta_partida():
    global pc_comb_atual
    global pc_id_alea_comb_jog
    global num_jog_comp
    #reseta valores da partida
    ultima_jogada.clear()
    for posicao in lista_todas_posicoes:
        posicao['simbolo'] = ' '
    #reseta status de vitoria dos jogadores
    jogador_x[3] = 0
    jogador_o[3] = 0
    #resetar variaveis de controle do computador
    pc_comb_atual = 0
    num_jog_comp = 0
    lista_pc_pos_comb_esc.clear()
    pc_id_alea_comb_jog = 0
    for bloq in lista_retorno_pc_comb_jog:
        bloq['bloq'] = 0

def menu_final_jogo():
    system('cls')
    if (jogador_x[0] > jogador_o[0]):
        jogador_vencedor = jogador_x[1]
    elif (jogador_o[0] > jogador_x[0]):
        jogador_vencedor = jogador_o[1]
    if (jogador_x[0] == jogador_o[0]):
        print(f'| Partida de Jogo da Velha não teve vencedores!\n')
    if ((jogador_x[0] > jogador_o[0]) or (jogador_o[0] > jogador_x[0])):
        system('cls')
        print(f'| Parabéns {jogador_vencedor}! Você venceu!\n')
    print(f'| Pontuações:\n| - {jogador_x[1]}: {jogador_x[0]}\n| - {jogador_o[1]}: {jogador_o[0]}')
    
def menu_final_partida():
    global jogador_x
    global jogador_o
    system('cls')
    menu()
    if((jogador_x[3] == 0) and (jogador_o[3] == 0)):
        print('| Empate! Nenhum jogador ganhou\n')
    else:
        if (jogador_x[3] == 1):
            print(f'| Vitoria de {jogador_x[1]} que escolheu {jogador_x[2]}!\n')
            jogador_x[0] += 1
        else:
            print(f'| Vitoria de {jogador_o[1]} que escolheu {jogador_o[2]}!\n')
            jogador_o[0] += 1
    print(f'| Pontuações:\n| - {jogador_x[1]}: {jogador_x[0]}\n| - {jogador_o[1]}: {jogador_o[0]}')

def menu():
    print(' JOGO DA VELHA\n ')
    for id in range(1,10,1):
        if (id in (1,4,7)):
            print('    |', end='')
        for posicao in lista_todas_posicoes:
            if (posicao['id'] == id):
                print(posicao['simbolo'], end='')
                print('|', end='')
        if(id in (3,6)):
            print('\r')
    print('\n\n Coluna x Linha\n')
    
def main():
    system('cls')
    print('|      JOGO DA VELHA       |')
    print('| Feito por Andrey Gabriel |')
    print('|                          |')
    print('|      MODOS DE JOGO       |')
    print('| 1 - Jogador x Jogador    |')
    print('| 2 - Jogador x Computador |\n')
    modo_jogo = valida_per('| Escolha um modo de jogo: ','menu',1,2)
    if (modo_jogo == 1):
        jogador_x[1] = valida_per('\n| Nome do Jogador que será o X: ',str)
        jogador_o[1] = valida_per('| Nome do Jogador que será o O: ',str)
    else:
        jogador_x[1] = valida_per('\n| Nome do Jogador que será o X: ',str)
        jogador_o[1] = 'Computador'
    while(True):
        system('cls')
        turno_atual(modo_jogo,True)
        #estrutura de repetição da jogada
        while(status_partida() == 0): #repetirá enquanto a partida estiver com status de jogo acontecendo
            system('cls')
            menu()
            turno_atual(modo_jogo,False)
        #estrutura após a finalização da partida
        menu_final_partida()
        resetar_partida = valida_per('\n| Deseja iniciar uma nova partida ? (1/0): ','menu',0,1)
        if(resetar_partida == 1):
            reseta_partida()
            continue
        else:
            menu_final_jogo()
            break

#variáveis de jogadores
jogador_x = [0,'','X',0] #pontuação, nome, simbolo, vitoria (0 e 1)
jogador_o = [0,'','O',0]
#controles de jogada
ultima_jogada = [] #jogador ultima jogada, simbolo do jogador
#variaveis globais do computador
num_jog_comp = 0
pc_comb_atual = 0
pc_id_alea_comb_jog = 0
lista_pc_pos_comb_esc = []
lista_pos_val_modo_alea = []
lista_comb_possiveis = []
#cadastro de combinações do computador
lista_retorno_pc_comb_jog = [{'id':[1,3],'ret':2,'bloq':0},{'id':[4,6],'ret':5,'bloq':0},{'id':[7,9],'ret':8,'bloq':0},
                             {'id':[1,7],'ret':4,'bloq':0},{'id':[2,8],'ret':5,'bloq':0},{'id':[3,9],'ret':6,'bloq':0},
                             {'id':[1,9],'ret':5,'bloq':0},{'id':[3,7],'ret':5,'bloq':0},{'id':[1,2],'ret':3,'bloq':0},
                             {'id':[2,3],'ret':1,'bloq':0},{'id':[4,5],'ret':6,'bloq':0},{'id':[5,6],'ret':4,'bloq':0},
                             {'id':[7,8],'ret':9,'bloq':0},{'id':[8,9],'ret':7,'bloq':0},{'id':[1,4],'ret':7,'bloq':0},
                             {'id':[4,7],'ret':1,'bloq':0},{'id':[2,5],'ret':8,'bloq':0},{'id':[5,8],'ret':2,'bloq':0},
                             {'id':[3,6],'ret':9,'bloq':0},{'id':[6,9],'ret':3,'bloq':0},{'id':[1,5],'ret':9,'bloq':0},
                             {'id':[5,9],'ret':1,'bloq':0},{'id':[3,5],'ret':7,'bloq':0},{'id':[5,7],'ret':3,'bloq':0}]
#pos_comb são os ids das posicoes
lista_pc_comb = [{'id':1,'comb':'','valido':0,'pos_comb':[1,2,3]},{'id':2,'comb':'','valido':0,'pos_comb':[4,5,6]},
                 {'id':3,'comb':'','valido':0,'pos_comb':[7,8,9]},{'id':4,'comb':'','valido':0,'pos_comb':[1,4,7]},
                 {'id':5,'comb':'','valido':0,'pos_comb':[2,5,8]},{'id':6,'comb':'','valido':0,'pos_comb':[3,6,9]},
                 {'id':7,'comb':'','valido':0,'pos_comb':[1,5,9]},{'id':8,'comb':'','valido':0,'pos_comb':[3,5,7]}]
#cadastro de posicoes
lista_todas_posicoes = [{'simbolo':' ','linha':1,'coluna':1,'id':1}, {'simbolo':' ','linha':1,'coluna':2,'id':2}, 
                        {'simbolo':' ','linha':1,'coluna':3,'id':3}, {'simbolo':' ','linha':2,'coluna':1,'id':4}, 
                        {'simbolo':' ','linha':2,'coluna':2,'id':5}, {'simbolo':' ','linha':2,'coluna':3,'id':6}, 
                        {'simbolo':' ','linha':3,'coluna':1,'id':7}, {'simbolo':' ','linha':3,'coluna':2,'id':8}, 
                        {'simbolo':' ','linha':3,'coluna':3,'id':9}]

from os import system
import random

main()