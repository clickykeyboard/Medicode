from config import Configuration


class Blood_Status:
    def __init__(self, donating_blood, requesting_blood):
        self.donation_blood = donating_blood
        self.requesting_blood = requesting_blood

    def get_donating_blood(self):
        return self.donating_blood

    def get_requesting_blood(self):
        return self.requesting_blood

    def set_donating_blood(self, new_donating_blood):
        self.donating_blood = new_donating_blood

    def set_requesting_blood(self, new_requesting_blood):
        self.requesting_blood = new_requesting_blood


def blood_section_main():
    while True:
        print(f""" 
        Welcome to the Blood Section Menu
        {Configuration.medium_dashes}
        * Enter [1] to check for Blood Acceptors
        * Enter [2] to request Blood Donors
        * Enter [3] to go back
        {Configuration.medium_dashes}
        """)

        choice = int(input(">   "))
        if choice not in Configuration.blood_section_number_of_choices:
            print(f"{Configuration.small_dashes}")
            print("Please enter a valid choice!")
            print(f"{Configuration.small_dashes}")

        else:
            if choice == 1:
                print("Choice 1")

            elif choice == 2:
                print("Choice 2")

            elif choice == 3:
                print("Going back...")
                print(f"{Configuration.medium_dashes}")
                break
