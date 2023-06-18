

class AI():
    def __init__(self):
        pass

    def randomly_pick_a_playable_move(self,game):
        '''
        abscissa = rand()
        ordinate = rand()

        while is_playable_move(abscissa, ordinate) ==False:
            abscissa = rand()
            ordinate = rand()  

        return translate_move_from_computer_coordinates_to_go_coordinates(abscissa, ordinate)
        '''
        return "E4"



if __name__ == "__main__":
    my_ai=AI()