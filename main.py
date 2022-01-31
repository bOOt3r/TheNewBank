#importerar klasser
from classes.bank import *
from classes.customer import Customer as c

#kollar så att main ÄR main
if __name__ == '__main__':
    #initierar bank klassen
    b = Bank()
    b._load()

    #startar konsol applikationen
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

        #visar alla kunder i banken
        if ui == "1":
            b.get_customers()
            input("Tryck på ENTER för att återgå.")

        #visar alla uppgifter om ett visst konto (ej klar)
        if ui == "2":
            while True:
                try:
                    acc_id = int(input("Fyll i kontonummer för det konto du vill se information om"))
                    b.get_account(acc_id)
                    input("Tryck på ENTER för att återgå")
                    break
                except ValueError:
                    print("Någonting blev fel, försök igen!")
                except KeyboardInterrupt:
                    print("\nÅtergår till huvudmenyn")
                    input("Tryck på ENTER för att återgå")
                    break
        #skapar en ny kund
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
        #ändrar namn på en kund
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
        #raderar en kund
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
        #avslutar konsol applikationen
        if ui == "6":
            quit()
