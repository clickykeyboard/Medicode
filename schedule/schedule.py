from config import Configuration


def schedule_main():
    while True:
        print(f"""
        Welcome to the Schedule Appointment Menu!
        {Configuration.medium_dashes}
        * Enter [1] to check to Schedule Appointment
        * Enter [2] to go back
        {Configuration.medium_dashes}
        """)

        choice = int(input(">   "))
        if choice not in Configuration.schedule_appointment_number_of_choices:
            print(f"{Configuration.small_dashes}")
            print("Please enter a valid choice!")
            print(f"{Configuration.small_dashes}")

        else:
            if choice == 1:
                print(Configuration.make_appointments())
                print("Choice 1")

            elif choice == 2:
                print("Going back...")
                print(f"{Configuration.medium_dashes}")
                break
