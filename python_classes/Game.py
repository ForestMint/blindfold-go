from Goban import Goban
from Chain import Chain

class Game():

    def __init__(self,size,number_of_handicap_stones):
        self.goban=Goban(size,number_of_handicap_stones)
        self.list_of_moves=[]
        self.number_of_prisoners_for_black=0
        self.number_of_prisoners_for_white=0
        self.black_just_has_passed=False
        self.white_just_has_passed=False
        self.black_has_resigned=False
        self.white_has_resigned=False



    def is_over_for_some_reason(self):
        return self.is_over_because_both_players_just_passed() or self.is_over_because_resignation()

    def is_over_because_both_players_just_passed(self):
        return (self.black_just_has_passed and self.white_just_has_passed)

    def is_over_because_resignation(self):
        return (self.black_has_resigned or self.white_has_resigned)

    def add_stone(self,move):
        pass

    def winner_is_black(self):
        return True

    def translate_move_from_computer_coordinates_to_go_coordinates(self,abscissa,ordinate):
        return {"go_coordinates":"A1"}

    def translate_move_from_go_coordinates_to_computer_coordinates(self,move):
        return {"computer_coordinates":[0,1]}

    def is_move_forbidden_because_of_the_rule_of_ko(self,abscissa,ordinate):
        return False






    def proceed_captures_if_any(self):
        # this function will check if there are stones that are captured by the last move played
        # if yes, this function will call the removal of those captured stones from the board
        # if not, this function will do nothing further

        
        if self.list_of_moves[:-1]["move"] in ["pass","undo","resign"]:
            # first, if the move just played was not a stone move, there can be no capture to be processed
            pass
        else:
            # otherwise, some stones of the other color than the one just played might be captured

            # for each stone of the other color than the last stone played on the board
            for row in self.goban.matrix:
                for intersection in row:
                    if self.list_of_moves[:-1]["player"]!=intersection:
                        pass
                    else:
                        # let's calculate the number of liberties that the chain including this stone has
                        # if the number of liberties is 0 then add this stone to the list of stones to capture 
                        # and all the stones on capture list will be captured at the same moment at the end of this process
                        # (since capturing stones within the loop would re-give liberties to the other stones of the chain)
                        list_of_intersections_in_chain=[]
                        my_chain=Chain(intersection,self.goban.matrix)




        








if __name__ == "__main__":
    my_game=Game()