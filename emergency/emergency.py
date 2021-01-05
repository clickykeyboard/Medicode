from config import Configuration


def emergency_main():
    while True:
        print(f""" 
        Welcome to the Emergency Status Menu
        {Configuration.medium_dashes}
        * Enter [1] to request an ambulance
        * Enter [2] to go back
        {Configuration.medium_dashes}
        """)

        choice = int(input(">   "))
        if choice not in Configuration.emergency_number_of_choices:
            print(f"{Configuration.small_dashes}")
            print("Please enter a valid choice!")
            print(f"{Configuration.small_dashes}")

        else:
            if choice == 1:
                for _ in range(1):
                    print("Request an ambulance.")
                    print(f"{Configuration.long_dashes}")
                    print("Please wait...")
                    print(f"{Configuration.long_dashes}")
                    print("An ambulance has been dispatched to your address and will arrive shortly.")
                    print(f"{Configuration.long_dashes}")



            elif choice == 2:
                print("Going back...")
                print(f"{Configuration.long_dashes}")
                break
