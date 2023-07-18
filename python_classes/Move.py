
import string

class Move():

    def __init__(self, *args):
        '''
            constructor overloading based on args
        '''
        if len(args)>1:
            self.abscissa = args[0]
            self.ordinate = args[1]
        else:
            if args==("",):
                self.abscissa = ""
                self.ordinate = ""
            else:
                if (len(args[0])in[2,3]):
                    letters_coordinates = list(string.ascii_uppercase)
                    letters_coordinates.remove("I")
                    if (args[0][:1] in list(string.ascii_uppercase) and args[0][-1:] in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']) :

                        self.abscissa=int(letters_coordinates.index(args[0][:1]))
                        self.ordinate=int(args[0][-1:])-1
                    else:
                        self.abscissa = ""
                        self.ordinate = ""                     
                else:
                    self.abscissa = ""
                    self.ordinate = ""
                     

    def get_computer_coordinates(self):
        return {"abscissa":self.abscissa, "ordinate":self.ordinate}

    def get_go_name(self):
        letters_coordinates = list(string.ascii_uppercase)
        letters_coordinates.remove("I")
        return letters_coordinates[self.abscissa]+str(self.ordinate+1)

    def is_pass(self):
        return False

    def is_resign(self):
        return False
        


        