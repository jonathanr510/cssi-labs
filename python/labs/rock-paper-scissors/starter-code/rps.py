#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
print("Welcome to RPS!")
import random


def get_player_move():
    playerMove = raw_input("Enter a move Rock(1), Paper(2), Scissors(3): ")
    return playerMove

def get_computer_move():
    compMove =  random.randint(1, 6)
    return compMove
def determine_winner(player_move, comp_move):
    if player_move == comp_move:
        return "tie"
    elif (player_move == "r" and comp_move == "s") or \
         (player_move == "s" and comp_move == "p") or \
         (player_move == "p" and comp_move == "r"):
        return "player"
    else:
        return "computer"


def print_scoreboard(player_wins, comp_wins, ties):

    print("Player Score: %s" % player_wins)
    print("Computer Score: %s" % comp_wins)
    print("Ties: %s" % ties)

def get_move_name(short_move):

    if short_move == 'r':
        return "Rock"
    elif short_move == 'p':
        return "Paper"
    else:
        return "Scissors"


# Write your code below - make RPS happen using the functions above!

print(get_player_move)
print(compMove)
print(determine_winner)
print(scoreboard)
print(get_move_name)
