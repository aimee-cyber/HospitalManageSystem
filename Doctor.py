class Doctor:
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality, patients, appointments):
        self.first_name = first_name
        self.surname = surname
        self.speciality = speciality
        self.patients = patients
        self.appointments = appointments
        


    def full_name(self) :
        return f"{self.first_name} {self.surname}"
    
    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self, new_first_name):
        self.first_name = new_first_name
    
    def get_surname(self):
        return self.surname
    
    def set_surname(self, new_surname):
        self.surname = new_surname
    
    def get_speciality(self):
        return self.speciality
    
    def set_speciality(self, new_speciality):
        self.speciality = new_speciality
    
    
    def add_patient(self, patient):
        self.patients.append(patient)


    def __str__(self) :
        return f'{self.full_name():^30}|{self.speciality:^15}'
    
    

   

            
        
        
    