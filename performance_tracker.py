class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

def calculate_average_marks(students):
    averages = {student.name: student.average_marks() for student in students}
    return averages

def top_performer(averages):
    return max(averages, key=averages.get)

if __name__ == "__main__":
    students_data = {
        "John": [85, 78, 92],
        "Alice": [88, 79, 95],
        "Bob": [70, 75, 80]
    }
    
    students = [Student(name, marks) for name, marks in students_data.items()]
    averages = calculate_average_marks(students)
    top_student = top_performer(averages)

    print(f"Average Marks: {averages}")
    print(f"Top Performer: {top_student}")