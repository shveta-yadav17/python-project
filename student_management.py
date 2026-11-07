
# Student Management System

students = []

# Add Student
def add_student():
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")
    
    marks = float(input("Enter Marks (out of 100): "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)
    print("\nStudent Added Successfully!")


# Display All Students
def display_students():
    if not students:
        print("\nNo Student Records Found!")
        return

    print("\n----- Student Records -----")

    for student in students:
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Marks:", student["marks"])
        print("Percentage:", student["marks"], "%")
        print("------------------------")


# Search Student
def search_student():
    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["roll_no"] == roll:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Marks:", student["marks"])
            return

    print("Student Not Found!")


# Update Student
def update_student():
    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student["roll_no"] == roll:
            student["name"] = input("Enter New Name: ")
            student["marks"] = float(input("Enter New Marks: "))
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")


# Delete Student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["roll_no"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")


# Main Menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You for Using Student Management System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
