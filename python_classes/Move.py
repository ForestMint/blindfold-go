
import string

class Move():

    def __init__(self, abscissa, ordinate):
        self.abscissa = abscissa
        self.ordinate = ordinate

    def get_computer_coordinates(self):
        return {"abscissa":self.abscissa, "ordinate":self.ordinate}

    def get_go_name(self):
        letters_coordinates = list(string.ascii_uppercase)
        letters_coordinates.remove("I")
        return letters_coordinates[self.abscissa]+str(self.ordinate+1)
        


        