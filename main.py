import chess
import AiEngine as cEngine
board=chess.Board()
def playHumanMove():
    print(board.legal_moves)
    play= input()
    board.push_san(play)
def playEngineMove(board,maxDepth,color):
    engine=cEngine.Engine(board,maxDepth,color)
    board.push(engine.getBest())
def start():
    global board
    color = input("Play as (b or w): ")
    maxDepth = int(input("Choose depth: "))
    if color=="b":
        while(board.is_checkmate()==False) :
             print("Thinking \n")
             playEngineMove(board,maxDepth, chess.WHITE)
             print(board)
             playHumanMove()
             print(board)
        print(board)
        print(board.outcome)
    elif color=="w":
        while(board.is_checkmate()==False) :
             print(board)
             playHumanMove()
             print(board)
             print("Thinking \n")
             playEngineMove(board,maxDepth, chess.BLACK)
        print(board)
        print(board.outcome)
def main():
    start()
    return 0

if __name__=="__main__":
    main()