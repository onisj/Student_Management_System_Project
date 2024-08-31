from src.person import Student, Instructor
from src.course import Course
from src.student_mgt_system import StudentManagementSystem

def main():
    sms = StudentManagementSystem()

    # Load existing data (if any)
    sms.load_data('students.csv', 'instructors.csv', 'courses.csv')

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Add Instructor")
        print("3. Add Course")
        print("4. Enroll Student in Course")
        print("5. Assign Grade")
        print("6. Get Students in Course")
        print("7. Get Courses for Student")
        print("8. Save Data and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            id_number = input("Enter student ID: ")
            major = input("Enter student major: ")
            student = Student(name=name, id_number=id_number, major=major)
            sms.add_student(student)

        elif choice == '2':
            name = input("Enter instructor name: ")
            id_number = input("Enter instructor ID: ")
            department = input("Enter instructor department: ")
            instructor = Instructor(name=name, id_number=id_number, department=department)
            sms.add_instructor(instructor)

        elif choice == '3':
            course_name = input("Enter course name: ")
            course_id = input("Enter course ID: ")
            course = Course(course_name=course_name, course_id=course_id)
            sms.add_course(course)

        elif choice == '4':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            sms.enroll_student(student_id=student_id, course_id=course_id)

        elif choice == '5':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            grade = input("Enter grade: ")
            sms.assign_grade(student_id=student_id, course_id=course_id, grade=grade)

        elif choice == '6':
            course_id = input("Enter course ID: ")
            sms.get_students_in_course(course_id=course_id)

        elif choice == '7':
            student_id = input("Enter student ID: ")
            sms.get_courses_for_student(student_id=student_id)

        elif choice == '8':
            sms.save_data('students.csv', 'instructors.csv', 'courses.csv')
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
