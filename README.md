# Student Management System Project

## Project Overview

The **Student Management System** project is designed to apply Object-Oriented Programming (OOP) principles to create a simple system for managing students, courses, and enrollments. This system demonstrates the use of classes, objects, inheritance, polymorphism, and encapsulation to provide functionalities for managing educational entities and their interactions.


<br>

## Requirements

### Class Structure

1. **Person**: A base class representing a person with common attributes for both students and instructors.
   - **Attributes**:
     - `name`: Name of the person
     - `id_number`: ID number of the person
   - **Methods**:
     - `__str__`: Returns a string representation of the person.

2. **Student**: Inherits from `Person` and includes additional attributes specific to students.
   - **Attributes**:
     - `major`: Major of the student
   - **Methods**:
     - `__str__`: Returns a string representation including the student's major.

3. **Instructor**: Inherits from `Person` and includes attributes specific to instructors.
   - **Attributes**:
     - `department`: Department of the instructor
   - **Methods**:
     - `__str__`: Returns a string representation including the instructor's department.

4. **Course**: Represents a course with its details.
   - **Attributes**:
     - `course_name`: Name of the course
     - `course_id`: ID of the course
     - `enrolled_students`: List of students enrolled in the course
   - **Methods**:
     - Methods to add and remove students.
     - `__str__`: Returns a string representation of the course.

5. **Enrollment**: Represents the enrollment of a student in a course.
   - **Attributes**:
     - `student`: The student enrolled
     - `course`: The course in which the student is enrolled
     - `grade`: The grade assigned to the student (initially set to None)
   - **Methods**:
     - Method to assign a grade to the student.
     - `__str__`: Returns a string representation of the enrollment.

6. **StudentManagementSystem**: Manages students, instructors, courses, and enrollments.
   - **Methods**:
     - Add, remove, and update students and instructors
     - Add, remove, and update courses
     - Enroll students in courses
     - Assign grades to students
     - Retrieve lists of students in a course and courses for a student
     - Load and save data to CSV files

<br>

## Functional Requirements

- **Management of Entities**:
  - Add, remove, and update students and instructors.
  - Add, remove, and update courses.

- **Enrollment and Grading**:
  - Enroll students in courses.
  - Assign grades to students for specific courses.

- **Data Retrieval**:
  - Retrieve a list of students enrolled in a specific course.
  - Retrieve a list of courses a specific student is enrolled in.

<br>

## Detailed Instructions

1. **Person Class**:
   - Define attributes `name` and `id_number`.
   - Implement the `__str__` method for string representation.

2. **Student Class**:
   - Inherit from `Person`.
   - Add `major` attribute.
   - Override `__str__` method to include the major.

3. **Instructor Class**:
   - Inherit from `Person`.
   - Add `department` attribute.
   - Override `__str__` method to include the department.

4. **Course Class**:
   - Define attributes `course_name`, `course_id`, and `enrolled_students`.
   - Include methods to manage student enrollments.
   - Override `__str__` method for string representation.

5. **Enrollment Class**:
   - Define attributes `student`, `course`, and `grade`.
   - Implement method to assign a grade.
   - Override `__str__` method for string representation.

6. **Student Management System**:
   - Implement methods to manage students, instructors, courses, and enrollments.
   - Implement methods to load and save data from/to CSV files.

<br>

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Student_Mgt_System_Project.git
   ```

2. **Navigate to the Project Directory:**
    ```bash
    cd Student_Mgt_System_Project
    ```

3. **Install Dependencies: If there are any additional dependencies, install them using pip:**
    ```bash
    pip install -r requirements.txt
    ```

<br>

## Usage

1. Run the Application:

    ```bash
    python app.py
    ```

2. Follow the Interactive Prompts:

- Add students, instructors, and courses.
- Enroll students in courses and assign grades.
- Retrieve information about enrollments and course registrations.

