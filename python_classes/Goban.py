
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

        for row in self.matrix:
            print(row)

    def add_stone(self,abscissa,ordinate,stone_is_black):
        if stone_is_black:
            self.matrix[abscissa][ordinate]="black"
        else:
            self.matrix[abscissa][ordinate]="white"

    def remove_stone(self,abscissa,ordinate):
        self.matrix[abscissa][ordinate]="empty"

    def is_intersection_empty(self,abscissa,ordinate):
        print(abscissa)
        print(ordinate)
        return self.matrix[abscissa][ordinate]=="empty"

    def is_move_suicide(self,abscissa,ordinate,stone_is_black):
        return False





if __name__ == "__main__":
    my_goban=Goban()