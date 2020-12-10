from config import Configuration

def schedule_main():
    while True:
        print(""" 
        Welcome to the Schedule Appointment Menu!
        ----------------------
        * Enter [1] to check to Schedule Appointment
        * Enter [2] to go back
        ----------------------
        """)

        choice = int(input(">   "))
        if choice not in Configuration.schedule_appointment_number_of_choices:
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