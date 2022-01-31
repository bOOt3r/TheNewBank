class Account:

    def __init__(self, cust_id, ssn, name, acc_id = 0, acc_type = "debit account", balance = 0.00):
        self.cust_id = int(cust_id)
        self.ssn = int(ssn)
        self.name = name
        self.acc_id = int(acc_id)
        self.acc_type = acc_type
        self.balance = float(balance)

