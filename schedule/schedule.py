from datetime import datetime

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
                print(
                    f"""The date today is: {datetime.now().strftime("%I:%M %p - %d %B, %Y")}""")

                available_appointments = Configuration.make_appointments()

                print("The following slots are available for you: ")

                for number, appointment in enumerate(available_appointments):
                    print(number + 1)
                    print(f"{Configuration.small_dashes}")
                    print(f"""Doctor name: {appointment["doctor_name"]}""")
                    print(
                        f"""Specialization: {appointment["specialization"]}""")
                    print(f"""Timing: {appointment["timing"]}""")
                    print(f"{Configuration.small_dashes}")

                print("Which specialist would you like to schedule an appointment with?")

                appointment_choice = int(input("> "))
                print(f"{Configuration.small_dashes}")
                print(
                    f"""You have scheduled an appointment with {available_appointments[appointment_choice - 1]["doctor_name"]}""")
                print(
                    f"""The following are your timings: {available_appointments[appointment_choice - 1]["timing"]}""")
                print(f"{Configuration.small_dashes}")
                input("Enter anything to continue...")

            elif choice == 2:
                print("Going back...")
                print(f"{Configuration.medium_dashes}")
                break
