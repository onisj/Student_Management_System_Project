class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []

    def add_student(self, student):
        self.enrolled_students.append(student)

    def remove_student(self, student):
        self.enrolled_students.remove(student)

    def __str__(self):
        student_names = ", ".join([student.name for student in self.enrolled_students])
        return f"Course: {self.course_name}, ID: {self.course_id}, Enrolled Students: [{student_names}]"
