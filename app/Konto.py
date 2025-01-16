class KontoOsobiste:
    def __init__(self, imie, nazwisko, pesel, rabat: str | None = None):
        
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
        else:
            self.saldo = 0
        pass

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

    # feature_6: transactions - sending and receieving money
    def receiving_money(self, amount):
        self.saldo += amount

    def sending_money(self, amount):
        if self.saldo < amount:
            return False
        else:
            self.saldo -= amount
            return True

