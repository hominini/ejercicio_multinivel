class Comission:

    comissions_percents = [0.03, 0.012, 0.0012, 0.0008, 0.0006]

    def __init__(self, member_id, transaction_id, comission_amount):
        self.member_id = member_id
        self.transaction_id = transaction_id
        self.comission_amount = comission_amount

    def __repr__(self):
        return "{} obtiene una comision de {}$".format(self.member_id, round(self.comission_amount, 4))
