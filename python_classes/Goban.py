from colorama import init
from termcolor import colored
from colorama import Fore, Back, Style
init()


class Goban():

    def __init__(self,size,number_of_handicap_stones):
        self.size=size
        self.matrix=[]
        for i in range(0,size): 
            row = ["empty"]*size
            self.matrix.append(row)

        if size==9:
            coordinates_of_hoshis={
                "top-left":[2,6],
                "top":[4,6],
                "top-right":[6,6],
                "left":[2,4],
                "tengen":[4,4],
                "right":[6,4],
                "bottom-left":[2,2],
                "bottom":[4,2],
                "bottom-right":[6,2]
            }
        if size==13:
            coordinates_of_hoshis={
                "top-left":[3,9],
                "top":[6,9],
                "top-right":[9,9],
                "left":[3,6],
                "tengen":[6,6],
                "right":[9,6],
                "bottom-left":[3,3],
                "bottom":[6,3],
                "bottom-right":[9,3]
            }
        if size==19:
            coordinates_of_hoshis={
                "top-left":[3,15],
                "top":[9,15],
                "top-right":[15,15],
                "left":[3,9],
                "tengen":[9,9],
                "right":[15,9],
                "bottom-left":[3,3],
                "bottom":[9,3],
                "bottom-right":[15,3]
            }
        if number_of_handicap_stones!=0:
            if number_of_handicap_stones ==2:
                hoshis_for_handicap_stones=["bottom-left","top-right"]
            elif number_of_handicap_stones ==3:
                hoshis_for_handicap_stones=["bottom-left","top-left","top-right"]
            elif number_of_handicap_stones ==4:
                hoshis_for_handicap_stones=["bottom-left","top-left","bottom-right","top-right"]
            elif number_of_handicap_stones ==5:
                hoshis_for_handicap_stones=["bottom-left","top-left","bottom-right","top-right","tengen"]
            elif number_of_handicap_stones ==6:
                hoshis_for_handicap_stones=["bottom-left","left","top-left","bottom-right","right","top-right"]
            elif number_of_handicap_stones ==7:
                hoshis_for_handicap_stones=["bottom-left","left","top-left","bottom-right","right","top-right","tengen"]
            elif number_of_handicap_stones ==8:
                hoshis_for_handicap_stones=["bottom-left","left","top-left","bottom-right","right","top-right","bottom","top"]
            elif number_of_handicap_stones ==9:
                hoshis_for_handicap_stones=["bottom-left","left","top-left","bottom-right","right","top-right","bottom","top","tengen"]

            for hoshi_for_handicap_stone in hoshis_for_handicap_stones:
                coordinates=coordinates_of_hoshis[hoshi_for_handicap_stone]
                self.add_stone(coordinates[0],coordinates[1],True)

    def print(self):


        display_matrix=[]
        for i in range(0,len(self.matrix[0])):
            line=[]
            for j in range(0,len(self.matrix[0])):
                line.append(self.matrix[j][i])
            display_matrix.append(line)

        
                

        reversed_matrix=[]
        for i in range(0,len(self.matrix[0])):
            reversed_matrix.append(display_matrix[len(self.matrix[0])-i-1])
          




        for row in reversed_matrix:
            for item in row:
                if item in ['black','white']:new_item="0" 
                else : new_item="+"
                if item in ('black'):  # or `if item in "+-|"`
                    color = Fore.RED
                elif item in ('white'): # or `if item in "12345"`
                    color = Fore.GREEN
                else: 
                    color = Fore.WHITE
                print(f"{color}{new_item}", end=' ')   # I add `space` instead of `\n` as `end` 

                '''
                text = colored(new_item, 'green','on_red')
                print(text, end=' ')
                '''
            print() # go to next line

    

    def add_stone(self,abscissa,ordinate,stone_is_black):
        if stone_is_black:
            self.matrix[abscissa][ordinate]="black"
        else:
            self.matrix[abscissa][ordinate]="white"

    def is_same_situation(self, situation):
        return situation == self.matrix

    def remove_stone(self,abscissa,ordinate):
        self.matrix[abscissa][ordinate]="empty"

    def is_intersection_empty(self,abscissa,ordinate):
        return self.matrix[abscissa][ordinate]=="empty"

    def is_move_suicide(self,abscissa,ordinate,stone_is_black):
        return False





if __name__ == "__main__":
    my_goban=Goban()