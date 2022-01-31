from classes.customer import Customer as c
from classes.account import Account as a

class Bank:

#    proc_customers = []
#    accounts = []
#    cust_id_count = 100016
#    cust_acc_count = 1030

    #Lägger förfinad data i en egen lista innan den skickas till customers listan.
    c_check = []
    
    cust_id_count = 1000


    def _load(self):
        #Tar emot den förfinade datan.
        customers = []
        #Öppnar databasen.
        with open('./dataBase/customer_database.txt') as dbrd:
        #Förfining av datan.
            for x in dbrd:
               customers.append(x.strip().split(':'))
        #Lägger den förfinade datan i en lista som sen tar respektive index, 0-2, och lägger i klassen Customer.
            for x in customers:
                Bank.customers.append(c(x[0], x[1], x[2]))
                Bank.cust_id_count += 1



    def get_customers(self):
        """Prints all customers currently registered at the bank"""
        if not Bank.c_check:
            print("No customers registered")
        else:
            for x in Bank.customers:
                print(f"ID: {x.id} Customer: {x.name} {x.ssn}")
