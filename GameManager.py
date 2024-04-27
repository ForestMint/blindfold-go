import sente

class GameManager():
    def __init__(self,size,handicap):
        self.game=game = sente.Game(size, sente.rules.JAPANESE)
        self.blindfolded_player_is_black=True

    def is_blindfolded_player_black(self):
        return self.blindfolded_player_is_black
    
    def is_game_over(self):
        return False
    
    def is_move(self,size):
        return True
    
    
    def is_playable_move(self,size):
        return True

    def play_move(self, move):
        pass

    def request_move_from_AI(self):
        return ""