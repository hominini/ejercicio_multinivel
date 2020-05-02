from collections import deque
import transaction as tx
import comissions as cms
from bonds import Bonds


class TeamMember:

    _sales_total = 0.0

    def __init__(self, id, leader_ref, child_members=[], ventas=0):
        self.leader_ref = self._add_parent(leader_ref)
        self.child_members = child_members
        self.id = id
        self.sales = []
        self.comissions = []
        self.bonos = []

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id

    def get_my_level(self):
        level = 1
        while self.leader_ref != None:
            self = self.leader_ref
            level = level + 1
        return level

    def _add_parent(self, parent):
        # si el argumento pasado es nulo retorna el padre
        if parent == None:
            return parent
        # si el padre pasado existe agregar self como hijo, retornar el padre
        else:
            parent.child_members.append(self)
            return parent

    # breadtfirst traversal
    def print_subtree(self):
        queue = deque([self])
        # mientras haya elementos en la cola
        while queue:
            n = len(queue)
            while n > 0:
                p = queue.popleft()
                print(p.id, ' ', end=' ')
                for elem in p.child_members:
                    queue.append(elem)
                n = n - 1
            print()

    # guarda una registro de venta para este miembro del equipo
    def sell(self, amount, date_time):
        transaction = tx.Transaction(self.id, amount, date_time)
        self.sales.append(transaction)
        self.set_parents_comissions(transaction)

    # obtener todas las ventas de este miembro del equipo
    def get_sales(self):
        return self.sales

    # obtener todas las comisiones de este miembro del equipo
    def get_comissions(self):
        return self.comissions
    
    def get_bonds(self):
        return Bonds.calculate_bonds(self)

    def set_parents_comissions(self, transaction):
        cms_stack = cms.Comission.comissions_percents.copy()

        # agregar comisiones a todos los lideres de este miembro
        while self.leader_ref:
            comission_percent = cms_stack.pop(0)
            comission_total = transaction.amount * comission_percent
            self.comissions.append(cms.Comission(
                self.id, transaction.date_time, comission_total))
            self = self.leader_ref

        # agregar comision al ultimo miembro de la piramide
        comission_percent = cms_stack.pop(0)
        comission_total = transaction.amount * comission_percent
        self.comissions.append(cms.Comission(
            self.id, transaction.date_time, comission_total))

    def calculate_sales_total(self, parent):
        for sale in parent.get_sales():
            self._sales_total = self._sales_total + sale.amount
        for child in parent.child_members:
            self.calculate_sales_total(child)
    
    def get_sales_total(self):
        self._sales_total = 0.0
        self.calculate_sales_total(self)
        return self._sales_total

    @classmethod
    def get_by_id(self, id):
        pass
