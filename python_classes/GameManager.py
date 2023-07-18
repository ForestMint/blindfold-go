
from Game import Game
from AI import AI
from Move import Move
import string
import random

class GameManager():

    def __init__(self,size,number_of_handicap_stones):
        self.game=Game(size,number_of_handicap_stones)
        self.ai=AI()

        random_bits = random.getrandbits(1)
        self.blindfolded_player_is_black= bool(random_bits)
        self.black_to_play=number_of_handicap_stones==0










        # let's set the list of existing moves
        # by "existing moves", I mean all the moves that exist on a board the size of the one we are playing on plus "pass" and "resign"
        # maybe I will later implement the possibility for the AI to play the move "undo" but not for now
        # then, all the existing moves on a 9x9 board are the 81 stone moves plus "pass" and "resign", meaning a 83 items list must be returned
        # on a 19x19 board, it is 19x19+2 = 361+2 = 363 items list
        # of course, from this list of "existing moves" we will later need to get a list of "playable moves"
        # by "playable moves", I mean the moves that are allowed according to the rules of go
        # so to get the playable moves from the existing moves, we will have to delete :
        #   - the moves on an intersection that is already occupied by a stone
        #   - the moves on a free intersection that are suicide
        #   - the moves on a free intersection that are not suicide but that would send the game back to a situation met previously, 
        #       making those moves forbidden by the rule of ko
        goban_size=len(self.game.goban.matrix)
        list_of_abscissae=list(string.ascii_uppercase)
        list_of_abscissae.remove("I")
        list_of_abscissae=list_of_abscissae[0:goban_size]
        list_of_ordinates=range(1,goban_size+1)
        self.list_of_existing_moves=[]
        for abscissa in list_of_abscissae:
            for ordinate in list_of_ordinates:
                self.list_of_existing_moves.append(abscissa+str(ordinate))
        self.list_of_existing_moves.append("pass")
        self.list_of_existing_moves.append("resign")











    def request_move_from_AI(self):
        list_of_playable_moves= self.list_playable_moves()
        return self.ai.randomly_pick_a_playable_move(self.game, list_of_playable_moves)
        
    def is_blindfolded_player_black(self):
        return self.blindfolded_player_is_black

    def is_game_over(self):
        return self.game.is_over_for_some_reason()

    def is_playable_move(self, candidate_move):

        if candidate_move.get_computer_coordinates=={"abscissa":"", "ordinate":""}: 
            return False
        else: 
            #print("game_manager.is_playable_move()")
            #print(self.game.is_intersection_empty(candidate_move))
            return self.game.is_intersection_empty(candidate_move)

    def play_move(self, move):
        if move.is_pass():
            self.pass_move()
        elif move.is_resign():
            self.resign_game()
        else:
            letters_coordinates = list(string.ascii_uppercase)
            letters_coordinates.remove("I")
            abscissa=move.get_computer_coordinates()["abscissa"]
            ordinate=move.get_computer_coordinates()["ordinate"]
            stone_is_black=True
            self.game.goban.add_stone(abscissa, ordinate, stone_is_black=self.black_to_play)
            self.black_to_play=self.black_to_play==False

    @staticmethod
    def is_move(candidate_speech,goban_size):
        list_of_abscissae=list(string.ascii_uppercase)
        list_of_abscissae.remove("I")
        list_of_abscissae=list_of_abscissae[0:goban_size]
        list_of_ordinates=range(1,goban_size+1)
        list_of_moves=[]
        for abscissa in list_of_abscissae:
            for ordinate in list_of_ordinates:
                #list_of_moves.append(Move(abscissa,ordinate).get_go_name())
                list_of_moves.append(abscissa+str(ordinate))
        list_of_moves.append("pass")
        list_of_moves.append("resign")
        #list_of_moves.append("undo")
        #print(list_of_moves)
        #print("game_manager.is_move()")
        #print(candidate_speech in list_of_moves)
        #print(list_of_moves)
        return candidate_speech in list_of_moves
            


    def list_existing_moves(self):
        goban_size=self.game.goban.size
        list_of_existing_moves=[]
        list_of_abscissae=range(0,goban_size)
        list_of_ordinates=range(0,goban_size)
        for abscissa in list_of_abscissae :
            for ordinate in list_of_ordinates :
                list_of_existing_moves.append(Move(abscissa, ordinate))
        return list_of_existing_moves

    def print_position(self):
        self.game.print_position()

    def list_playable_moves(self):
        list_of_existing_moves=self.list_existing_moves()
        list_of_playable_moves=[]
        for existing_move in list_of_existing_moves:
            if (self.game.is_intersection_empty(existing_move) and not(self.game.is_move_forbidden_because_of_the_rule_of_ko(existing_move)) and not(self.game.is_move_suicide(existing_move,stone_is_black=True))):
                list_of_playable_moves.append(existing_move)
        list_of_playable_moves.append("pass")
        list_of_playable_moves.append("resign")
        return list_of_playable_moves

    def blindfolded_player_starts(self, handicap):
        if self.blindfolded_player_is_black and handicap ==0: 
            return True
        elif self.blindfolded_player_is_black==False and handicap>1:
            return True
        else:
            return False



if __name__ == "__main__":
    my_game_manager=GameManager()