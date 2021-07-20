import unittest
from morty import Morty

class MortyTests(unittest.TestCase):
    def test_universe(self):
        morty= Morty(111)
        self.assertEqual(morty.universe, 111)

    def test_is_assigned(self): #ovo mi je za treci zadatak, test metod koji proverava da li je morty assignovan
        morty= Morty(111)
        self.assertFalse(morty.is_assigned)

if __name__ == '__main__':
    unittest.main()
#test za mortija