import pygame

pygame.init()

ecran = pygame.display.set_mode((1000,800))
rectScreen = ecran.get_rect()
clock=pygame.time.Clock()

##Section Couleurs##
'''
WHITE = (255,255,255)
BLACK = (0,0,0)
WHEAT = (245,222,179)
OLIVE_GREEN = (107,142,35)
BLUE = (30,144,255)
'''
BORD = (83, 110, 130)
CORN = (255,248,220)
BLUE_2 = (35, 70, 158)
CHESS = (252, 53, 3)
CHESS_MATE = (98, 3, 252)

##Setup des dico et variables##
pos_pieces = {}
pos_pieces2 = {}
pos_pions_base = {}
double = 0
mouvement_possible = {}
joueur = 0
manged = 0
manged_w = 1
manged_b = 1
manged_p_w = 1
manged_p_b = 1
chess_w = 0
chess_b = 0
##lettres pour les cases##
case = ["a","b","c","d","e","f","g","h"]

##Liste des pieces et pions BLACK et WHITE##
pieces_w = ["wr1.png","wn1.png","wb1.png","wq.png","wk.png","wb2.png","wn2.png","wr2.png"]
pions_w = ["wp1.png","wp2.png","wp3.png","wp4.png","wp5.png","wp6.png","wp7.png","wp8.png"]
pieces_b = ["br1.png","bn1.png","bb1.png","bq.png","bk.png","bb2.png","bn2.png","br2.png"]
pions_b = ["bp1.png","bp2.png","bp3.png","bp4.png","bp5.png","bp6.png","bp7.png","bp8.png"]

def miseEnPlace():##Creation de la fonction de mise en place du jeu
    ecran.fill(BLUE_2)##Ecran peint en bleu_2
    for i in range(5):
        for n in range(5):##Dessins des cases blanches de l'échéquier
            pygame.draw.rect(ecran,CORN,(n*200,i*200,100,100))
            pygame.draw.rect(ecran,CORN,(100 + n*200,i*200-100,100,100))
    for i in range(8):##Mise en place des lettres et chiffre pour le nom des cases
        bigText = pygame.font.SysFont('apple-system',30)
        if i % 2 == 0 :
            title_text = bigText.render(case[i],True,CORN)
        else :
            title_text = bigText.render(case[i],True,BLUE_2)
        ecran.blit(title_text,(i*100+85,775))
    for i in range(8):
        bigText = pygame.font.SysFont('apple-system',30)
        if i % 2 == 0 :
            title_text = bigText.render(str(8-i),True,BLUE_2)
        else :
            title_text = bigText.render(str(8-i ),True,CORN)
        ecran.blit(title_text,(5,i*100))
    for i in range(8) :## Mise en place pieces blanches
        piece_w = pygame.image.load(pieces_w[i]).convert_alpha()
        piece_w = pygame.transform.scale(piece_w,(100,100))
        pos_pieces[pieces_w[i]]=(i*100,700)
        ecran.blit(piece_w,(i*100,700))
    for i in range(8):## Mise en place pions blancs
        pion_w = pygame.image.load(pions_w[i]).convert_alpha()
        pion_w = pygame.transform.scale(pion_w,(100,100))
        pos_pieces[pions_w[i]]=(i*100,600)
        pos_pions_base[pions_w[i]]=(i*100,600)
        ecran.blit((pion_w),(i*100,600))
    for i in range(8) :## Mise en place pieces noires
        piece_b = pygame.image.load(pieces_b[i]).convert_alpha()
        piece_b = pygame.transform.scale(piece_b,(100,100))
        pos_pieces[pieces_b[i]]=(i*100,0)
        ecran.blit(piece_b,(i*100,0))
    for i in range(8):## Mise en place pions noirs
        pion_b = pygame.image.load(pions_b[i]).convert_alpha()
        pion_b = pygame.transform.scale(pion_b,(100,100))
        pos_pieces[pions_b[i]]=(i*100,100)
        pos_pions_base[pions_b[i]]=(i*100,100)
        ecran.blit(pion_b,(i*100,100))
    pygame.draw.rect(ecran,BORD,(800,0,200,800))

def cases():
    for i in range(8):##Mise en place des lettres et chiffre pour le nom des cases
        bigText = pygame.font.SysFont('apple-system',30)
        if i % 2 == 0 :
            title_text = bigText.render(case[i],True,CORN)
        else :
            title_text = bigText.render(case[i],True,BLUE_2)
        ecran.blit(title_text,(i*100+85,775))
    for i in range(8):
        bigText = pygame.font.SysFont('apple-system',30)
        if i % 2 == 0 :
            title_text = bigText.render(str(8-i),True,BLUE_2)
        else :
            title_text = bigText.render(str(8-i ),True,CORN)
        ecran.blit(title_text,(5,i*100))

###Fonction pour les mouvements possibles de chaques pieces###
def possibilités(mouvement_possible,nom_piece,pos_pieces,pos_pions_base,chess_b,chess_w) :
    for key in pos_pieces.keys() :
        ###Mouvements possibles des tour###
        if key[1] == "r" :
            possible = []
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0]),(int(pos_pieces[key][1])-(i+1)*100))
                possible.append(moove)
                if moove[1] < 0:
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0]),(int(pos_pieces[key][1])+(i+1)*100))
                possible.append(moove)
                if moove[1] > 800 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0])+(i+1)*100,int(pos_pieces[key][1]))
                possible.append(moove)
                if moove[0] > 800 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0])-(i+1)*100,int(pos_pieces[key][1]))
                possible.append(moove)
                if moove[0] < 0 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            possible.sort()
            mouvement_possible[key] = possible
        ###Mouvements possibles des fous###
        if key[1] == "b" :
            possible = []
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0]) + (i+1)*100 , int(pos_pieces[key][1]) + (i+1)*100)
                possible.append(moove)
                if moove[0] >= 800 and moove[1] >= 800 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0]) - (i+1)*100 , int(pos_pieces[key][1]) + (i+1)*100)
                possible.append(moove)
                if moove[0] <= 0 and moove[1] >= 800 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0]) + (i+1)*100 , int(pos_pieces[key][1]) - (i+1)*100)
                possible.append(moove)
                if moove[0] >= 800 and moove[1] <= 0 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0]) - (i+1)*100 , int(pos_pieces[key][1]) - (i+1)*100)
                possible.append(moove)
                if moove[0] <= 0 and moove[1] <= 0 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            possible.sort()
            mouvement_possible[key] = possible
        ###Mouvements possibles des rennes###
        if key[1] == "q" :
            possible = []
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0]),(int(pos_pieces[key][1])-(i+1)*100))
                possible.append(moove)
                if moove[1] < 0:
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0]),(int(pos_pieces[key][1])+(i+1)*100))
                possible.append(moove)
                if moove[1] > 800 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0])+(i+1)*100,int(pos_pieces[key][1]))
                possible.append(moove)
                if moove[0] > 800 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0])-(i+1)*100,int(pos_pieces[key][1]))
                possible.append(moove)
                if moove[0] < 0 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0]) + (i+1)*100 , int(pos_pieces[key][1]) + (i+1)*100)
                possible.append(moove)
                if moove[0] >= 800 and moove[1] >= 800 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0]) - (i+1)*100 , int(pos_pieces[key][1]) + (i+1)*100)
                possible.append(moove)
                if moove[0] <= 0 and moove[1] >= 800 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0]) + (i+1)*100 , int(pos_pieces[key][1]) - (i+1)*100)
                possible.append(moove)
                if moove[0] >= 800 and moove[1] <= 0 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            run = True
            i = 0
            while run == True :###Pour chaques axes et directions on regarde jusqu'ou la tour peut aller###
                moove = (int(pos_pieces[key][0]) - (i+1)*100 , int(pos_pieces[key][1]) - (i+1)*100)
                possible.append(moove)
                if moove[0] <= 0 and moove[1] <= 0 :
                    run = False
                if moove in pos_pieces.values() :
                    run = False
                i += 1
            possible.sort()
            mouvement_possible[key] = possible
        ###Mouvements possibles des cavaliers###
        if key[1] == "n" :
            possible = []
            ###Tous les mouvements possibles du cavalier###
            moove = (int(pos_pieces[key][0]) - 200 , int(pos_pieces[key][1]) + 100)
            possible.append(moove)

            moove = (int(pos_pieces[key][0]) - 200 , int(pos_pieces[key][1]) - 100)
            possible.append(moove)

            moove = (int(pos_pieces[key][0]) - 100 , int(pos_pieces[key][1]) - 200)
            possible.append(moove)

            moove = (int(pos_pieces[key][0]) - 100 , int(pos_pieces[key][1]) + 200)
            possible.append(moove)

            moove = (int(pos_pieces[key][0]) + 100 , int(pos_pieces[key][1]) - 200)
            possible.append(moove)

            moove = (int(pos_pieces[key][0]) + 100 , int(pos_pieces[key][1]) + 200)
            possible.append(moove)

            moove = (int(pos_pieces[key][0]) + 200 , int(pos_pieces[key][1]) - 100)
            possible.append(moove)

            moove = (int(pos_pieces[key][0]) + 200 , int(pos_pieces[key][1]) + 100)
            possible.append(moove)


            possible.sort()
            mouvement_possible[key] = possible
        ###Mouvements possibles des pions###
        if key[1] == "p" :
            possible = []
            if nom_piece[0]== "w" :### Si pion blanc ###
                    if pos_pieces[key] == pos_pions_base[key] :
                        ### Si pion est a sa pose de base ###
                        if ((int(pos_pieces[key][0]) , int(pos_pieces[key][1]) - 200) and (int(pos_pieces[key][0]) , int(pos_pieces[key][1]) - 100) not in pos_pieces.values() ) :
                            moove = (int(pos_pieces[key][0]) , int(pos_pieces[key][1]) - 100)
                            possible.append(moove)
                            moove = (int(pos_pieces[key][0]) , int(pos_pieces[key][1]) - 200)
                            possible.append(moove)
                    if (int(pos_pieces[key][0]) , int(pos_pieces[key][1]) - 100) not in pos_pieces.values() :
                        moove = (int(pos_pieces[key][0]) , int(pos_pieces[key][1]) - 100)
                        possible.append(moove)
                    if (int(pos_pieces[key][0]) + 100 ,int(pos_pieces[key][1]) - 100) in pos_pieces.values() :
                        moove = (int(pos_pieces[key][0]) + 100 ,int(pos_pieces[key][1]) - 100)
                        possible.append(moove)
                    if (int(pos_pieces[key][0]) - 100 ,int(pos_pieces[key][1]) - 100) in pos_pieces.values() :
                        moove = (int(pos_pieces[key][0]) - 100 ,int(pos_pieces[key][1]) - 100)
                        possible.append(moove)
            if nom_piece[0] == "b" :### Si pion noir ###
                    if pos_pieces[key] == pos_pions_base[key] :
                        ### Si pion est a sa pose de base ###
                        if ((int(pos_pieces[key][0]) , int(pos_pieces[key][1]) + 200) and (int(pos_pieces[key][0]) , int(pos_pieces[key][1]) + 100) not in pos_pieces.values() ) :
                            moove = (int(pos_pieces[key][0]) , int(pos_pieces[key][1]) + 100)
                            possible.append(moove)
                            moove = (int(pos_pieces[key][0]) , int(pos_pieces[key][1]) + 200)
                            possible.append(moove)
                    if (int(pos_pieces[key][0]) , int(pos_pieces[key][1]) + 100) not in pos_pieces.values() :
                        moove = (int(pos_pieces[key][0]) , int(pos_pieces[key][1]) + 100)
                        possible.append(moove)
                    if (int(pos_pieces[key][0]) + 100 ,int(pos_pieces[key][1]) + 100) in pos_pieces.values() :
                        moove = (int(pos_pieces[key][0]) + 100 ,int(pos_pieces[key][1]) + 100)
                        possible.append(moove)
                    if (int(pos_pieces[key][0]) - 100 ,int(pos_pieces[key][1]) + 100) in pos_pieces.values() :
                        moove = (int(pos_pieces[key][0]) - 100 ,int(pos_pieces[key][1]) + 100)
                        possible.append(moove)

            possible.sort()
            mouvement_possible[key] = possible
        ###Mouvements possibles des rois###
        if key[1] == "k" :
            possible = []
            ###Tous les mouvements d'une case autour du roi possibles###
            if key[0] == "b" :
                if chess_b == 1 :
                    moove = (int(pos_pieces[key][0]),(int(pos_pieces[key][1])-100))
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "b" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]),(int(pos_pieces[key][1])+100))
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "b" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0])+100,int(pos_pieces[key][1]))
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "b" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0])-100,int(pos_pieces[key][1]))
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "b" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]) + 100 , int(pos_pieces[key][1]) + 100)
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "b" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]) - 100 , int(pos_pieces[key][1]) + 100)
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "b" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]) + 100 , int(pos_pieces[key][1]) - 100)
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "b" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]) - 100 , int(pos_pieces[key][1]) - 100)
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "b" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
            if key[0] == "w" :
                if chess_w == 1 :
                    moove = (int(pos_pieces[key][0]),(int(pos_pieces[key][1])-100))
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "w" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]),(int(pos_pieces[key][1])+100))
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "w" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0])+100,int(pos_pieces[key][1]))
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "w" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0])-100,int(pos_pieces[key][1]))
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "w" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]) + 100 , int(pos_pieces[key][1]) + 100)
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "w" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]) - 100 , int(pos_pieces[key][1]) + 100)
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "w" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]) + 100 , int(pos_pieces[key][1]) - 100)
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "w" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]) - 100 , int(pos_pieces[key][1]) - 100)
                    if moove in pos_pieces.values() :
                        if pos_pieces2[moove][0] != "w" :
                            if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    else :
                        if moove[0] >= 0 and moove[1] >= 0 :
                                if moove[0] <= 700 and moove[1] <= 700 :
                                    possible.append(moove)
                    possible.sort()
                    mouvement_possible[key] = possible
            if chess_w == 0 and chess_b == 0 :
                    moove = (int(pos_pieces[key][0]),(int(pos_pieces[key][1])-100))
                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]),(int(pos_pieces[key][1])+100))
                    possible.append(moove)
                    moove = (int(pos_pieces[key][0])+100,int(pos_pieces[key][1]))
                    possible.append(moove)
                    moove = (int(pos_pieces[key][0])-100,int(pos_pieces[key][1]))
                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]) + 100 , int(pos_pieces[key][1]) + 100)
                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]) - 100 , int(pos_pieces[key][1]) + 100)
                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]) + 100 , int(pos_pieces[key][1]) - 100)
                    possible.append(moove)
                    moove = (int(pos_pieces[key][0]) - 100 , int(pos_pieces[key][1]) - 100)
                    possible.append(moove)
        possible.sort()
        mouvement_possible[key] = possible
    return mouvement_possible

miseEnPlace()##Mise en place avant de lancer le jeu
def mouvement(nom_piece,nom_piece2,joueur,manged_w,manged_b):
    manged = 0
    if coordonee1 != coordonee2 :##Verification si il y a eu un mouvement
        if nom_piece[0] != nom_piece2[0] :
            if nom_piece2[1] != "k" :
                piece = pygame.image.load(nom_piece).convert_alpha()##Choix de l'image de la pièce avec l'URL
                piece = pygame.transform.scale(piece,(100,100))##Mise a l'échelle de la pièce
                for value in pos_pieces.values() :
                    if coordonee2 == value :
                        manged += 1
                if (((pos_pieces[nom_piece])[0])+((pos_pieces[nom_piece])[1]))%200 == 0 :##Cache l'ancienne pièce
                    pygame.draw.rect(ecran,CORN,((pos_pieces[nom_piece])[0],(pos_pieces[nom_piece])[1],100,100))
                    cases()
                else :
                    pygame.draw.rect(ecran,BLUE_2,((pos_pieces[nom_piece])[0],(pos_pieces[nom_piece])[1],100,100))
                    cases()
                if ((coordonee2_x)+(coordonee2_y))%200 == 0 :##Prépare la nouvelle case pour la pièce
                    pygame.draw.rect(ecran,CORN,(coordonee2_x,coordonee2_y,100,100))
                    cases()
                else :
                    pygame.draw.rect(ecran,BLUE_2,(coordonee2_x,coordonee2_y,100,100))
                    cases()
                ecran.blit(piece,(coordonee2[0],coordonee2[1]))##Affichage de la pièce sur sa nouvelle case
                nom_piece2 = "oo"
                for key in pos_pieces.keys() :
                    if pos_pieces[key] == coordonee2 :
                        nom_piece2 = key
                ###Si il y'a eu une piece mangée ou non ###
                ###On met les dictionnaires des pieces a jours ###
                if manged == 1 :
                    del pos_pieces[nom_piece2]
                    del pos_pieces2[coordonee2]
                    del pos_pieces2[coordonee1]
                    pos_pieces[nom_piece] = coordonee2
                    pos_pieces2[coordonee2] = nom_piece
                else :
                    pos_pieces[nom_piece] = coordonee2
                    del pos_pieces2[coordonee1]
                    pos_pieces2[coordonee2] = nom_piece

def chess(pos_pieces,mouvement_possible) :
    chess_w = 0
    chess_b = 0
    for key in mouvement_possible.keys() :
        for i in range (len(mouvement_possible[key])) :
            if key[0] == "w" :
                if (mouvement_possible[key])[i] == pos_pieces["bk.png"] :
                    chess_b += 1
                    b_king = pygame.image.load("bk.png").convert_alpha()
                    b_king = pygame.transform.scale(b_king,(100,100))
                    pygame.draw.rect(ecran,CHESS,(pos_pieces["bk.png"][0],pos_pieces["bk.png"][1],100,100))
                    ecran.blit(b_king,(pos_pieces["bk.png"][0],pos_pieces["bk.png"][1]))
            if key[0] == "b" :
                if (mouvement_possible[key])[i] == pos_pieces["wk.png"] :
                    chess_w += 1
                    w_king = pygame.image.load("wk.png").convert_alpha()
                    w_king = pygame.transform.scale(w_king,(100,100))
                    pygame.draw.rect(ecran,CHESS,(pos_pieces["wk.png"][0],pos_pieces["wk.png"][1],100,100))
                    ecran.blit(w_king,(pos_pieces["wk.png"][0],pos_pieces["wk.png"][1]))
    return chess_b,chess_w

continuer = True

while continuer:##Boucle de jeu
    for key in pos_pieces.keys():
        pos_pieces2[pos_pieces[key]] = key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:##Si on appuis sur la croix ferme le jeu et l'arrete
            continuer = False
        elif event.type == pygame.MOUSEBUTTONDOWN   :##Quand on appuis sur le bouton de la souris

            coordonee1_x = pygame.mouse.get_pos()[0]//100*100 #arrondir à 100px
            coordonee1_y = pygame.mouse.get_pos()[1]//100*100 #arrondir à 100px

            coordonee1 = (coordonee1_x,coordonee1_y)##Coordonées arrondies au centiéme pour identifié la pièce a deplacer

            for key in pos_pieces.keys():
                if pos_pieces[key] == coordonee1 :##Si on a Cliquer sur une pièce
                    nom_piece = key##URL de l'image pour la pièce choisie

            chess(pos_pieces,mouvement_possible)
            chess_b = chess(pos_pieces,mouvement_possible)[0]
            chess_w = chess(pos_pieces,mouvement_possible)[1]
            print(chess_b,chess_w)

            possibilités(mouvement_possible,nom_piece,pos_pieces,pos_pions_base,chess_b,chess_w)
            print(mouvement_possible["wk.png"])

        elif event.type == pygame.MOUSEBUTTONUP   :##Quand le bouton de souris est relaché
            coordonee2_x = pygame.mouse.get_pos()[0]//100*100 #arrondir à 100px
            coordonee2_y = pygame.mouse.get_pos()[1]//100*100 #arrondir à 100px

            coordonee2 = (coordonee2_x,coordonee2_y)##Coordonées de la nouvelle case arrondies a la centaine

            nom_piece2 = "oo"
            for key in pos_pieces.keys() :
                if pos_pieces[key] == coordonee2 :
                    nom_piece2 = key

            ##Debut fonctions mouvement differentes pièces##

            eaten = "oo"

            if int(joueur) % 2 == 0 :
                if nom_piece[0] == "w" :
                    if (nom_piece in mouvement_possible.keys()) :
                        if chess_w == 0 :
                            if (coordonee2 in (mouvement_possible[nom_piece])) :
                                manged = 0
                                for value in pos_pieces.values() :
                                    if coordonee2 == value  :
                                        if (pos_pieces[nom_piece])[0] != value[0] :
                                            manged += 1
                                if manged == 1 :
                                    eaten = pos_pieces2[coordonee2]
                                mouvement(nom_piece,nom_piece2,joueur,manged_w,manged_b)
                        if pos_pieces[nom_piece] != coordonee1 :
                                joueur += 1
            if int(joueur) % 2 == 1 :
                if nom_piece[0] == "b" :
                    if (nom_piece in mouvement_possible.keys()) :
                        if (coordonee2 in (mouvement_possible[nom_piece])) :
                            manged = 0
                            for value in pos_pieces.values() :
                                if coordonee2 == value :
                                    manged += 1
                            if manged == 1 :
                                eaten = pos_pieces2[coordonee2]
                            mouvement(nom_piece,nom_piece2,joueur,manged_w,manged_b)
                    if pos_pieces[nom_piece] != coordonee1 :
                        joueur += 1
            ###############################################
            if manged == 1 :
                if nom_piece[0] != eaten[0] :
                    if eaten[0] == "w" and eaten[1] == "p" :
                        manged_w += 1
                    if eaten[0] == "b" and eaten[1] == "p" :
                        manged_b += 1
                    if eaten != "oo" :
                        mange = pygame.image.load(eaten).convert_alpha()
                        mange = pygame.transform.scale(mange,(80,80))
                        if (eaten)[0] == "w" :
                            if (eaten)[1] == "p" :
                                ecran.blit(mange,(750+((manged_w+1)*15),100))
                            if (eaten)[1] != "p" :
                                ecran.blit(mange,(800+((8-manged_p_w)*25),200))
                        if (eaten)[0] == "b" :
                            if (eaten)[1] == "p" :
                                ecran.blit(mange,(750+((manged_b+1)*15),500))
                            if (eaten)[1] != "p" :
                                ecran.blit(mange,(800+((8-manged_p_b)*25),600))
            manged_p_w = 0
            manged_p_b = 0
            for i in pos_pieces.keys() :
                if i[0] == "w" and i[1] != "p" :
                    manged_p_w += 1
                if i[0] == "b" and i[1] != "p" :
                    manged_p_b += 1

            chess_b = chess(pos_pieces,mouvement_possible)[0]
            chess_w = chess(pos_pieces,mouvement_possible)[1]

            possibilités(mouvement_possible,nom_piece,pos_pieces,pos_pions_base,chess_b,chess_w)

            chess_b = chess(pos_pieces,mouvement_possible)[0]
            chess_w = chess(pos_pieces,mouvement_possible)[1]

            possibilités(mouvement_possible,nom_piece,pos_pieces,pos_pions_base,chess_b,chess_w)

            if chess_w == 0 :
                if (((pos_pieces["wk.png"])[0])+((pos_pieces["wk.png"])[1]))%200 == 0 :##Cache l'ancienne pièce
                    pygame.draw.rect(ecran,CORN,((pos_pieces["wk.png"])[0],(pos_pieces["wk.png"])[1],100,100))
                    cases()
                    w_king = pygame.image.load("wk.png").convert_alpha()
                    w_king = pygame.transform.scale(w_king,(100,100))
                    ecran.blit(w_king,(pos_pieces["wk.png"][0],pos_pieces["wk.png"][1]))
                else :
                    pygame.draw.rect(ecran,BLUE_2,((pos_pieces["wk.png"])[0],(pos_pieces["wk.png"])[1],100,100))
                    cases()
                    w_king = pygame.image.load("wk.png").convert_alpha()
                    w_king = pygame.transform.scale(w_king,(100,100))
                    ecran.blit(w_king,(pos_pieces["wk.png"][0],pos_pieces["wk.png"][1]))
            if chess_b == 0 :
                if (((pos_pieces["bk.png"])[0])+((pos_pieces["bk.png"])[1]))%200 == 0 :##Cache l'ancienne pièce
                    pygame.draw.rect(ecran,CORN,((pos_pieces["bk.png"])[0],(pos_pieces["bk.png"])[1],100,100))
                    cases()
                    b_king = pygame.image.load("bk.png").convert_alpha()
                    b_king = pygame.transform.scale(b_king,(100,100))
                    ecran.blit(b_king,(pos_pieces["bk.png"][0],pos_pieces["bk.png"][1]))
                else :
                    pygame.draw.rect(ecran,BLUE_2,((pos_pieces["bk.png"])[0],(pos_pieces["bk.png"])[1],100,100))
                    cases()
                    b_king = pygame.image.load("bk.png").convert_alpha()
                    b_king = pygame.transform.scale(b_king,(100,100))
                    ecran.blit(b_king,(pos_pieces["bk.png"][0],pos_pieces["bk.png"][1]))

            possibilités(mouvement_possible,nom_piece,pos_pieces,pos_pions_base,chess_b,chess_w)

        if event.type == pygame.K_r or event.type == pygame.KEYUP:##appuyer sur r pour reset l'échéquier

                miseEnPlace()
                print(pos_pieces)

    clock.tick(60)
    pygame.display.flip()
pygame.quit()







###Anciennes fonctions de mouvement
"""
for value in pos_pieces.values() :
                    if coordonee2 == value :
                        manged += 1
            print(manged)

            if manged > 0 :
                mange = pygame.image.load(pos_pieces2[coordonee2]).convert_alpha()
                mange = pygame.transform.scale(mange,(70,70))
                if (pos_pieces2[coordonee2])[0] == "w" :
                    ecran.blit(mange,(800+(manged_w*20),200))
                    manged_w += 1
                if (pos_pieces2[coordonee2])[0] == "b" :
                    ecran.blit(mange,(int(800+(manged_b*20)),500))
                    manged_b += 1
"""

"""
def mouvement_tour(nom_piece,pos_pieces,mouvement_possible,nom_piece2):
    if str(nom_piece[1]) == "r" :
        mouvement_possible
        if coordonee1[0] == coordonee2[0] :
            mouvement(nom_piece,nom_piece2,joueur)
        elif coordonee1[1] == coordonee2[1] :
            mouvement(nom_piece,nom_piece2,joueur)
"""

"""
def mouvement_fous(nom_piece,nom_piece2) :
    if str(nom_piece[1]) == "b" :
        for i in range(8) :
            if int(coordonee1[0]) + i*100 == coordonee2[0] and int(coordonee1[1]) + i*100 == coordonee2[1] :
                mouvement(nom_piece,nom_piece2,joueur)
            if int(coordonee1[0]) + i*100 == coordonee2[0] and int(coordonee1[1]) - i*100 == coordonee2[1] :
                mouvement(nom_piece,nom_piece2,joueur)
            if int(coordonee1[0]) - i*100 == coordonee2[0] and int(coordonee1[1]) + i*100 == coordonee2[1] :
                mouvement(nom_piece,nom_piece2,joueur)
            if int(coordonee1[0]) - i*100 == coordonee2[0] and int(coordonee1[1]) - i*100 == coordonee2[1] :
                mouvement(nom_piece,nom_piece2,joueur)
"""

'''
def mouvement_cavalier(nom_piece,nom_piece2):
    if str(nom_piece[1]) == "n" :
        if coordonee2[0] == int(coordonee1[0]) - 200 and coordonee2[1] == int(coordonee1[1]) + 100 :
            mouvement(nom_piece,nom_piece2,joueur)
        elif coordonee2[0] == int(coordonee1[0]) - 200 and coordonee2[1] == int(coordonee1[1]) - 100 :
            mouvement(nom_piece,nom_piece2,joueur)
        elif coordonee2[0] == int(coordonee1[0]) - 100 and coordonee2[1] == int(coordonee1[1]) - 200 :
            mouvement(nom_piece,nom_piece2,joueur)
        elif coordonee2[0] == int(coordonee1[0]) - 100 and coordonee2[1] == int(coordonee1[1]) + 200 :
            mouvement(nom_piece,nom_piece2,joueur)
        elif coordonee2[0] == int(coordonee1[0]) + 100 and coordonee2[1] == int(coordonee1[1]) - 200 :
            mouvement(nom_piece,nom_piece2,joueur)
        elif coordonee2[0] == int(coordonee1[0]) + 100 and coordonee2[1] == int(coordonee1[1]) + 200 :
            mouvement(nom_piece,nom_piece2,joueur)
        elif coordonee2[0] == int(coordonee1[0]) + 200 and coordonee2[1] == int(coordonee1[1]) - 100 :
            mouvement(nom_piece,nom_piece2,joueur)
        elif coordonee2[0] == int(coordonee1[0]) + 200 and coordonee2[1] == int(coordonee1[1]) + 100 :
            mouvement(nom_piece,nom_piece2,joueur)
'''

'''
def mouvement_pions(nom_piece,pos_pions_base,pos_pieces,nom_piece2) :
    mange = 0
    for value in pos_pieces.values() :
        if coordonee2 == value :
            mange += 1
    if str(nom_piece[0]+nom_piece[1]) == "wp" :
        if mange == 0 :
            if coordonee1[0] == coordonee2[0] and coordonee2[1] == int((pos_pions_base[nom_piece])[1]) - 200 :
                mouvement(nom_piece,nom_piece2,joueur)
            elif coordonee1[0] == coordonee2[0] and coordonee2[1] == int((pos_pieces[nom_piece])[1]) - 100 :
                mouvement(nom_piece,nom_piece2,joueur)
        else :
            if coordonee1[0] == coordonee2[0] + 100 and coordonee2[1] == int((pos_pieces[nom_piece])[1]) - 100 :
                mouvement(nom_piece,nom_piece2,joueur)
            elif coordonee1[0] == coordonee2[0] - 100 and coordonee2[1] == int((pos_pieces[nom_piece])[1]) - 100 :
                mouvement(nom_piece,nom_piece2,joueur)
    if str(nom_piece[0]+nom_piece[1]) == "bp" :
        if mange == 0 :
            if coordonee1[0] == coordonee2[0] and coordonee2[1] == int((pos_pions_base[nom_piece])[1]) + 200 :
                mouvement(nom_piece,nom_piece2,joueur)
            elif coordonee1[0] == coordonee2[0] and coordonee2[1] == int((pos_pieces[nom_piece])[1]) + 100 :
                mouvement(nom_piece,nom_piece2,joueur)
        else :
            if coordonee1[0] == coordonee2[0] + 100 and coordonee2[1] == int((pos_pieces[nom_piece])[1]) + 100 :
                mouvement(nom_piece,nom_piece2,joueur)
            elif coordonee1[0] == coordonee2[0] - 100 and coordonee2[1] == int((pos_pieces[nom_piece])[1]) + 100 :
                mouvement(nom_piece,nom_piece2,joueur)
'''

"""
def mouvement_queen(nom_piece,nom_piece2):
    if nom_piece[1] == "q" :
        if coordonee1[0] == coordonee2[0] :
            mouvement(nom_piece,nom_piece2,joueur)
        if coordonee1[1] == coordonee2[1] :
            mouvement(nom_piece,nom_piece2,joueur)
        for i in range(8) :
            if int(coordonee1[0]) + i*100 == coordonee2[0] and int(coordonee1[1]) + i*100 == coordonee2[1] :
                mouvement(nom_piece,nom_piece2,joueur)
            if int(coordonee1[0]) + i*100 == coordonee2[0] and int(coordonee1[1]) - i*100 == coordonee2[1] :
                mouvement(nom_piece,nom_piece2,joueur)
            if int(coordonee1[0]) - i*100 == coordonee2[0] and int(coordonee1[1]) + i*100 == coordonee2[1] :
                mouvement(nom_piece,nom_piece2,joueur)
            if int(coordonee1[0]) - i*100 == coordonee2[0] and int(coordonee1[1]) - i*100 == coordonee2[1] :
                mouvement(nom_piece,nom_piece2,joueur)
"""
'''
def mouvement_king(nom_piece,nom_piece2) :
    if nom_piece[1] == "k" :
        if int(coordonee1[0]) + 100 == coordonee2[0] :
            mouvement(nom_piece,nom_piece2,joueur)
        if int(coordonee1[1]) + 100 == coordonee2[1] :
            mouvement(nom_piece,nom_piece2,joueur)
        if int(coordonee1[0]) - 100 == coordonee2[0] :
            mouvement(nom_piece,nom_piece2,joueur)
        if int(coordonee1[1]) - 100 == coordonee2[1] :
            mouvement(nom_piece,nom_piece2,joueur)
        if int(coordonee1[0]) + 100 == coordonee2[0] and int(coordonee1[1]) + 100 == coordonee2[1] :
            mouvement(nom_piece,nom_piece2,joueur)
        if int(coordonee1[0]) + 100 == coordonee2[0] and int(coordonee1[1]) - 100 == coordonee2[1] :
            mouvement(nom_piece,nom_piece2,joueur)
        if int(coordonee1[0]) - 100 == coordonee2[0] and int(coordonee1[1]) + 100 == coordonee2[1] :
            mouvement(nom_piece,nom_piece2,joueur)
        if int(coordonee1[0]) - 100 == coordonee2[0] and int(coordonee1[1]) - 100 == coordonee2[1] :
            mouvement(nom_piece,nom_piece2,joueur)
'''

"""
    moove = ""
    piece = 0
    possible = 0
    mvmnt_rook = []
    vector = {}
    vector[nom_piece] = ""
    if str(nom_piece[1]) == "r" :
        if coordonee1[0] == coordonee2[0] :
            if coordonee1[1] > coordonee2[1] :
                mvmnt_rook = []
                for i in range(1,coordonee2[1]//100-2):
                    moove = (coordonee1[0],coordonee1[1]-i*100)
                    mvmnt_rook.append(moove)
                vector[nom_piece] = mvmnt_rook
                print(vector)
                print(len(vector[nom_piece]))
                for i in range (len(vector[nom_piece])) :
                    print(vector[nom_piece])
                    if ((vector[nom_piece])[i] in pos_pieces.values()):
                        possible += 1
                if possible == 0 :
                    mouvement(nom_piece,nom_piece2,joueur)
                    for i in range(8) :
                        moove = (coordonee1[0],i*100)
                        mvmnt_rook.append(moove)
                        moove = i*100,coordonee1[1]
                        mvmnt_rook.append(moove)
                        mvmnt_rook.sort()
                    mouvement_pieces[nom_piece] = mvmnt_rook
                print(possible)
            if coordonee1[1] < coordonee2[1] :
                mvmnt_rook = []
                for i in range(2,coordonee2[1]//100):
                    moove = (coordonee1[0],coordonee1[1]+i*100)
                    mvmnt_rook.append(moove)
                vector[nom_piece] = mvmnt_rook
                print(vector)
                for i in range (len(vector[nom_piece])) :
                    if ((vector[nom_piece])[i] in pos_pieces.values()):
                        possible += 1
                if possible == 0 :
                    mouvement(nom_piece,nom_piece2,joueur)
                    for i in range(8) :
                        moove = (coordonee1[0],i*100)
                        mvmnt_rook.append(moove)
                        moove = i*100,coordonee1[1]
                        mvmnt_rook.append(moove)
                        mvmnt_rook.sort()
                    mouvement_pieces[nom_piece] = mvmnt_rook
        if coordonee1[1] == coordonee2[1] :
            if coordonee1[0] > coordonee2[0] :
                for i in range(2,coordonee2[0]//100):
                    moove = coordonee1[0]-i*100,coordonee1[1]
                    vector[nom_piece] = vector[nom_piece] + str(moove)
                for i in range (len(vector[nom_piece])) :
                    if ((vector[nom_piece])[i] in pos_pieces.values()):
                        possible += 1
                if possible == 0 :
                    mouvement(nom_piece,nom_piece2,joueur)
                    for i in range(8) :
                        moove = (coordonee1[0],i*100)
                        mvmnt_rook.append(moove)
                        moove = i*100,coordonee1[1]
                        mvmnt_rook.append(moove)
                        mvmnt_rook.sort()
                    mouvement_pieces[nom_piece] = mvmnt_rook
            if coordonee1[0] < coordonee2[0] :
                for i in range(2,coordonee2[0]//100):
                    moove = coordonee1[0]+i*100,coordonee1[1]
                    vector[nom_piece] = vector[nom_piece] + str(moove)
                for i in range (len(vector[nom_piece])) :
                    if ((vector[nom_piece])[i] in pos_pieces.values()):
                        possible += 1
                if possible == 0 :
                    mouvement(nom_piece,nom_piece2,joueur)
                    for i in range(8) :
                        moove = (coordonee1[0],i*100)
                        mvmnt_rook.append(moove)
                        moove = i*100,coordonee1[1]
                        mvmnt_rook.append(moove)
                        mvmnt_rook.sort()
                    mouvement_pieces[nom_piece] = mvmnt_rook
"""