"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""

from random import randint


class Player:
    def __init__(self, player_num):
        self.num = player_num
        self.score = 0

    def take_turn(self):
        roll = randint(1, 6)
        self.score += roll
        print(f"{self.num}: {self.score} (rolled a {roll})")

    def has_won(self, target_score):
        return self.score >= target_score

    def __str__(self):
        return f"Player {self.num}"

    def __repr__(self):
        return f"Player({self.num})"


def run_game(num_players: int = 2, target_score: int = 100):

    players = [Player(i + 1) for i in range(num_players) ]

    while True:
        for player in players:
            player.take_turn()

            if player.has_won(target_score=100):
                print(f"{player.num} wins!")
                return
        # player_1_roll = randint(1, 6)
        # player_1_score += player_1_roll
        # print(f"Player 1 rolled {player_1_roll} and now has a score of {player_1_score}")
        # if player_1_score >= 100:
        #     print("Player 1 wins!")
        #     return


        # player_2_roll = randint(1, 6)
        # player_2_score += player_2_roll
        # print(f"Player 2 rolled {player_2_roll} and now has a score of {player_2_score}")
        # if player_2_score >= 100:
        #     print("Player 2 wins!")
        #     return



if __name__ == '__main__':
    run_game(num_players=2, target_score=100)
