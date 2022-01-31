#innehåller infomation om klassen Customer

class Customer:

    def __init__(self, c_id, ssn, name):
        self.c_id = int(c_id)
        self.ssn = int(ssn)
        self.name = name