class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        self.patient_first_name = first_name
        self.patient_surname = surname
        self.patient_age = age
        self.patient_mobile = mobile
        self.patient_postcode = postcode
        self.patient_doctor = 'None'
        self.patient_symptoms = []
       

    
    def assign_doctor(self, doctor):
        self.patient_doctor = doctor
    
    
    def add_symptoms(self, new_symptoms):
        self.patient_symptoms.extend(new_symptoms)
    
    def print_symptoms(self):
        print("Symptoms:", ", ".join(self.patient_symptoms))
    
    
    
    def full_name(self) :
        return f"{self.patient_first_name} {self.patient_surname}"


    def get_doctor(self) :
        return self.doctor


    def link(self, doctor):
        self.doctor = doctor


    def __str__(self):
        return f'{self.full_name():^30}|{self.doctor:^30}|{self.age:^5}|{self.mobile:^15}|{self.postcode:^10}'

        
        
        