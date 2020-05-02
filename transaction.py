from datetime import date

class Transaction:

    def __init__(self, member_id, amount, date_time):
        self.member_id = member_id
        self.amount = amount
        self.date_time = date_time

    def __repr__(self):
        return "{} vende {}$ el {}".format(self.member_id, round(self.amount, 2), self.date_time)