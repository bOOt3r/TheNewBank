
from genericpath import exists
#from classes.account import Account as a
from classes.customer import Customer as c
from classes.dataSource import *

class TxtReader(DataSource):

    def __init__(self,t_path="/dataBase/customer_transaction.txt",c_path="dataBase/customer_database.txt"):
        """Initializes datasource with paths, checks if paths exists and creates objects from data in paths"""
        self.transactions_path = t_path
        self.customer_path = c_path
        self.conn()
        self.load_transactions()
        self.load_customers()

    def conn(self):
        """Checks if paths to data is valid, exits otherwise"""
        if exists(self.customer_path) & exists(self.transactions_path):
            return (self.customer_path,exists(self.customer_path),self.transactions_path,exists(self.transactions_path))
        else:
            print('error')
            exit()

    def load_customers(self):
        """Reads customer path and creates objects from file"""
        self.objects = []
        self.customers = self.get_all_customers()
        for customer in self.customers:
            self.accounts = []
            bid = customer.split(':')[0]
            name = customer.split(':')[1]
            id = customer.split(':')[2]
            account_str = customer.split(':')[3]
            if ('#') in account_str:
                multiple_accounts = account_str.split('#')
                for account in multiple_accounts:
                    number=account.split('-')[0]
                    balance=account.split('-')[2]
                    self.accounts.append(a(number,self.get_transactions(id,number),balance))
                self.objects.append(c(bid,id,name,self.accounts))
            elif not '-' in account_str:
                    self.objects.append(c(bid,id,name,self.accounts))
            else:
                number=account_str.split('-')[0]
                balance=account_str.split('-')[2]
                self.accounts.append(a(number,self.get_transactions(id,number),balance))
                self.objects.append(c(bid,id,name,self.accounts))