# configuration settings
from config import main_number_of_choices

# menu files
from medical_records.medical_main import medical_main
from health_status.health_status import health_main

# Entry point

while True:

    print("""
    Welcome to Medicode!
    --------------------
    * Enter [1] for Medical Records Section
    * Enter [2] for Health Section
    * Enter [3] for COVID-19 Section
    * Enter [4] for Blood Section
    * Enter [5] for Emergency Section
    * Enter [6] for First Aid Section
    * Enter [7] for Schedule Section
    * Enter [8] to exit
    --------------------
    """)

    choice = int(input(">   "))

    if choice not in main_number_of_choices:
        print("------------------------")
        print("Please enter a valid choice!")
        print("------------------------")

    else:
        if choice == 1:
            print("Entering medical records..")
            print("------------------------")
            medical_main()

        elif choice == 2:
            print("Entering health section..")
            print("------------------------")
            health_main()

        elif choice == 3:
            print("Entering covid section..")
            print("------------------------")

        elif choice == 4:
            print("Entering blood section..")
            print("------------------------")

        elif choice == 5:
            print("Entering emergency section..")
            print("------------------------")

        elif choice == 6:
            print("Entering first aid section..")
            print("------------------------")

        elif choice == 7:
            print("Entering schedule section..")
            print("------------------------")

        elif choice == 8:
            print("Exiting Medicode...")
            exit()
