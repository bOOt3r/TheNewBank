class Account:

    def __init__(self, c_id, ssn, name, acc_id, acc_type, balance):
        self.c_id = int(c_id)
        self.ssn = int(ssn)
        self.name = name
        self.acc_id = int(acc_id)
        self.acc_type = acc_type
        self.balance = float(balance)

