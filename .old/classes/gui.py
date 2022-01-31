import os
from classes.bank import Bank as b

clear = lambda: os.system('clear')  # Rensa consolen för Mac/Linux
#clear = lambda: os.system('cls')   # Rensa consolen för Windows

class GUI:


    
    def start_menu():
        clear()
        print(10* "-")
        print("Välkommen till TheNewBank")
        print("1. Logga in")
        print("2. Skapa konto")
        print("3. Avsluta")
        print("4. Se kunder")
        print(10* "-")
        ui = input("Välj ett alternativ.\n")

        if ui == "4":
            b.get_customers()

