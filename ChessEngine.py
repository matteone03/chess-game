""" questa classe memorizza le informazioni sullo stato della partita
    e determina le mosse valide nello stato della partita
    memorizza anche un log delle mosse"""

class GameState():
    def __init__(self):
        #attributo della scacchiera: il primo carattere rappresenta il colore
        #il secondo carattere rappresenta il pezzo
        #la stringa "--" rappresenta uno spazio vuoto
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []
    """def make_move(self,riga,colonna):"""