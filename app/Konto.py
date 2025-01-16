# feature_7: adding brand accounts and object programming
class KontoBazowe:
    def __init__(self):

        self.saldo = 0

    # feature_6: transactions - sending and receieving money
    def receiving_money(self, amount):
        self.saldo += amount

    def sending_money(self, amount, account_to_send):
        if self.saldo < amount:
            return False
        
        self.saldo -= amount
        account_to_send.receiving_money(amount) # some account we send money to
        return True



class KontoOsobiste(KontoBazowe):
    def __init__(self, imie, nazwisko, pesel, rabat: str | None = None):
        super().__init__()
        # Feature_2: add pesel to account ^
        # Feature_3: add pesel validation (11 digits)
        if len(pesel) != 11:
            pesel = "Niepoprawny pesel!"

        self.imie = imie
        self.nazwisko = nazwisko
        self.rabat = rabat
        self.pesel = pesel

        # Feature_4: add promo codes that add +50 to saldo if starts with "PROM_[XYZ]"
        if self.is_eligible_for_promotion():
            self.saldo = 50

    def is_eligible_for_promotion(self):
        if self.rabat is None:
            return False
        
        if not self.rabat.startswith("PROM_"):
            return False
        
        # Feature_5: promo only applies to people born after 1960
        # check if the first 2 digits are less than 60
        # if digit 3 and 4 are less than 12, it means born before 2000
        if int(self.pesel[:2]) < 60 and int(self.pesel[2:4]) <= 12:
            return False
        
        return True
    
    # feature_8: express transfer
    def send_express_transfer(self, account_to_send, amount):
        if self.saldo < amount:
            return False
        
        self.saldo -= amount + 5
        account_to_send.receiving_money(amount)
        return True



# feature_7: adding brand accounts and object programming
class KontoFirmowe(KontoBazowe):
    def __init__(self, nazwa_firmy, nip):
        super().__init__()
        self.nazwa_firmy = nazwa_firmy
        self.nip = nip

        if not self.validate_nip():
            self.nip = "Niepoprawny NIP!"

    def validate_nip(self):
        if len(self.nip) != 10:
            return False
        
        if not self.nip.isnumeric():
            return False
        
        return True

    # feature_8: express transfer
    def send_express_transfer(self, amount, account_to_send):
        if self.saldo < amount:
            return False
        
        self.saldo -= amount + 5
        account_to_send.receiving_money(amount)
        return True