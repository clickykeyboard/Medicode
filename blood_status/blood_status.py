from config import Configuration


class Blood_Status:
    def __init__(self, donating_blood, requesting_blood):
        self.donating_blood = donating_blood
        self.requesting_blood = requesting_blood

    def get_donating_blood(self):
        return self.donating_blood

    def get_requesting_blood(self):
        return self.requesting_blood

    def set_donating_blood(self, new_donating_blood):
        self.donating_blood = new_donating_blood

    def set_requesting_blood(self, new_requesting_blood):
        self.requesting_blood = new_requesting_blood


def blood_status_main():
    while True:
        print(""" 
        Welcome to the Emergency Status Menu
        ----------------------
        * Enter [1] to check for Blood Acceptors
        * Enter [2] to request Blood Donors
        * Enter [3] to go back
        ----------------------
        """)

        choice = int(input(">   "))
        if choice not in Configuration.blood_status_number_of_choices:
            print("----------------")
            print("Please enter a valid choice!")
            print("----------------")

        else:
            if choice == 1:
                print("Choice 1")

            elif choice == 2:
                print("Choice 2")

            elif choice == 3:
                print("Going back...")
                print("------------------------")
                break
