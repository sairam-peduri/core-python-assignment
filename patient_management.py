class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

def search_patients_by_disease(patients, disease):
    return [patient.name for patient in patients if patient.disease == disease]

if __name__ == "__main__":
    patients_data = [
        {"Name": "Alice", "Age": 30, "Disease": "Flu"},
        {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
        {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
    ]
    
   