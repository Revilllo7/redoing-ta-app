import unittest

from ..Konto import KontoOsobiste

class TestPersonalAccountCreation(unittest.TestCase):

    # feature 1
    def test_personal_account_creation(self):
        test1 = KontoOsobiste("Jan", "Kowalski", "12345678901")

        self.assertEqual(test1.imie, "Jan", "Imie nie zapisane poprawnie")
        self.assertEqual(test1.nazwisko, "Kowalski", "Nazwisko nie zapisane poprawnie")
        self.assertEqual(test1.saldo, 0, "Saldo nie zainicjalizowane poprawnie - nie jest zerowe.")

    # feature 2
    def test_pesel_assignment(self):
        account = KontoOsobiste("Jan", "Kowalski", "12345678901")
        self.assertEqual(account.pesel, "12345678901", "PESEL should be correctly assigned if valid.")

    # feature 3
    def test_pesel_validation(self):
        account = KontoOsobiste("Jan", "Kowalski", "12345")
        self.assertEqual(account.pesel, "Niepoprawny pesel!", "PESEL should be marked as invalid if not 11 digits.")

    # feature 4
    def test_promo_code_applies_saldo(self):
        account = KontoOsobiste("Jan", "Kowalski", "62010112345", "PROM_XYZ")
        self.assertEqual(account.saldo, 50, "Promo code should add 50 to saldo if conditions are met.")

    # feature 4
    def test_promo_code_no_saldo(self):
        account = KontoOsobiste("Jan", "Kowalski", "62010112345", "INVALID")
        self.assertEqual(account.saldo, 0, "Invalid promo code should not add to saldo.")

    # feature 5
    def test_promo_code_birth_year_before_1960(self):
        account = KontoOsobiste("Jan", "Kowalski", "59010112345", "PROM_XYZ")
        self.assertEqual(account.saldo, 0, "Promo code should not apply to people born before 1960.")

    # feature 5
    def test_promo_code_birth_year_after_1960(self):
        account = KontoOsobiste("Jan", "Kowalski", "60010112345", "PROM_XYZ")
        self.assertEqual(account.saldo, 50, "Promo code should apply to people born after 1960.")

    # feature 5
    def test_promo_code_birth_month_after_2000(self):
        account = KontoOsobiste("Jan", "Kowalski", "02210112345", "PROM_XYZ")
        self.assertEqual(account.saldo, 50, "Promo code should apply to people born after 2000.")

    # feature 5
    def test_no_promo_code(self):
        account = KontoOsobiste("Jan", "Kowalski", "62010112345")
        self.assertEqual(account.saldo, 0, "No promo code should result in 0 saldo.")
