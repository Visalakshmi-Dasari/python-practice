from random import choice
class Game():
    def __init__(self, total_rounds):
        self.total_rounds = total_rounds
        self.compute_score = 0
        self.player_score = 0
        self.options = ['Rock', 'Paper', 'Scissors']

    def find_winner(self, compute_selection, player_sections):
        if compute_selection == 'Rock' and player_sections == 'Paper':
            self.player_score += 1
            print 'Player wins'
        elif compute_selection == 'Paper' and player_sections == 'Scissors':
            self.player_score += 1

    def play_round(self):
        computer_selection = choice(self.options)
        player_selection = raw_input('Please select one of the three - Rock, Paper, Scissors: ')
        self.find_winner(computer_selection, player_selection)

    def play_game(self):
        for round in range(self.total_rounds):
            self.play_round()

    def final_winner(self):
        if self.compute_score > self.player_score:
            return 'Computer'
        elif self.compute_score < self.player_score:
            return 'Player'
        else:
            return "Draw"

game = Game(3)
game.play_game()
print game.final_winner()
print game.play_game()




