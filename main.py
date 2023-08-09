import pygame
from Checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from constants_api import FPS
from Checkers.game import Game
from minimax.algorithm import minimax, get_all_moves
#from Checkers.board import white_kings

#Display the game
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

# Set the game name
pygame.display.set_caption('Checkers')

# Get the row and col by the position of the mouse
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


# Execute the gamme
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    max_turns = 100
    
    while run:
        clock.tick(FPS)      
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game, -100, +100)
            game.ai_move(new_board)
            max_turns = max_turns-1
            #print(self.white_kings)


        if game.turn == RED:
            value, new_board = minimax(game.get_board(), 3, None, game, -100, +100)
            game.ai_move(new_board) 
            max_turns = max_turns-1
            
        if game.winner() != None:
            print(game.winner())
            run = False
            
        if max_turns == 0:
            print('tie')
            run = False            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()            # original position of the piece
                row, col = get_row_col_from_mouse(pos)  # assign the original position to row and col 
                game.select(row, col)
      
        # game update       
        game.update()
        

    pygame.quit()

main()