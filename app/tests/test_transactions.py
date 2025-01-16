import unittest

from ..Konto import KontoOsobiste, KontoFirmowe

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
        second_account = KontoOsobiste("Drugie", "Konto", "00000000000")
        account.sending_money(50, second_account)
        self.assertEqual(account.saldo, 50, "Sending money should subtract from saldo.")
        third_account = KontoOsobiste("Trzecie", "Konto", "00000000000")
        account.sending_money(50, third_account)
        self.assertEqual(account.saldo, 0, "Sending money should subtract from saldo.")

    # feature 6
    def test_sending_money_not_enough(self):
        account = KontoOsobiste("Jan", "Kowalski", "62010112345")
        account.receiving_money(100)
        second_account = KontoOsobiste("Drugie", "Konto", "00000000000")
        account.sending_money(150, second_account)
        self.assertEqual(account.saldo, 100, "Sending more money than available should not be possible.")

    # feature 7
    def test_receiving_money_business(self):
        account = KontoFirmowe("Firma", "1234567890")
        account.receiving_money(100)
        self.assertEqual(account.saldo, 100, "Receiving money should add to saldo.")
    
    # feature 7
    def test_sending_money_business(self):
        account = KontoFirmowe("Firma", "1234567890")
        account.receiving_money(100)
        second_account = KontoOsobiste("Drugie", "Konto", "00000000000")
        account.sending_money(50, second_account)
        self.assertEqual(account.saldo, 50, "Sending money should subtract from saldo.")

    # feature 7
    def test_sending_money_not_enough_business(self):
        account = KontoFirmowe("Firma", "1234567890")
        account.receiving_money(100)
        second_account = KontoOsobiste("Drugie", "Konto", "00000000000")
        account.sending_money(150, second_account)
        self.assertEqual(account.saldo, 100, "Sending more money than available should not be possible.")

    # feature 8
    def test_express_transfer(self):
        account = KontoOsobiste("Jan", "Kowalski", "62010112345")
        account.receiving_money(100)
        second_account = KontoFirmowe("DrugieKonto", "0000000000")
        account.send_express_transfer(50, second_account)
        self.assertEqual(account.saldo, 49, "Sending money should subtract from saldo and add 1 for express transfer.")

    # feature 8
    def test_express_transfer(self):
        account = KontoFirmowe("Firma", "1234556780")
        account.receiving_money(100)
        second_account = KontoFirmowe("DrugieKonto", "0000000000")
        account.send_express_transfer(50, second_account)
        self.assertEqual(account.saldo, 45, "Sending money should subtract from saldo and add 5 for express transfer.")