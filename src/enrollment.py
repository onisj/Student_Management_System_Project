class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None

    def assign_grade(self, grade):
        self.grade = grade

    def __str__(self):
        return f"Student: {self.student.name}, Course: {self.course.course_name}, Grade: {self.grade}"
