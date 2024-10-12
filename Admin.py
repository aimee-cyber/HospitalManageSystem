from Doctor import Doctor
import os
import time


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address):
        self.username = username
        self.password = password
        self.address =  address
    


# Admin Login Authentication: Sees if the username and password the user entered is valid. 
# Username: 'admin' Password: '123'

    def login(self):      
        print("-----Login-----")
        adminusername = input("Enter the Username: ")
        adminpass = input("Enter the Password: ")
        
        if adminusername == self.username and adminpass == self.password:
            print("Login Successful")
            return True
        else:
            print("Invalid Admin Credentials")
            return False
  

    def view_patients(self, patients):
        print("-----List of Patients-----")
        

        for i, patient in enumerate(patients, start=1):
            print(i, f'{patient.patient_first_name} {patient.patient_surname}', patient.patient_doctor, patient.patient_age, patient.patient_mobile, patient.patient_postcode)
            
        

    def find_index(self,index,doctors):
            # Checking that the Doctor's ID Exists           
        if 0 <= index < len(doctors):
            return index
        return None
        
          
    def view_doc(self, doctors):
        for i, doctor in enumerate(doctors, start=1):
            print(f'{i}  |  {doctor.full_name()}  |  {doctor.get_speciality()}')

    


    def doctor_management(self, doctors):
        # A method that deals with registering, viewing, updating, deleting doctors
        # The Doctor Management Menu
     while True:
        print("-----Doctor Management-----")
        print()
        print('Choose the Operation:')
        print(' [1] - Register')
        print(' [2] - View')
        print(' [3] - Update')
        print(' [4] - Delete')
        print()
        print('[5] - Exit')
        print()
        op = input("Select an Option: ")
        

        # The User Chose [1] (Register Doctor)
        if op == '1':
            os.system("cls")
            print("-----Register-----")

            # Get the Doctor's Details
            print("Enter the New Doctor's Details Below")
            print()
            newdoc_first_name = input("Doctor's First Name: ")
            newdoc_surname = input("Doctor's Surname: ")
            print()
            newdoc_speciality = input("Doctor's Speciality: ")
             
            # Check if the Name already Exists
            name_exists = False
            for doctor in doctors:
                if newdoc_first_name == doctor.get_first_name() and newdoc_surname == doctor.get_surname():
                    name_exists = True
                    break
                
            if name_exists:
                print('Name Already Exists')               
            else:         
                print('Doctor Registered')



        # The User Chose [2] (View List of Doctors)
        elif op == '2':
            print()
            print("-----List of Doctors-----")
            self.view_doc(doctors)
            
            
                
            

        # The User Chose [3] (Update Current Doctor Details)
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                self.view_doc(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index = self.find_index(index, doctors)
                    if doctor_index is not None:
                        break
                    else: 
                        print("Doctor Not Found")
                        
                except ValueError: 
                    # The Entered ID Could Not be Changed to an Int
                    print('The ID entered is Incorrect')

            # The Update Menu
            print('Choose the Field to be Updated:')
            print(' [1] First Name')
            print(' [2] Surname')
            print(' [3] Speciality')
            print()
            op = int(input('Input: ')) # Make the User Input Lowercase
            
            # The User wants to Change the First Name [1]
            if op == 1:
                newdoc_first_name = input("Enter the New First Name: ")
                doctors[doctor_index].first_name = newdoc_first_name
                print("New First Name: ", newdoc_first_name)
                print("First Name Updated Successfully")
                
                
            # The User wants to Change the Surname [2]    
            elif op == 2:
                newdoc_surname = input("Enter the New Surname: ")
                doctors[doctor_index].first_name = newdoc_surname
                print("New Surname: ", newdoc_surname)
                print("Surname Updated Successfully")
            
            
            # The User wants to Change the Speciality [3]
            elif op == 3:
                newdoc_speciality = input("Enter the New Speciality: ")
                doctors[doctor_index].speciality = newdoc_speciality
                print("New Speciality: ", newdoc_speciality)
                print("Speciality Updated Successfully")
            
            # If the User enters an invalid number    
            else: 
                print("ERROR: Invalid Choice, Please Enter a Valid Option")
        
    

                
                      

        # The User Chose [4] (Delete Current Doctor)
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view_doc(doctors)   
            
            try:   
            # The User enters the ID of the Doctor they Want to Delete
                del_doc_id = int(input('Enter the ID of the doctor to be deleted: '))
                doctor_index = self.find_index(del_doc_id - 1, doctors)
                
                if doctor_index is not None:
                    deleted_doc = doctors[doctor_index]
                    # The Chosen Doctor is Deleted
                    doctors.remove(deleted_doc)
                    # A Message is shown to tell the user the doctor is deleted successfully
                    print(f"Doctor {deleted_doc.first_name} {deleted_doc.surname} deleted successfully")
               
               # If the ID inputted doesn't exist then it will display an error message  
                else: 
                    print("Doctor Not Found")
               
            # If the user enteres a letter (for example), it will also give an error     
            except ValueError:
                print("Invalid ID, Please Enter a Valid Number")
            
        elif op == '5':
            print("Exiting Doctor Management")
            break
        
        else: 
            print("Invalid Choice")








    def discharge(self, patients, discharged_patients):
        print()
        print("-----Discharge Patient-----")
        self.view_patients(patients)
        
        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1
            
            if 0 <= patient_index < len(patients):
                patient_to_discharge = patients[patient_index]
                
                patients = patients[:patient_index] + patients[patient_index + 1:]
                
                discharged_patients.append(patient_to_discharge)
                
                print(f'Patient {patient_to_discharge.patient_first_name}'  
                      f'{patient_to_discharge.patient_surname} Discharged Successfully')
        
                    
                
            else:
                print("Invalid ID Entered")
                
            return patients, discharged_patients
                
        except ValueError:
            print("Invalid ID Entered")
            return patients, discharged_patients
        except Exception as e:
            print(f"An Error Occured")
            return patients, discharged_patients
            
            
            

    def view_discharged_patients(self, discharged_patients):
        print()
        print("-----Previously Discharged Patients-----")
        for i, patient in enumerate(discharged_patients, start=1):
            print(f"{i}. {patient.patient_first_name} {patient.patient_surname}")
        else:
            print("No previous discharged patients")
        
        


            







    def assign_doctor_to_patient(self, patients, doctors):
        print("-----Assign-----")
        self.view_patients(patients)

        try:
           patient_index = int(input('Please enter the patient ID: ')) - 1

           if patient_index not in range(len(patients)):
               print('The ID Entered was not found')
               return  
           
           # The Admin can add the Patients Symptoms
           new_symptoms = input("Enter Symptoms [Seperate By Commas i.e. Cough, Headache]: ").split('.')
           patients[patient_index].add_symptoms(new_symptoms)
           
           

           print("-----Doctors Select-----")
           print('Select the doctor that fits these symptoms:')
           patients[patient_index].print_symptoms() 


           self.view_doc(doctors)
           doctor_index = int(input('Please enter the doctor ID: ')) - 1

           if 0 <= doctor_index < len(doctors):
               patients[patient_index].assign_doctor(doctors[doctor_index])
               print("Patient Has Been Assigned to a Doctor")
           else:
               print("Doctor ID Invalid")
               
        except ValueError:
            print("Invalid ID Entered")











        except (ValueError, IndexError):
            print('Invalid ID entered. Please enter a valid numeric ID.')




    def update_details(self):
        print()
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            username = input("Enter the New Username: ")
            self.username = username
            print("Your Username has been changed to:",username)

        elif op == 2:
            password = input('Enter the new password: ')
            if password == input('Enter the new password again: '):
                self.password = password
                print("Password Updated Successfully")

