import json
class Stats:
    def __init__(self):
        self.scores = 0
        self.game_active = False
        self.load_high_score()

    def save_high_score(self):
        with open('high_score.json', 'w') as file_object:
            json.dump(self.high_score, file_object)

    def load_high_score(self):
        try:
            with open('high_score.json', 'r') as file_object:
                self.high_score = json.load(file_object)

        except:
            self.high_score = 0





        
