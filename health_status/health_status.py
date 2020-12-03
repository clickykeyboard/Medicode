from config import Configuration


def health_main():
    while True:
        print(""" 
        Welcome to the Health Status Menu
        ----------------------
        * Enter [1] to check for Health Status
        * Enter [2] to go back
        ----------------------
        """)

        choice = int(input(">   "))
        if choice not in Configuration.health_status_number_of_choices:
            print("----------------")
            print("Please enter a valid choice!")
            print("----------------")

        else:
            if choice == 1:
                print("Choice 1")

            elif choice == 2:
                print("Going back...")
                print("------------------------")
                break
