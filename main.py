from classes.bank import *
from classes.customer import Customer as c

if __name__ == '__main__':
    b = Bank()
    b._load()

    ui = True
    while ui:
        print("Välkommen till TheNewBank!")
        print("1. Se kunder")
        print("2. Se konton")
        print("3. Skapa kund")
        print("4. Ändra namn på kund")
        print("5. Radera kund")
        print("6. Avsluta")

        ui = input("Gör ett val\n")


        if ui == "1":
            b.get_customers()
            input("Tryck på ENTER för att återgå.")

        if ui == "2":
            while True:
                try:
                    acc_id = int(input("Enter account number of the account you wish to see information about: "))
                    b.get_account(acc_id)
                    input("Tryck på ENTER för att återgå")
                    break
                except ValueError:
                    print("Någonting blev fel, försök igen!")
                except KeyboardInterrupt:
                    print("\nÅtergår till huvudmenyn")
                    input("Tryck på ENTER för att återgå")
                    break

        if ui == "3":
            while True:
                try:
                    ssn = int(input("Fyll i kundens personnummer:\n"))
                    name = input("Fyll i kundens namn:\n")
                    b.add_customer(ssn, name)
                    input("Tryck på ENTER för att återgå")
                    break
                except ValueError:
                    print("Någonting blev fel, försök igen!")
                except KeyboardInterrupt:
                    print("\nÅtergår till huvudmenyn")
                    input("Tryck på ENTER för att återgå")
                    break

        if ui == "4":
            while True:
                try:
                    c_id = int(input("Fyll i kundnummer för kund du vill ändra namnet på\n"))
                    name = input("Fyll i det fullsätndiga nya namnet\n")
                    b.change_customer_name(c_id, name)
                    input("Tryck på ENTER för att återgå")
                    break
                except ValueError:
                    print("Någonting blev fel, försök igen!")
                except KeyboardInterrupt:
                    print("\nÅtergår till huvudmenyn")
                    input("Tryck på ENTER för att återgå")
                    break
        
        if ui == "5":
            while True:
                try:
                    c_id = int(input("Fyll i kundnummer för den kund du vill radera\n"))
                    b.delete_customer(c_id)
                    input("Tryck på ENTER för att återgå")
                    break
                except ValueError:
                    print("Någonting blev fel, försök igen!")
                except KeyboardInterrupt:
                    print("\nÅtergår till huvudmenyn")
                    input("Tryck på ENTER för att återgå")
                    break

        if ui == "6":
            quit()
