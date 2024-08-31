from src.person import Student, Instructor
from src.course import Course
from src.enrollment import Enrollment

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.instructors = []
        self.courses = []
        self.enrollments = []

    # Methods for managing students
    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            print(f"Added student: {student}")
        else:
            print("Invalid student object.")

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.id_number != student_id]
        print(f"Removed student with ID: {student_id}")

    def update_student(self, student_id, name=None, major=None):
        for student in self.students:
            if student.id_number == student_id:
                if name:
                    student.name = name
                if major:
                    student.major = major
                print(f"Updated student: {student}")
                return
        print("Student not found.")

    # Methods for managing instructors
    def add_instructor(self, instructor):
        if isinstance(instructor, Instructor):
            self.instructors.append(instructor)
            print(f"Added instructor: {instructor}")
        else:
            print("Invalid instructor object.")

    def remove_instructor(self, instructor_id):
        self.instructors = [i for i in self.instructors if i.id_number != instructor_id]
        print(f"Removed instructor with ID: {instructor_id}")

    def update_instructor(self, instructor_id, name=None, department=None):
        for instructor in self.instructors:
            if instructor.id_number == instructor_id:
                if name:
                    instructor.name = name
                if department:
                    instructor.department = department
                print(f"Updated instructor: {instructor}")
                return
        print("Instructor not found.")

    # Methods for managing courses
    def add_course(self, course):
        if isinstance(course, Course):
            self.courses.append(course)
            print(f"Added course: {course}")
        else:
            print("Invalid course object.")

    def remove_course(self, course_id):
        self.courses = [c for c in self.courses if c.course_id != course_id]
        print(f"Removed course with ID: {course_id}")

    def update_course(self, course_id, course_name=None):
        for course in self.courses:
            if course.course_id == course_id:
                if course_name:
                    course.course_name = course_name
                print(f"Updated course: {course}")
                return
        print("Course not found.")

    # Methods for managing enrollments
    def enroll_student(self, student_id, course_id):
        student = next((s for s in self.students if s.id_number == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)
        
        if student and course:
            enrollment = Enrollment(student, course)
            self.enrollments.append(enrollment)
            course.enrolled_students.append(student)
            print(f"Enrolled student {student_id} in course {course_id}")
        else:
            print("Invalid student ID or course ID.")

    def assign_grade(self, student_id, course_id, grade):
        enrollment = next((e for e in self.enrollments if e.student.id_number == student_id and e.course.course_id == course_id), None)
        
        if enrollment:
            enrollment.grade = grade
            print(f"Assigned grade {grade} to student {student_id} for course {course_id}")
        else:
            print("Enrollment not found.")

    def get_students_in_course(self, course_id):
        course = next((c for c in self.courses if c.course_id == course_id), None)
        
        if course:
            students = [s for s in course.enrolled_students]
            print(f"Students enrolled in course {course_id}: {[s.name for s in students]}")
            return students
        else:
            print("Course not found.")
            return []

    def get_courses_for_student(self, student_id):
        student_courses = [e.course for e in self.enrollments if e.student.id_number == student_id]
        
        if student_courses:
            print(f"Courses for student {student_id}: {[c.course_name for c in student_courses]}")
            return student_courses
        else:
            print("Student not found or has no enrolled courses.")
            return []
        
        
        


# This one automatically inserts data

from src.person import Student, Instructor
from src.course import Course
from src.student_mgt_system import StudentManagementSystem

# Create an instance of the StudentManagementSystem
sms = StudentManagementSystem()

# Create some example data
student1 = Student(name="Alice", id_number="S001", major="Computer Science")
instructor1 = Instructor(name="Dr. Smith", id_number="I001", department="Computer Science")
course1 = Course(course_name="Introduction to Programming", course_id="C001")

# Add example data
sms.add_student(student1)
sms.add_instructor(instructor1)
sms.add_course(course1)

# Enroll student in course
sms.enroll_student(student_id="S001", course_id="C001")

# Assign grade
sms.assign_grade(student_id="S001", course_id="C001", grade="A")

# Retrieve data
sms.get_students_in_course(course_id="C001")
sms.get_courses_for_student(student_id="S001")