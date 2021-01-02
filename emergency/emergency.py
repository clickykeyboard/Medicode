from config import Configuration


class Emergency:
    def __init__(self, emergency_history, room_number):
        self.emergency_history = emergency_history
        self.room_number = room_number

    def get_emergency_history(self):
        return self.emergency_history

    def get_room_number(self):
        return self.room_number

    def set_emergency_history(self, new_emergency_history):
        self.emergency_history = new_emergency_history

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number


def emergency_main():
    while True:
        print(f""" 
        Welcome to the Emergency Status Menu
        {Configuration.medium_dashes}
        * Enter [1] to check for Emergency Status
        * Enter [2] to go back
        {Configuration.medium_dashes}
        """)

        choice = int(input(">   "))
        if choice not in Configuration.emergency_status_number_of_choices:
            print(f"{Configuration.small_dashes}")
            print("Please enter a valid choice!")
            print(f"{Configuration.small_dashes}")

        else:
            if choice == 1:
                print("Choice 1")

            elif choice == 2:
                print("Going back...")
                print(f"{Configuration.long_dashes}")
                break
