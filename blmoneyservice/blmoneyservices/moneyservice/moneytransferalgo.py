import random


class Variablez:
    def __init__(self):
        self.y = None
        self.x = None
        self.total_amount = None
        self.commission = None
        self.percentage1 = 0.06
        self.percentage2 = 0.08

        self.usd_Rub_Buying = 60
        self.usd_Rub_Selling = 59
        self.zmw_usd_buying = 17
        self.zmw_usd_selling = 16.5

    def rub2kwacha(self, amnt, usd_rub_buying, zmw_usd_selling):
        self.x = amnt / usd_rub_buying
        self.y = self.x * zmw_usd_selling

        # calculate commission
        if self.x <= 200:
            self.commission = self.y * self.percentage2
        else:
            self.commission = self.y * self.percentage1
        self.total_amount = self.y + self.commission

        return round(self.y, 2), round(self.x, 2), self.commission, self.total_amount

    def kwacha2rub(self, amount, zmw_usd_buying, usd_rub_selling):
        self.x = amount / zmw_usd_buying
        self.y = self.x * usd_rub_selling

        # calculate commission
        if self.x <= 200:
            self.commission = self.y * self.percentage2
        else:
            self.commission = self.y * self.percentage1
        self.total_amount = self.y + self.commission

        return round(self.y, 2), round(self.x, 2), self.commission, self.total_amount

    def mtcn(self, last_id_in_db):
        num = random.randint(10, 50)
        n = last_id_in_db + 1
        return f"MTC-00{n}{num}BLMS"