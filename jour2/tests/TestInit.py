import unittest
import numpy as np
from Voiture.moves import move_cars


class TestInit(unittest.TestCase):
    def setUp(self):
        self.list_cars = [
            {
                "marque": "Mercedes",
                "position": np.array([0,0]),
                "direction": np.array([0,1])
            }
        ]
    
    def testInitBasic(self):
        self.assertTrue((self.list_cars[0]["position"] == np.array([0,0])).all())

    def testInitWrongType(self):
        self.list_cars[0]["position"] = "toto"
        with self.assertRaises(TypeError):
            move_cars(self.list_cars)
