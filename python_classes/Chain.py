
class Chain():

    def __init__(self, intersection, goban_matrix):
        self.goban_matrix=goban_matrix
        self.intersections_in_the_chain= set()

        self.add_stone_and_stones_of_the_same_color_around(intersection)



    def add_stone_and_stones_of_the_same_color_around(self,intersection):
        intersections_around= set()
        # add the left intersection if there is one
        # add the bottom intersection if there is one
        # add the top intersection if there is one
        # add the right intersection if there is one