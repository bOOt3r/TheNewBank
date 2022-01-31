from numpy import c_, empty
import classes.customer as c
import classes.account as a

class Bank:
    #listor som håller information om kunder internt i klassen
    hold_c = []
    hold_a = []

    #läser in textfilen, sorterar den och lägger rätt uppgifter om kunden på rätt ställe i customer klassen
    def _load(self):
        customers = []
        with open("c_db.txt", "rt") as f:
            for line in f:
                customers.append(line.strip().split(":"))
            for line in customers:
                Bank.hold_c.append(c.Customer(line[0], line[1], line[2]))
                if IndexError(line[3]):
                    pass
                else:
                    Bank.hold_a.append(a.Account(line[0], line[1], line[2], line[3], line[4], line[5]))
    
    #presenterar all data på alla kunder OM textfilen finns
    def get_customers(self):
        if not Bank.hold_c:
            print("Inga kunder registrerade")
        else:
            print("ID,    Personnummer, Namn")
            for x in Bank.hold_c:
                print(f"{x.c_id}, {x.ssn}, {x.name}")
    
    #visar information om ett konto (ej klar)
    def get_account(self, acc_id):
        for x in Bank.hold_a:
            if x.acc_id == acc_id:
                print(f'Owner: {x.name}, {x.pnr}\nAccount: {x.acc_id}, {x.acc_type}, {x.balance}')
                break
        else:
            print(a.Account(acc_id))
            print(f'Did not find account: {acc_id}. Did you type it correctly?')

    #söker efter kundens "ssn" i textfilen, om den inte finns läggs en ny kund till på sista raden
    def add_customer(self, ssn, name):
        c_id = []
        for y in Bank.hold_c:
            if ssn == "" or name == "":
                print("Fältet får ej vara tomt.")
                break
            elif y.ssn == ssn:
                print(f'Det finns redan en kund med personnummer {ssn}')
                break
        else:
            print(f"{name} med personnummer {ssn} är nu kund i TheNewBank")
            with open("./c_db.txt", "r+t") as f:
                for x in f:
                    cs = x.split(":")
                    c_id.append(cs[0])
                c_id = int(c_id[-1]) + 1

                dbw = str(c_id) + ":" + str(ssn) + ":" + name + ":"
                f.write("\n")
                f.write(str(dbw))

    #söker efter kundens "c_id" i textfilen, hittas den så tas raden med kunden bort
    def delete_customer(self, c_id):
        for y in Bank.hold_c:
            if c_id == "":
                print("Fältet får ej vara tomt.")
            elif c_id == y.c_id:
                with open("./c_db.txt" , "r+t") as f:
                    new_f = f.readlines()
                    f.seek(0)
                    for line in new_f:
                        if str(c_id) not in line:
                            f.write(line)
                    f.truncate()

    #söker efter kundens "c_id" i textfilen och ersätter gammalt namn med nytt namn
    def change_customer_name(self, c_id, name):
        for y in Bank.hold_c:
            if c_id == "" or name == "":
                print("Fältet får ej vara tomt.")
                break
            elif y.c_id == c_id:
                o_v = str(y.ssn) + ":" + y.name
                n_v = str(y.ssn) + ":" + name
                f = open("./c_db.txt", "rt")
                filedata = f.read()
                f.close()
                new_data = filedata.replace(o_v, n_v)
                f = open("./c_db.txt", "wt")
                f.write(new_data)
                f.close()
                print(f'Ok, namnet på kundnummer {y.c_id}, ändrades från {y.name} till {name}')
                break
        else:
            print(f"{c_id} är inte ett registrerat kundnummer")




