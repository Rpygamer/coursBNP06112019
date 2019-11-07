import os
from time import sleep
from random import randint

import numpy as np

from Voiture.display import display_board
from Voiture.moves import move_cars


list_positions = [ np.array([randint(0,9), randint(0,9)]) for i in range(8)]
list_cars = [
    {"marque": "Mercedes", "position": pos, "direction": np.array([0,1])}
    for pos in list_positions
]

for i in range(15):
    os.system("cls")
    display_board(list_cars)
    list_cars = move_cars(list_cars)
    sleep(0.5)
