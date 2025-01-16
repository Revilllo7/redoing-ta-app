import unittest

from ..Konto import KontoOsobiste

class TestTransactions(unittest.TestCase):
    
    # feature 6
    def test_receiving_money(self):
        account = KontoOsobiste("Jan", "Kowalski", "62010112345")
        account.receiving_money(100)
        self.assertEqual(account.saldo, 100, "Receiving money should add to saldo.")

    # feature 6
    def test_sending_money(self):
        account = KontoOsobiste("Jan", "Kowalski", "62010112345")
        account.receiving_money(100)
        account.sending_money(50)
        self.assertEqual(account.saldo, 50, "Sending money should subtract from saldo.")

    # feature 6
    def test_sending_money_not_enough(self):
        account = KontoOsobiste("Jan", "Kowalski", "62010112345")
        account.receiving_money(100)
        account.sending_money(150)
        self.assertEqual(account.saldo, 100, "Sending more money than available should not be possible.")