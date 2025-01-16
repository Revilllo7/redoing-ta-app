import unittest

from ..Konto import KontoOsobiste

def test_personal_account_creation(self):
    account = KontoOsobiste("Jan", "Kowalski")

    self.assertEqual(account.imie, "Jan", "Imie nie zapisane poprawnie")
    self.assertEqual(account.nazwisko, "Kowalski", "Nazwisko nie zapisane poprawnie")
    self.assertEqual(account.saldo, 0, "Saldo nie zainicjalizowane poprawnie - nie jest zerowe.")