import unittest

from ..Konto import KontoFirmowe

class TestBusinessAccountCreation(unittest.TestCase):

    # feature 7
    def test_business_account_creation(self):
        account = KontoFirmowe("Firma", "1234567890")

        self.assertEqual(account.nazwa_firmy, "Firma", "Nazwa firmy nie zapisana poprawnie")
        self.assertEqual(account.nip, "1234567890", "NIP nie zapisany poprawnie")

    # feature 7
    def test_invalid_nip(self):
        account = KontoFirmowe("Firma", "123456789")
        self.assertEqual(account.nip, "Niepoprawny NIP!", "NIP should be marked as invalid if not 10 digits.")

    # feature 7
    def test_transactions(self):
        account = KontoFirmowe("Firma", "1234567890")
        account.receiving_money(100)
        self.assertEqual(account.saldo, 100, "Receiving money should add to saldo.")

        second_account = KontoFirmowe("DrugieKonto", "0000000000")
        account.sending_money(50, second_account)
        self.assertEqual(account.saldo, 50, "Sending money should subtract from saldo.")
        account.sending_money(150, second_account)
        self.assertEqual(account.saldo, 50, "Sending more money than available should not be possible.")