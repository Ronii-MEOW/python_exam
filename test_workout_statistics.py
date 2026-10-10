import unittest
from workout_statistics import count_calories

class TestCountCalories(unittest.TestCase):

    def test_count_calories_no(self):
        calories = count_calories(120,47,20,45,"N")
        self.assertEqual(calories, 309.8127390057)
    def test_count_calories_ferfi(self):
        calories = count_calories(137,75,28,60,"F")
        self.assertEqual(calories, 744.1778202677)
    def test_count_calories_ferfi_negativ_edzeshossz(self):
        calories = count_calories(137,75,28,-15,"F")
        self.assertEqual(calories, -186.0444550669)
    def test_count_calories_ferfi_0_edzeshossz(self):
        calories = count_calories(137,75,28,0,"F")
        self.assertEqual(calories, 0)