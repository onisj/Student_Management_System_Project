import csv
import os
from src.person import Student, Instructor
from src.course import Course
from src.enrollment import Enrollment

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.instructors = []
        self.courses = []
        self.enrollments = []
        self.database_dir = "database"  # Directory to store CSV files

        # Ensure the database directory exists
        os.makedirs(self.database_dir, exist_ok=True)

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

    # Methods for loading and saving data to CSV files
    def load_data(self, students_file, instructors_file, courses_file):
        # Load students
        students_path = os.path.join(self.database_dir, students_file)
        if os.path.exists(students_path):
            with open(students_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(name=row["name"], id_number=row["id_number"], major=row["major"])
                    self.add_student(student)

        # Load instructors
        instructors_path = os.path.join(self.database_dir, instructors_file)
        if os.path.exists(instructors_path):
            with open(instructors_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    instructor = Instructor(name=row["name"], id_number=row["id_number"], department=row["department"])
                    self.add_instructor(instructor)

        # Load courses
        courses_path = os.path.join(self.database_dir, courses_file)
        if os.path.exists(courses_path):
            with open(courses_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    course = Course(course_name=row["course_name"], course_id=row["course_id"])
                    self.add_course(course)

    def save_data(self, students_file, instructors_file, courses_file):
        # Save students
        students_path = os.path.join(self.database_dir, students_file)
        with open(students_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "id_number", "major"])
            writer.writeheader()
            for student in self.students:
                writer.writerow({"name": student.name, "id_number": student.id_number, "major": student.major})

        # Save instructors
        instructors_path = os.path.join(self.database_dir, instructors_file)
        with open(instructors_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "id_number", "department"])
            writer.writeheader()
            for instructor in self.instructors:
                writer.writerow({"name": instructor.name, "id_number": instructor.id_number, "department": instructor.department})

        # Save courses
        courses_path = os.path.join(self.database_dir, courses_file)
        with open(courses_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["course_name", "course_id"])
            writer.writeheader()
            for course in self.courses:
                writer.writerow({"course_name": course.course_name, "course_id": course.course_id})
