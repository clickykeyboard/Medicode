Medicode   
An app for patients provided by a hospital

        Database:

            One patient data is stored in a dictionary form

            {
                patient_name,
                patient_age,
                patient_date_of_birth,
                patient_gender,
                patient_contact,
                patient_location,
                patient_cnic,
                patient_pin,
                patient_blood_group,
                records: {
                    (records of 
                    injuries,
                    illnesses,
                    diseases,
                    mental_illness,
                    disability,

                },
                appointments

            }

        ----------------------------------------

        1 - Provides information about the patient
          - Request to update information
            - CNIC required to update information and pin

        2 - Medical history of patient / Record of patient
          - Injuries, Illnesses, Diseases, Mental Illnesses, Disability

        3 - Blood section
          - If patient wants to donate or request blood
            - Patient can submit a form to donate / request blood

        4 - Scheduling
          - A patient can schedule an appointment
            - Department list

        5 - COVID-19
          - Information about COVID-19, precautions
          - Beds available in hospital for COVID patients

        6 - Emergency
          - Request an ambulance to your location