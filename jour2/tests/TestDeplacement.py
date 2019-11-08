import unittest
import numpy as np

from Voiture.moves import move_cars


class TestDeplacement(unittest.TestCase):
    def setUp(self):
        self.list_cars = [
            {
                "marque": "Mercedes",
                "position": np.array([0,0]),
                "direction": np.array([0,1])
            }
        ]
    
    def testAvancer(self):
        move_cars(self.list_cars)
        self.assertTrue((self.list_cars[0]["position"] == np.array([0,1])).all())

    def testDebordement(self):
        for i in range(11):
            move_cars(self.list_cars)
            self.assertTrue((self.list_cars[0]["position"] < np.array([10,10])).all())
            self.assertTrue((self.list_cars[0]["position"] >= np.array([0,0])).all())
            
    
