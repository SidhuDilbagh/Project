import chess
import random
class Engine:
    def __init__(self,board,maxDepth, colour):
        self.board=board
        self.maxDepth=maxDepth
        self.colour=colour
    def CheckMate(self):
        if(self.board.is_checkmate()):
            if(self.board.turn==self.colour):
                return -9999999
            else:
                return 9999999
        else:
            return 0
    def SquareValue(self,square):
        val=0
        if(self.board.piece_type_at(square) == chess.PAWN):
            val = 1
        elif (self.board.piece_type_at(square) == chess.ROOK):
            val = 5.1
        elif (self.board.piece_type_at(square) == chess.BISHOP):
            val = 3.33
        elif (self.board.piece_type_at(square) == chess.KNIGHT):
            val = 3.2
        elif (self.board.piece_type_at(square) == chess.QUEEN):
            val = 8.8
        if (self.board.color_at(square)!=self.colour):
            return -val
        else:
            return val
    def Eval(self):
        value=0
        for i in range(64):
            value+=self.SquareValue(chess.SQUARES[i])
        value+=self.CheckMate()+random.random()
        return value
    def engine(self, candidate, depth):
        if depth==self.maxDepth or self.board.legal_moves.count()==0:
            return self.Eval()
        else:
            moveLst=list(self.board.legal_moves)
            candidateMove=None
            if depth%2==0:
                candidateMove=float("inf")
            else:
                candidateMove=float("-inf")
            for i in moveLst:
                self.board.push(i)
                value=self.engine(candidateMove,depth+1)
                if value > candidateMove and depth%2!=0:
                    if depth==1:
                        move=i
                    candidateMove=value
                elif value<candidateMove and depth%2==0:
                    candidateMove=value
                if candidate!=None and value<candidate and depth%2==0:
                    self.board.pop()
                    break
                if candidate!=None and value>candidate and depth%2!=0:
                    self.board.pop()
                    break
                self.board.pop()
            if depth>1:
                return candidateMove
            else:
                return move
    def getBest(self):
        return self.engine(None,1)