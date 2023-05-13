class disease:
    def __init__(self, personal_number, name, birth_certificate, doctor):
        self.personal_number = personal_number
        self.name = name
        self.birth_certificate = birth_certificate
        self.doctor = doctor
    def __str__(self):
        return F"პირადი ნომერი: {self.personal_number}, სახელი: {self.name}, დაავადები სახელი: {self.birth_certificate}, ექიმი: {self.doctor}"
    def diagnose(self, birth_certificate, doctor = None):
        if doctor is None:
            print("ექიმის მიმაგრება ვერ მოხდება")
            return
        if doctor.get_patirnt_count() < 10:
            doctor.add_patient(self)
            print(F"ექიმმა {self.name} დაუსვა დიაგნოზი")
        else:
            print("ექიმის მიმაგრება ვერ მოხდება")
class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.patient = []
    def add_patient(self, patient):
        self.patient.append(patient)
    def get_patient_count(self):
        return len(self.patient)
doctor = Doctor("ექიმმა განკურნა", "specialization")
disease = disease("1020304050", "მიხეილი", "შავი ჭირი", "doctor")
print(disease)
disease.diagnose("შავი ჭირი")