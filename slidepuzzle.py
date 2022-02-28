import pygame
import random
pygame.init()
size = (900,700)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
over = False
menu = False
slideto = ""

End = True
Mainmenu = True
gamescreen = False
End = False
board = []
finishedboard = []

def starting_board():
    x = 1
    for z in range(len(board)):
        for y in range(len(board)):
            r = random.randint(0, len(board)-1)
            c = random.randint(0, len(board)-1)
            while board[r][c] != 0:
                r = random.randint(0, len(board)-1)
                c = random.randint(0, len(board)-1)

            if x != len(board) **2:
                board[r][c] = x
            else:
                board[r][c] = 0
            x += 1

def solve_board():
    a = 1
    for r in range(len(board)):
        for c in range(len(board)):
            if a != len(board)**2:
                board[r][c] = a
                a += 1
            else:
                board[r][c] = 0


def make_zero():
    for r in range(len(board)):
        for c in range(len(board)):
            board[r][c] = 0

def getempthy():
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                return (r,c)


def function(move):
    click = move
    blankx, blanky = getempthy()

    if click == "right":
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
    if click == "left":
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
    if click == "up":
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]

    if click == "down":
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]

def boundaries(move):
    blankx, blanky = getempthy()
    tryslide = move
#     cheaking x axis
    if tryslide == "left":
        if blanky+1 < len(board[0]):
            return True
    elif tryslide == "right":
        if blanky-1 >= 0:
            return True

    elif tryslide == "up":
        if blankx+1 < len(board):
            return True
    elif tryslide == "down":
        if blankx-1 >= 0:
            return True
    else:
        return False

def menu():
    global rect_level1,rect_level2,rect_level3
    title = TITLE.render("Welcome to sliding Puzzle", False, (255, 255, 255))
    Level1 = font.render("Level 1", False, (255, 255, 255))
    rect_level1 = pygame.draw.rect(screen, (0, 0, 0), (387, 372,Level1.get_width(),Level1.get_height()))
    Level2 = font.render("Level 2", False, (255, 255, 255))
    rect_level2 = pygame.draw.rect(screen,(0,0,0),(387, 472,Level2.get_width(),Level2.get_height()))
    Level3 = font.render("Level 3", False, (255, 255, 255))
    rect_level3 = pygame.draw.rect(screen, (0, 0, 0), (387, 572, Level3.get_width(), Level3.get_height()))
    screen.blit(title, (125, 272))
    screen.blit(Level1, (387, 372))
    screen.blit(Level2, (387, 472))
    screen.blit(Level3, (387, 572))

def draw():
    global new_rect,solve_rect,Quit_rect
    screen.fill((0, 0, 0))

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] != 0:
                pygame.draw.rect(screen,(0,204,0),(c*(700/int(len(board))),r*(700/int(len(board))),(700/int(len(board)))-1,(700/int(len(board)))-1))
                test = font.render(str(board[r][c]),False,(0,0,0))
                screen.blit(test,(c*(700/int(len(board))) + float((700/int(len(board)))/2) - 16,r*(700/int(len(board))) +float((700/int(len(board)))/2) - 16))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (c * (700/int(len(board))), r * (700/int(len(board))), (700/int(len(board))), (700/int(len(board)))))

    newgame = font.render("New Game", False, (255, 255, 255))
    new_rect = pygame.draw.rect(screen, (0, 0, 0),
                                (720, 500, newgame.get_width(), newgame.get_height()))
    screen.blit(newgame, (720, 500))

    solve = font.render("Solve", False, (255, 255, 255))
    solve_rect = pygame.draw.rect(screen, (0, 0, 0),(720, 600, solve.get_width(), solve.get_height()))
    screen.blit(solve, (720, 600))

    Quit = font.render("Quit",False,(255,255,255))
    Quit_rect = pygame.draw.rect(screen, (0, 0, 0),(720, 400, Quit.get_width(), Quit.get_height()))
    screen.blit(Quit,(720, 400))


font = pygame.font.Font('freesansbold.ttf', 32)
TITLE = pygame.font.Font('freesansbold.ttf',50)
keydown = True
while not over:
    global rect_level1,rect_level2,rect_level3,solve_rect,new_rect,Quit_rect

    # if Intro:
    #     screen.blit(TITLE.render("Press enter",False,(255,255,255)),(700/2,700/2))
    if Mainmenu:
      screen.fill((0, 0, 0))
      menu()
      Mainmenu = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True
        if event.type == pygame.KEYDOWN and keydown:
            if event.key == pygame.K_RETURN and End:
                End = False
                Mainmenu = True
            if event.key == pygame.K_UP and boundaries("up") and gamescreen:
                slideto = "up"
            elif event.key == pygame.K_DOWN and boundaries("down") and gamescreen:
                slideto = "down"
            elif event.key == pygame.K_LEFT and boundaries("left") and gamescreen:
                slideto = "left"
            elif event.key == pygame.K_RIGHT and boundaries("right") and gamescreen:
                slideto = "right"
            keydown = False

        if event.type == pygame.KEYUP:
            keydown = True


        if event.type == pygame.MOUSEBUTTONDOWN and Mainmenu:
            if rect_level1.collidepoint(event.pos) and Mainmenu:
                board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                finishedboard = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
                starting_board()
                draw()
                Mainmenu = False
                gamescreen = True
            if rect_level2.collidepoint(event.pos) and Mainmenu:
                board = [[0, 0, 0,0], [0, 0, 0,0], [0, 0, 0,0],[0, 0, 0,0]]
                finishedboard = [[1, 2, 3,4], [5, 6, 7,8], [9, 10, 11,12],[13, 14, 15,0]]
                starting_board()
                draw()
                Mainmenu = False
                gamescreen = True

            if rect_level3.collidepoint(event.pos) and Mainmenu:
                board = [[0, 0, 0,0,0], [0, 0, 0,0,0], [0, 0, 0,0,0],[0, 0, 0,0,0],[0, 0, 0,0,0]]
                finishedboard = [[1, 2, 3,4,5], [6, 7, 8,9,10], [11, 12, 13,14,15],[16, 17, 18,19,20],[21, 22, 23,24,0]]
                starting_board()
                draw()
                Mainmenu = False
                gamescreen = True
        if event.type == pygame.MOUSEBUTTONDOWN and gamescreen:
            if solve_rect.collidepoint(event.pos) and gamescreen:
                solve_board()
                draw()

            if new_rect.collidepoint(event.pos) and gamescreen:
                make_zero()
                starting_board()
                draw()
            if Quit_rect.collidepoint(event.pos) and gamescreen:
                gamescreen = False
                screen.fill((0, 0, 0))
                menu()
                Mainmenu = True

    if slideto:
        function(slideto)
        draw()
    slideto = ""

    pygame.display.update()
    if board == finishedboard:
        gamescreen = False
        screen.fill((0,0,0))
        end = font.render("you win",False,(255,255,255))
        pressenter = font.render("press enter",False,(255,255,255))
        screen.blit(end,(450-int(end.get_width()/2),700/2))
        screen.blit(pressenter,(450-int(pressenter.get_width()/2),550))
        End = True

pygame.quit()