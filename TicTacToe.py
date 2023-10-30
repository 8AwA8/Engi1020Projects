import pygame
import time
'''This code was written and tested by Andrew Matthews, acwmatthews@mun.ca. Use of code is public, do not claim as own. This code instantializes a replayable game of Tic Tac Toe'''
pygame.init()

#region Base Starting Code for variable assignment and pygame setup
headingf = pygame.font.SysFont("Times new roman", 50, bold=True)
normf = pygame.font.SysFont("Times new roman", 15, bold=True)
ga = [['','',''],['','',''],['','','']]
cpos = [[[450, 180],[450, 360],[450,540]],[[640, 180],[640, 360],[640,540]],[[820, 180],[820, 360],[820,540]]]
colors=["#f7cac9", "#dec2cb", "#c5b9cd", "#abb1cf", "#92a8d1"]
playcols = [(17,17,240),(240,17,17)]
grayscale = ['#111111','#333333','#555555','#777777','#999999','#FFFFFF']
screen = pygame.display.set_mode((1280,720))
playind = pygame.Surface((1280, 720), pygame.SRCALPHA)
timer = pygame.time.Clock()
running = True
ts = 0
intro = True
Game = True
score = [0,0]
v = 0.5
pygame.mixer.music.load('Move on Old Friend - HalfHuman.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(v)
turn = 'x'
screen.fill('White')
pygame.draw.circle(screen, "Black", (1280/2, 720/2), 70)
AwA = headingf.render("AwA", False, "White")
screen.blit(AwA, (587, 325))
#endregion

def startAnim():    #Works through the cool starting animation when code is loaded
    for i in range(74):
        pygame.draw.line(screen, colors[i%5], (1280-i*12,720), (1280,720-i*12), 50)
        pygame.display.flip()
        pygame.draw.line(screen, colors[i%5], (1280-i*12,0), (1280,0+i*12), 50)
        pygame.display.flip()
        pygame.draw.line(screen, colors[i%5], (0+i*12,0), (0,0+i*12), 50)
        pygame.display.flip()
        pygame.draw.line(screen, colors[i%5], (0,720-i*12), (0+i*12,720), 50)
        time.sleep(0.02)
        pygame.display.flip()
    for i in range(125):
        pygame.draw.line(screen, "Black", (0,370), (0+i*12,370), 1000)
        time.sleep(0.01)
        pygame.display.flip()
    screen.fill("Black")
    for i in range(541):
        pygame.draw.line(screen, "white", (550, 90), (550, 90+i),10)
        pygame.draw.line(screen, "white", (730, 630-i), (730, 630),10)
        pygame.draw.line(screen, "white", (370, 270), (370+i, 270),10)
        pygame.draw.line(screen, "white", (910-i, 450), (910, 450),10)
        time.sleep(0.01)
        pygame.display.flip()
        if i == 104:
            tic = headingf.render("Tic", False, "White")
            screen.blit(tic, (420, 10))
        if i == 208:
            tac = headingf.render("Tac", False, "White")
            screen.blit(tac, (600, 10))
        if i == 312:
            tic = headingf.render("Toe", False, "White")
            screen.blit(tic, (780, 10))

def GameCheck():    #Checks if game has ended in a win or tie
    win = False
    for x in range(3):
        if ga[x][0] == ga[x][1] == ga[x][2] and ga[x][0] != '':
            WinEffect(x,0,x,2, 0, 60)
            win = True
        elif ga[0][x] == ga[1][x] == ga[2][x] and ga[0][x] != '':
            WinEffect(0,x,2,x, 60, 0)
            win = True
    if ga[0][0] == ga[1][1] == ga[2][2] and ga[1][1] != '':
        WinEffect(0,0,2,2, 60, 60)
        win = True
    elif ga[2][0] == ga[1][1] == ga[0][2] and ga[1][1] != '':
        WinEffect(2,0,0,2, -60, -60)
        win = True
    if win == False:
        for i in range(3):
            for x in range(3):
                if ga[i][x] == '':
                    return(win)
        Tiexx = headingf.render("Replay?", False, "White", 'Black')
        screen.blit(Tiexx, (553, 400))
        win = True
    return(win)
    
def ScoreUpdater(n):    #Updates scoreboard
    score[n] += 1
    pygame.draw.rect(screen, 'Black', (100, 300, 200, 100))
    pygame.draw.rect(screen, 'Black', (1120, 300, 160, 100))
    sc1 = headingf.render(str(score[0]), False, playcols[0])
    sc2 = headingf.render(str(score[1]), False, playcols[1])
    screen.blit(sc1, (100, 300))
    screen.blit(sc2, (1120, 300))
    pygame.display.flip()

def WinEffect(x,y,x2,y2, xd,yd):    #Creates the win line, calls scoreupdater, and the text boxes in the middle
    if ga[x][y] == 'o':
        win = 1
        winner = "Red"
        col = playcols[1]
    else:
        win = 0
        winner = "Blue"
        col = playcols[0]
    pygame.draw.line(screen, col, (cpos[x][y][0]-xd, cpos[x][y][1]-yd), (cpos[x2][y2][0]+xd, cpos[x2][y2][1]+yd),10)
    pygame.display.flip()
    time.sleep(0.75)
    Wint = headingf.render(winner, False, col, "White")
    screen.blit(Wint, (500, 260))
    Wintx = headingf.render("Wins!", False, "White", col)
    screen.blit(Wintx, (680, 260))
    Wintxx = headingf.render("Replay?", False, "White", 'Black')
    screen.blit(Wintxx, (553, 400))
    ScoreUpdater(win)
    pygame.display.flip()

def Play(x, y, t):  #Updates board, places x's and o's
    if ga[x][y] is '':
        ga[x][y] = t
        print(ga)
        for i in range(len(grayscale)):
            if t == 'x':
                pygame.draw.line(screen, grayscale[i], (cpos[x][y][0]-45, cpos[x][y][1]-45), (cpos[x][y][0]+45, cpos[x][y][1]+45),10)
                pygame.draw.line(screen, grayscale[i], (cpos[x][y][0]+45, cpos[x][y][1]-45), (cpos[x][y][0]-45, cpos[x][y][1]+45),10)
                if i == 0: 
                    for p in range(10):
                        pygame.draw.line(playind, (playcols[0][0],playcols[0][1],playcols[0][2], 20-2*p), (cpos[x][y][0]-60, cpos[x][y][1]+60+p), (cpos[x][y][0]+60, cpos[x][y][1]+60+p))
                        screen.blit(playind, (0,0))
                    pygame.draw.rect(playind, (0,0,0,0), (cpos[x][y][0]-60, cpos[x][y][1]+60, 121, 20))
            if t == 'o':
                pygame.draw.circle(screen, grayscale[i], (cpos[x][y][0], cpos[x][y][1]), 45,10)
                if i == 0: 
                    for p in range(10):
                        pygame.draw.line(playind, (playcols[1][0],playcols[1][1],playcols[1][2], 20-2*p), (cpos[x][y][0]-60, cpos[x][y][1]+60+p), (cpos[x][y][0]+60, cpos[x][y][1]+60+p))
                        screen.blit(playind, (0,0))
                    pygame.draw.rect(playind, (0,0,0,0), (cpos[x][y][0]-60, cpos[x][y][1]+60, 121, 20))
            time.sleep(0.05)
            pygame.display.flip()
        return(True)
    else: return(False)

def PlayIndicator(c):   #Updates effects for whose turn it is
    pygame.draw.rect(screen, 'Black', (0, 630, 1280, 90), 60)
    for i in range(90):
        pygame.draw.line(playind, (c[0],c[1],c[2], 1), (0, 720-i), (1280, 720-i))
        screen.blit(playind, (0,0))
        pygame.display.flip()
        time.sleep(0.003)
    pygame.draw.rect(playind, 'Black', (0, 630, 1280, 720), 60)

def greset():   #Resets board
    for i in range(130):
        pygame.draw.line(screen, "black", (300+i*5, 90),(300+i*5, 630), 5)
        if 369 < round(i*5+300) < 910:
            pygame.draw.line(screen, "white", (370, 270), (round(370+i*4.154), 270),10)
            pygame.draw.line(screen, "white", (370, 450), (round(370+i*4.154), 450),10)
        if round(i*5+300) > 555:
            pygame.draw.line(screen, "white", (550, 90), (550, 630),10)
        if round(i*5+300) > 735:
            pygame.draw.line(screen, "white", (730, 90), (730, 630),10)
        time.sleep(0.01)
        pygame.display.flip()

while running:  #Frame by frame calling of code
    if intro == True:
        startAnim()
        PlayIndicator(playcols[0])
        intro=False
        Mustxx = headingf.render("Music", False, "White")
        MusArtxx = normf.render("Move on Old Friend - Half Human", False, "White")
        pygame.draw.line(screen, "yellow", (1070, 560), (1040, 560),10)
        pygame.draw.line(screen, "green", (1240, 560), (1270, 560),10)
        screen.blit(Mustxx, (1090, 530))
        screen.blit(MusArtxx, (1042, 580))

    ms = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Game == True:
                if 370 < ms[0] < 910 and 90 < ms[1] < 630:
                    if ms[0] < 550:
                        sqx = 0
                    elif ms[0] < 730:
                        sqx = 1
                    elif ms[0] < 910:
                        sqx = 2

                    if ms[1] < 270:
                        sqy = 0
                    elif ms[1] < 450:
                        sqy = 1
                    elif ms[1] < 630:
                        sqy = 2
                
                    if Play(sqx, sqy, turn) == True:
                        if turn == 'x':
                            turn = 'o'
                            PlayIndicator(playcols[1])
                        else:
                            turn = 'x'
                            PlayIndicator(playcols[0])
                    if GameCheck() == True:
                        Game = False
            else:
                if 550 < ms[0] < 725 and 400 < ms[1] < 450:
                    greset()
                    Game = True
                    ga = [['','',''],['','',''],['','','']]
            if 1040 < ms[0] < 1070 and 550 < ms[1] < 570:
                v-=0.1
                pygame.mixer.music.set_volume(v)
            if 1240 < ms[0] < 1270 and 550 < ms[1] < 570:
                v+=0.1
                pygame.mixer.music.set_volume(v)
    pygame.display.flip()
    dt = timer.tick(60)/1000

pygame.quit()