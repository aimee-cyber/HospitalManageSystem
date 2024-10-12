# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

import time


def main():
    
    # Admin Login 
    admin = Admin('admin', '123','B1 1AB')
    
    # Initialising the actors
    doctors = [ 
        Doctor('John','Smith','Internal Med.','',''), 
        Doctor('Jone','Smith','Pediatrics', '', ''), 
        Doctor('Jone','Carlos','Cardiology', '', '')    
    ]
    

    patients = [
        Patient('Sara','Smith', 20, '07012345678','B1 234'), 
        Patient('Mike','Jones', 37,'07555551234','L2 2AB'), 
        Patient('David','Smith', 15, '07123456789','C1 ABC'),
    ]
            
    discharged_patients = []

    while True:
        if admin.login():
            running = True
            break
        else:
            print('')
            
            
    while running:
        # Printing the Menu
        print("-----Hospital Management System-----")
        print()
        print("Please Choose an Option Below [1-6]")
        print()
        print("[1] Register/View/Update/Delete Doctor")
        print()
        print("[2] Discharge Patients")
        print()
        print("[3] View Discharged Patients")
        print()
        print("[4] Assign Doctor to Patient")
        print()
        print("[5] Update Admin Details")
        print()
        print("[6] Quit")
        print()
        
        # Getting the User's Option
        optmain = input("Option: ")
        
        
        
        
        # The User Chose Option [1]
        if optmain == "1":
            # The User is Presented with the Doctor Management Page
            admin.doctor_management(doctors)
         
         
         
         
         
        # The User Chose Option [2]
        elif optmain == "2":
            # The User is Presented with the Patient Discharge Page
            patients, discharged_patients = admin.discharge(patients, discharged_patients)
            
            
            
            
        # The User Chose Option [3]
        elif optmain == "3":
            # The User is Presented with the View Discharged Patients Page
            admin.view_discharged_patients(discharged_patients)
        
        
        
        
        # The User Chose Option [4]
        elif optmain == "4":
            # The User is Presented with the Assign Doctor to Patient Page
            admin.assign_doctor_to_patient(patients, doctors)
        
        
        
        # The User Chose Option [5]
        elif optmain == "5":
            # The User is Presented with the Change Admin Details Page
            admin.update_details()
            
            
        # The User Chose Option [6]   
        elif optmain == "6":     
            print("Exiting Program...")
            time.sleep(1)
            break
        else:
            print("Invalid Option")
            
        
            
            
            
               
    


if __name__ == '__main__':
    main()

