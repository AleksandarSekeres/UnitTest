import unittest
from citadel import Citadel
from rick import Rick
from morty import Morty

class CitadelTest(unittest.TestCase):
    def test_get_all_residents(self): #prvo pravim unittest koji uzima sve residente iz citadela
        citadel= Citadel()
        residents= citadel.get_all_residents()
        self.assertCountEqual(residents, [])

    def test_add_residents(self): #pa dodao test koji dodaje residente citadeli, implementirao ih sve u citadel klasi
        citadel= Citadel()
        rick= Rick(111)
        morty= Morty(111)

        citadel.add_resident(rick)
        citadel.add_resident(morty)
        residents= citadel.get_all_residents()
        self.assertEqual(residents[0], rick) #prvo dodajem ricka pa ocekujem da je 0 na listi a drugi bi trebao biti morty
        self.assertEqual(residents[1], morty)

    def test_picle_ricks_with_morties(self):
        citadel= Citadel()
        rick= Rick(111)
        morty= Morty(111)
        rick.assign(morty)

        citadel.add_resident(rick)
        citadel.add_resident(morty)

        citadel.picle_ricks_with_morties()
        residents= citadel.get_all_residents()

        self.assertTrue(residents[0].is_pickle)

if __name__ == '__main__':
    unittest.main()