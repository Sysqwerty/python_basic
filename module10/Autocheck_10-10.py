from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(payment):
        sum = 0
        for value in payment:
            if value > 0:
                sum = sum + value
        return sum