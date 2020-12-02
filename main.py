# configuration settings
from config import main_number_of_choices

# menu files
from medical_records.medical_main import medical_main

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
    --------------------
    """)

    choice = int(input(">   "))

    if choice not in main_number_of_choices:
        print("Please enter a valid choice!")

    else:
        if choice == 1:
            print("Entering medical records..")
            medical_main()

        elif choice == 2:
            print("Entering health section..")

        elif choice == 3:
            print("Entering covid section..")

        elif choice == 4:
            print("Entering blood section..")

        elif choice == 5:
            print("Entering emergency section..")

        elif choice == 6:
            print("Entering first aid section..")

        elif choice == 7:
            print("Entering schedule section..")
