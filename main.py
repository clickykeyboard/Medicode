# configuration settings
from config import Configuration
from emergency.emergency import emergency_main
# menu files
from patient_records.patient_main import patient_main
from medical_history.medical_history import medical_main
from blood_status.blood_status import blood_section_main
from covid.covid import covid_main
from schedule.schedule import schedule_main

# Entry point

while True:

    print(f"""
    Welcome to Medicode!
    { Configuration.small_dashes }
    * Enter [1] for Patient Information
    * Enter [2] for Medical History / Records
    * Enter [3] for Blood Section
    * Enter [4] for Schedule an Appointment
    * Enter [5] for COVID-19 Section
    * Enter [6] for Emergency

    * Enter [7] to exit
    { Configuration.small_dashes }
    """)

    choice = int(input(">   "))

    if choice not in Configuration.main_number_of_choices:
        print(f"{ Configuration.long_dashes }")
        print("Please enter a valid choice!")
        print(f"{ Configuration.long_dashes }")

    else:
        if choice == 1:
            print("Entering patient section..")
            print(f"{ Configuration.long_dashes }")
            patient_main()

        elif choice == 2:
            print("Entering medical history section..")
            print(f"{ Configuration.long_dashes }")
            medical_main()

        elif choice == 3:
            print("Entering blood section..")
            print(f"{ Configuration.long_dashes }")
            blood_section_main()

        elif choice == 4:
            print("Entering schedule section..")
            print(f"{ Configuration.long_dashes }")
            schedule_main()

        elif choice == 5:
            print("Entering COVID section..")
            print(f"{ Configuration.long_dashes }")
            covid_main()
        elif choice == 6:
            print("Entering emergency section..")
            print(f"{ Configuration.long_dashes }")
            emergency_main()

        elif choice == 7:
            print("Exiting Medicode...")
            exit()
