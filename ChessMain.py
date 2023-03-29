""" prende l'input del giocatore e mostra lo stato della partita"""
import pygame as p
import os
from chessgame import ChessEngine
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

"""INIZIALIZZERÀ UN DIZIONARIO GLOBALE CON LE IMMAGINI DEI PEZZI"""
def load_images():
    for fileName in os.listdir("/home/teo/PycharmProjects/chessGame/chessgame/images"):
        fileName = fileName[:2]
        IMAGES[fileName] = p.transform.scale(p.image.load(f"images/{fileName}.png"),(SQ_SIZE,SQ_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    #crea un gamestate, oggetto della classe GameState
    gs = ChessEngine.GameState()
    load_images()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False


        draw_gamestate(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()

"""def make_move(screen,gs,riga,colonna):

"""
def draw_gamestate(screen,gs):
    draw_board(screen)
    draw_pieces(screen,gs.board)

def draw_board(screen):
    colors = [p.Color("white"),p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((c+r) % 2)]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

def draw_pieces(screen,board):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if board[i][j] != "--":
                screen.blit(IMAGES[board[i][j]],p.Rect(j*SQ_SIZE,i*SQ_SIZE,SQ_SIZE,SQ_SIZE))

main()