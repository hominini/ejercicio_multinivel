from datetime import date

class Bonds:

    meta_propia = 'meta_propia'
    quincena = 'quincena'
    liderazgo = 'liderazgo'
    trimestral = 'trimestral'

    def __init__(self):
        # self.sale = sale
        pass

    # def __repr__(self):
    #     return "recibe {} por bono tipo {}".format(self.)

    
    @classmethod
    def calculate_bonds(cls, team_member):
        bonds = []
        all_sales = team_member.get_sales()
        # print(cls.calculate_meta_propia_bonds(all_sales))
        bonds = bonds + cls.calculate_meta_propia_bonds(all_sales)
        return bonds
        
    @classmethod
    def calculate_meta_propia_bonds(cls, sales):
        meta_propia_bonds = []
        for transaction in sales:
            if transaction.amount >= 5000.00 and transaction.amount < 10000.00:
                meta_propia_bonds.append({'type': cls.meta_propia, 'bond_amount': 150.00})
            elif transaction.amount >= 10000.00 and transaction.amount < 15000.00:
                meta_propia_bonds.append({'type': cls.meta_propia, 'bond_amount': 200.00})
            elif transaction.amount >= 15000.00 and transaction.amount < 25000.00:
                meta_propia_bonds.append({'type': cls.meta_propia, 'bond_amount': 300.00})
            elif transaction.amount >= 25000.00:
                meta_propia_bonds.append({'type': cls.meta_propia, 'bond_amount': 400.00})

        return meta_propia_bonds

    @classmethod
    def calculate_team_bonds(cls, team_leader):
        bonds = []
        all_sales = team_member.get_sales()
        # print(cls.calculate_meta_propia_bonds(all_sales))
        bonds = bonds + cls.calculate_meta_propia_bonds(all_sales)
        return bonds
