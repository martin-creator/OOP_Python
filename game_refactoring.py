"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""

from random import randint


def run_game(num_players: int = 2):

    scores = [0 for _ in range(num_players)]

    player_1_score = 0
    player_2_score = 0

    while True:

        for i, score in enumerate(scores):
            roll = randint(1, 6)
            scores[i] += roll
            print(f"Player {i+1} rolled {roll} and now has a score of {scores[i]}")
            if scores[i] >= 100:
                print(f"Player {i+1} wins!")
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
    run_game(num_players=2)
