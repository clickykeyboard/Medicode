# configuration settings
from blood_status.blood_status import blood_status_main
from config import Configuration
from emergency.emergency import emergency_main
from health_status.health_status import health_main
# menu files
from medical_records.patient_main import patient_main

# Entry point

while True:

    print("""
    Welcome to Medicode!
    --------------------
    * Enter [1] for Patient History
    * Enter [2] for Medical History / Records
    * Enter [3] for Blood Section
    * Enter [4] for Scheduling an Appointment
    * Enter [5] for COVID-19 Section
    * Enter [6] for Emergency

    * Enter [7] to exit
    --------------------
    """)

    choice = int(input(">   "))

    if choice not in Configuration.main_number_of_choices:
        print("------------------------")
        print("Please enter a valid choice!")
        print("------------------------")

    else:
        if choice == 1:
            print("Entering patient section..")
            print("------------------------")
            patient_main()

        elif choice == 2:
            print("Entering medical history section..")
            print("------------------------")
            health_main()

        elif choice == 3:
            print("Entering blood section..")
            print("------------------------")

        elif choice == 4:
            print("Entering schedule sction..")
            print("------------------------")
            blood_status_main()

        elif choice == 5:
            print("Entering COVID section..")
            print("------------------------")
            emergency_main()

        elif choice == 6:
            print("Entering emergency section..")
            print("------------------------")

        elif choice == 7:
            print("Exiting Medicode...")
            exit()
